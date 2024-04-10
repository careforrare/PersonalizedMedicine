FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app
# Make port 8000 available to the world outside this container

# Run the application
CMD ["python","main.py"]
