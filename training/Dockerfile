# Use a lightweight Python base image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies required for TensorFlow and data processing
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Install Python dependencies directly via pip
RUN pip install --upgrade pip && \
    pip install --no-cache-dir \
        tensorflow==2.14.0 \
        pandas==2.2.3 \
        "numpy<2" \
        scikit-learn==1.2.2

# Copy the training script and data generation script into the Docker image
COPY train.py .
COPY generate_dataset.py .

# Run data generation and training script by default
CMD ["bash", "-c", "python generate_dataset.py && python train.py"]
