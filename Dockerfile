# Use the official Python image from the Docker Hub
FROM python:alpine3.20

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Start Uvicorn with live reload
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
