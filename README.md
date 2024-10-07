# Weather App with FastAPI and Redis

This app is designed to fetch and display weather data in a user-friendly format, using Redis for caching to improve performance. It connects to the Visual Crossing Weather API to retrieve real-time weather information, which is stored temporarily to avoid frequent API calls. Redis ensures that data is cached until midnight, at which point it expires and updates with fresh data.

Docker provides the infrastructure needed to run both the app and the Redis server seamlessly, making the app easy to deploy and manage in any environment.

## Features

- Search by city: Users can search for weather information by entering a city name.
- Weather data in a card layout: Displays weather details in a simple, visually appealing card format, providing a quick snapshot of the current weather conditions.
- Redis caching: Weather data is cached in Redis, improving performance by reducing repetitive API calls. Cached data is set to expire at midnight each day to ensure up-to-date information.
- Docker integration: The app and Redis server run in Docker containers, making setup and deployment straightforward across different systems.

## Tools & Technologies

- FastAPI: High-performance web framework for building APIs.
- Jinja2: Powerful templating engine for rendering HTML responses.
- Redis: In-memory key-value store used for caching weather data.
- httpx: Asynchronous HTTP client for making requests to the Visual Crossing Weather API.
- Docker: Containerization tool to run both the FastAPI app and Redis server seamlessly.
