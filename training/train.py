import os
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('vibration_temperature_levels.csv')

# Split the data into features and labels
X = data[['vibration_level', 'temperature']]
y = data['label']

# Split into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Build the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=16,
          validation_data=(X_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy:.2f}")

# Save the model to the 'model' directory
os.makedirs('model', exist_ok=True)

# Convert and save the model in TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
with open('model/fault_detection_model.tflite', 'wb') as f:
    f.write(tflite_model)
