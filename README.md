# Weather App with FastAPI and Redis

This project is a weather application built with FastAPI, Jinja2 for templating, and Redis for caching. The app fetches weather data from the Visual Crossing Weather API and displays it in a user-friendly format. The weather data is cached in Redis with a 24-hour expiration to improve performance and reduce API calls.

## Features

- Search for weather data by city.
- Display weather data in a card layout.
- Cache weather data in Redis for 24 hours.

## Getting Started

### Prerequisites

- Python 3.8+
- Redis
- Visual Crossing Weather API key

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up Redis:**

   - Ensure Redis is installed and running on your local machine. You can start it using:
     ```sh
     redis-server
     ```

5. **Configure the Visual Crossing Weather API key:**
   - Replace `YOUR_API_KEY` in the `main.py` file with your actual API key:
     ```python
     "key": "YOUR_API_KEY"
     ```

### Running the Application

1. **Start the FastAPI server:**

   ```sh
   uvicorn main:app --reload
   ```

2. **Open your browser** and go to `http://localhost:8000`. You should see a search form and the weather data displayed as cards for the specified city.

### Usage

- Enter a city name in the search form to get the weather data for that city.
- The weather data is displayed in a card layout, showing the date, max temperature, min temperature, and average temperature.
- The data is cached in Redis for 24 hours to reduce the number of API calls.

### Project Structure
