@echo off

REM Navigate to the training directory
cd training

REM Build the Docker image
docker build -t training-container .

REM Ensure the host model folder exists
if not exist model mkdir model

REM Run the training container with volume mapping
docker run --rm ^
  -v %cd%/model:/app/model ^
  training-container

REM Check if the .tflite file was generated
if exist model\fault_detection_model.tflite (
    echo Model training and conversion completed. .tflite file found in training\model\.

    REM Remove the old model file
    if exist ..\tensor-flow-lite\fault_detection_model.tflite del ..\tensor-flow-lite\fault_detection_model.tflite

    REM Copy the .tflite file to the tensor-flow-lite folder
    copy model\fault_detection_model.tflite ..\tensor-flow-lite\
    echo TensorFlow Lite model copied to ..\tensor-flow-lite\
) else (
    echo Error: TensorFlow Lite model not found in training\model\.
    exit /b 1
)
