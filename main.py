from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import httpx
from json import JSONDecodeError, dumps, loads
import redis.asyncio as redis
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    try:
        yield {'redis_client': r}
    finally:
        await r.close()

app = FastAPI(lifespan=lifespan)

templates = Jinja2Templates(directory='templates')


async def get_weather(city: str):
    params = {
        "unitGroup": "metric",
        "key": "8V39W3U2P8D58U5CQWP2SRRTT",
        "contentType": "json",
        "include": "days",
        "elements": "datetime,tempmax,tempmin,temp"
    }
    async with httpx.AsyncClient() as client:
        r = await client.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}', params=params)
    try:
        return r.json()
    except JSONDecodeError:
        return None


@app.get('/', response_class=HTMLResponse)
async def weather_app(request: Request, city: str | None = None):
    weather_data = None
    if city:
        weather_data_str = await request.state.redis_client.get(city)
        if weather_data_str:
            weather_data = loads(weather_data_str)
        else:
            weather_data = await get_weather(city)
            await request.state.redis_client.set(city, dumps(weather_data), ex=86400)

    return templates.TemplateResponse('template.html', {'request': request, 'weather_data': weather_data, 'city': city})
