# Use the official Python image from the Docker Hub
FROM python:3.12

# Install Redis server
RUN apt-get update && apt-get install -y redis-server

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the ports used by your application and Redis
EXPOSE 80 6379

# Start Redis server and your application
CMD ["sh", "-c", "service redis-server start && uvicorn main:app --host 0.0.0.0 --port 80 --reload"]
