#!/bin/bash

# Navigate to the training directory
cd training

# Build the Docker image
docker build -t training-container .

# Ensure the host model folder exists
mkdir -p model

# Run the training container with volume mapping
docker run --rm \
  -v $(pwd)/model:/app/model \
  training-container

# Check if the .tflite file was generated
if [ -f "model/fault_detection_model.tflite" ]; then
    echo "Model training and conversion completed. .tflite file found in training/model/."

    # Remove the old model file
    rm -f ../tensor-flow-lite/fault_detection_model.tflite

    # Copy the .tflite file to the tensor-flow-lite folder
    cp model/fault_detection_model.tflite ../tensor-flow-lite/
    echo "TensorFlow Lite model copied to ../tensor-flow-lite/"
else
    echo "Error: TensorFlow Lite model not found in training/model/."
    exit 1
fi
