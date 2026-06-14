import random
import pandas as pd
from datetime import datetime
import os

# Generate virtual sensor values
voltage = random.randint(220, 240)
current = round(random.uniform(1, 10), 2)

# Calculations
power = round(voltage * current, 2)
energy = round(power / 1000, 3)
cost = round(energy * 8, 2)

# Alert Logic
alert = "NORMAL"

if power > 1500:
    alert = "HIGH CONSUMPTION"

# Display Output
print("\nSMART HOME ENERGY MONITORING SYSTEM\n")

print("Voltage:", voltage, "V")
print("Current:", current, "A")
print("Power:", power, "W")
print("Energy:", energy, "kWh")
print("Estimated Cost: ₹", cost)
print("Status:", alert)

# Create DataFrame
data = {
    "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    "Voltage": [voltage],
    "Current": [current],
    "Power": [power],
    "Energy": [energy],
    "Cost": [cost],
    "Alert": [alert]
}

df = pd.DataFrame(data)

# CSV file path
csv_file = "data/energy_log.csv"

# Write header only if file does not exist
if not os.path.exists(csv_file):
    df.to_csv(csv_file, index=False)
else:
    df.to_csv(csv_file, mode="a", header=False, index=False)

print("\nData Saved Successfully")