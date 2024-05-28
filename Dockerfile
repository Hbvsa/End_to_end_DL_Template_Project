# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the Flask app runs on
EXPOSE 80

# Set environment variables for Flask
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Run the Flask app
CMD ["python", "app.py"]
