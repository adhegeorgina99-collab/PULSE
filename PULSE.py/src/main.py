import csv
import random
import time
from datetime import datetime
from pathlib import Path


# ==============================
# PULSE EQUIPMENT CONFIGURATION
# ==============================

EQUIPMENT_ID = "VALVE-001"

# Location of the Data folder
DATA_FOLDER = Path(__file__).resolve().parent.parent / "Data"

# Name of the CSV file
CSV_FILE = DATA_FOLDER / "equipment_readings.csv"


# ==============================
# CREATE DATA FOLDER
# ==============================

DATA_FOLDER.mkdir(exist_ok=True)


# ==============================
# GENERATE EQUIPMENT READING
# ==============================

def generate_reading():
    """
    Generate one simulated equipment reading.
    """

    pressure = round(random.gauss(72, 5), 2)
    temperature = round(random.gauss(65, 4), 2)
    vibration = round(random.gauss(2.2, 0.5), 2)
    flow_rate = round(random.gauss(85, 5), 2)

    # Prevent unrealistic negative values
    pressure = max(0, pressure)
    temperature = max(0, temperature)
    vibration = max(0, vibration)
    flow_rate = max(0, flow_rate)

    # Determine equipment condition
    if (
        pressure > 95
        or temperature > 80
        or vibration > 5
        or flow_rate < 65
    ):
        status = "CRITICAL"

    elif (
        pressure > 85
        or temperature > 75
        or vibration > 4
        or flow_rate < 75
    ):
        status = "WARNING"

    else:
        status = "NORMAL"

    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "equipment_id": EQUIPMENT_ID,
        "pressure_bar": pressure,
        "temperature_c": temperature,
        "vibration_mm_s": vibration,
        "flow_rate_l_min": flow_rate,
        "status": status
    }


# ==============================
# SAVE READING TO CSV
# ==============================

def save_reading(reading):
    """
    Save a reading into the CSV file.
    """

    file_exists = CSV_FILE.exists()

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "timestamp",
                "equipment_id",
                "pressure_bar",
                "temperature_c",
                "vibration_mm_s",
                "flow_rate_l_min",
                "status"
            ]
        )

        # Create column headings if this is a new file
        if not file_exists:
            writer.writeheader()

        writer.writerow(reading)


# ==============================
# START PULSE
# ==============================

print("=" * 60)
print("PULSE - INDUSTRIAL EQUIPMENT CONDITION MONITORING SYSTEM")
print("=" * 60)
print(f"Monitoring equipment: {EQUIPMENT_ID}")
print("Automatic readings have started.")
print("Press CTRL + C to stop.")
print()


# ==============================
# AUTOMATIC READING GENERATOR
# ==============================

try:

    while True:

        reading = generate_reading()

        save_reading(reading)

        print(
            f"[{reading['timestamp']}] "
            f"{reading['equipment_id']} | "
            f"Pressure: {reading['pressure_bar']} bar | "
            f"Temperature: {reading['temperature_c']} °C | "
            f"Vibration: {reading['vibration_mm_s']} mm/s | "
            f"Flow: {reading['flow_rate_l_min']} L/min | "
            f"Status: {reading['status']}"
        )

        # Wait 5 seconds before generating another reading
        time.sleep(5)

except KeyboardInterrupt:

    print()
    print("PULSE monitoring stopped.")