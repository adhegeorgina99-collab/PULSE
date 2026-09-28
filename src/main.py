import csv
import random
import time
from datetime import datetime
from pathlib import Path

import gspread
from google.oauth2.service_account import Credentials


# ==============================
# GOOGLE SHEETS CONFIGURATION
# ==============================

SPREADSHEET_ID = "1LfCZ-iw3Nlbll3-OuzEBcagItR9HOP_MyklvF5A37pk"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

CREDENTIALS_FILE = (
    Path(__file__).resolve().parent.parent / "credentials.json"
)

credentials = Credentials.from_service_account_file(
    CREDENTIALS_FILE,
    scopes=SCOPES
)

client = gspread.authorize(credentials)

spreadsheet = client.open_by_key(SPREADSHEET_ID)

worksheet = spreadsheet.sheet1


# ==============================
# PULSE EQUIPMENT CONFIGURATION
# ==============================

EQUIPMENT_ID = "VALVE-001"

DATA_FOLDER = (
    Path(__file__).resolve().parent.parent / "Data"
)

CSV_FILE = DATA_FOLDER / "equipment_readings.csv"

DATA_FOLDER.mkdir(exist_ok=True)


# ==============================
# GENERATE EQUIPMENT READING
# ==============================

def generate_reading():

    # Generate changing equipment parameters
    pressure = round(random.gauss(72, 7), 2)

    temperature = round(random.gauss(65, 7), 2)

    vibration = round(random.gauss(2.2, 0.8), 2)

    flow_rate = round(random.gauss(85, 8), 2)


    # Prevent unrealistic negative values
    pressure = max(0, pressure)

    temperature = max(0, temperature)

    vibration = max(0, vibration)

    flow_rate = max(0, flow_rate)


    # ==============================
    # DETERMINE EQUIPMENT CONDITION
    # ==============================

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


    # ==============================
    # CREATE TIMESTAMP
    # ==============================

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    return {
        "timestamp": timestamp,
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

    file_exists = CSV_FILE.exists()

    with open(
        CSV_FILE,
        "a",
        newline=""
    ) as file:

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

        if not file_exists:
            writer.writeheader()

        writer.writerow(reading)


# ==============================
# SEND READING TO GOOGLE SHEETS
# ==============================

def send_to_google_sheets(reading):

    worksheet.append_row([
        reading["timestamp"],
        reading["equipment_id"],
        reading["pressure_bar"],
        reading["temperature_c"],
        reading["vibration_mm_s"],
        reading["flow_rate_l_min"],
        reading["status"]
    ])


# ==============================
# START PULSE
# ==============================

print("=" * 60)

print(
    "PULSE - INDUSTRIAL EQUIPMENT "
    "CONDITION MONITORING SYSTEM"
)

print("=" * 60)

print(
    f"Monitoring equipment: {EQUIPMENT_ID}"
)

print(
    "Automatic monitoring has started."
)

print(
    "A new reading will be generated every 5 seconds."
)

print(
    "Press CTRL + C to stop."
)

print()


# ==============================
# CONTINUOUS MONITORING
# ==============================

try:

    while True:

        reading = generate_reading()

        save_reading(reading)

        send_to_google_sheets(reading)


        # Display reading in PowerShell

        print(
            f"[{reading['timestamp']}] "
            f"{reading['equipment_id']} | "
            f"Pressure: "
            f"{reading['pressure_bar']} bar | "
            f"Temperature: "
            f"{reading['temperature_c']} °C | "
            f"Vibration: "
            f"{reading['vibration_mm_s']} mm/s | "
            f"Flow: "
            f"{reading['flow_rate_l_min']} L/min | "
            f"Status: "
            f"{reading['status']}"
        )


        # Wait 5 seconds

        time.sleep(5)


except KeyboardInterrupt:

    print()

    print(
        "PULSE monitoring stopped."
    )