import csv
import random

# Define the output CSV file name
output_file = 'vibration_temperature_levels.csv'

# Open the CSV file for writing
with open(output_file, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # Write the header
    writer.writerow(['vibration_level', 'temperature', 'label'])

    # Generate 1000 data points
    for _ in range(1000):
        # Random vibration level between 0 and 10
        vibration_level = round(random.uniform(0, 10), 2)
        # Random temperature between 20 and 100 degrees Celsius
        temperature = round(random.uniform(20, 100), 2)

        # Lowered threshold for fault detection
        threshold = 300  # Adjust as needed for demo

        # Calculate product
        product = vibration_level * temperature

        # Define fault probability based on product
        # Linear scaling: product / threshold with a max probability
        fault_probability = min(product / threshold,
                                0.7)  # Max 70% probability

        # Assign label based on probability
        if random.random() < fault_probability:
            label = 1  # Fault Detected
        else:
            label = 0  # Normal

        # Write the row
        writer.writerow([vibration_level, temperature, label])

    print(f"CSV file '{output_file}' has been generated successfully.")
