from flask import Flask, request, jsonify
import numpy as np
from tflite_runtime.interpreter import Interpreter as tflite

# Initialize Flask app
app = Flask(__name__)

# Load the TensorFlow Lite model
interpreter = tflite(model_path="fault_detection_model.tflite")
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input JSON data
        data = request.get_json()
        # Extract vibration level and temperature
        vibration_level = float(data['vibration_level'])
        temperature = float(data['temperature'])

        # Prepare input data
        input_data = np.array(
            [[vibration_level, temperature]], dtype=np.float32)

        # Set the input tensor
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()

        # Get the prediction
        output_data = interpreter.get_tensor(output_details[0]['index'])
        prediction = int(output_data[0][0] > 0.5)

        # Interpret the prediction
        status = "Normal" if prediction == 0 else "Fault Detected"

        # Return the status
        return jsonify({"status": status})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5050)
