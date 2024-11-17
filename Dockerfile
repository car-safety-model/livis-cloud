# Use an official Python image as the base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files to the working directory
COPY . .

# Expose the port if you are running a web application (optional)
EXPOSE 8000

# Define the command to run the Python script
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
