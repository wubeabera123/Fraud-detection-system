# Use a base image with Python
FROM python:3.8-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libopencv-dev \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DEFAULT_TIMEOUT=100
ENV PIP_CACHE_DIR="/root/.cache/pip"

# Copy requirements.txt into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Set working directory
WORKDIR /app

# Copy application code into the container
COPY . .

# Expose port (adjust if not using Flask default)
EXPOSE 5000

# Command to run the application (if using Flask)
CMD ["python", "serve_model"]
