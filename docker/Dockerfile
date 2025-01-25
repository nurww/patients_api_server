# Using the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the project files into the container
COPY . .

# Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to launch the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
