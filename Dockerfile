# Use the official Python base image
FROM python:3.8.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire FastAPI app directory into the container
COPY . .

# Expose the port that FastAPI is running on (assuming the app runs on port 8000)
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
