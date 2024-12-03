# Use a lightweight Python base image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install necessary system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pip and upgrade it
RUN pip install --upgrade pip

# Install necessary Python packages, pinning NumPy to <2.0
RUN pip install --no-cache-dir flask "numpy<2" tflite-runtime==2.14.0

# Verify tflite_runtime installation
RUN python -c "from tflite_runtime.interpreter import Interpreter; print('tflite_runtime installed successfully')"

# Set the working directory
WORKDIR /app

# Copy the TensorFlow Lite model and Flask app
COPY fault_detection_model.tflite .
COPY app.py .

# Expose the Flask API port
EXPOSE 5050

# Start the Flask app
CMD ["python", "app.py"]
