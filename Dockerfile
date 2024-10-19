# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the requirements.txt contents into the container
COPY requirements.txt requirements.txt

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install any needed Python packages
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
# Set the working directory in the container
WORKDIR /app

# Collect static files
RUN python product_management/manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=product_management.settings


# Start Django server
CMD ["python", "product_management/manage.py", "runserver", "0.0.0.0:8000"]
