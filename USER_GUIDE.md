# PULSE User Guide

## Industrial Equipment Condition Monitoring System

PULSE is a software prototype that provides a live view of changing industrial equipment parameters and classifies the equipment condition as **Normal, Warning, or Critical**.

---

## 1. What PULSE Monitors

The system currently monitors four equipment parameters:

- **Pressure**
- **Temperature**
- **Vibration**
- **Flow Rate**

These values change continuously in the prototype to simulate changing equipment conditions.

---

## 2. Understanding the Dashboard

When the PULSE application is running, the dashboard displays the current equipment readings.

The main information to observe includes:

- Equipment ID
- Pressure
- Temperature
- Vibration
- Flow Rate
- Current equipment status

---

## 3. Understanding Equipment Status

PULSE uses predefined thresholds to classify the current equipment condition.

### 🟢 NORMAL

The monitored parameters are within the normal operating range.

### 🟡 WARNING

One or more parameters are approaching an abnormal range.

This indicates that the equipment condition should receive attention.

### 🔴 CRITICAL

One or more parameters have exceeded a critical threshold.

This represents a condition that requires immediate attention in a real industrial monitoring scenario.

---

## 4. How to Use the Dashboard

### Step 1 — Start the application

Launch the PULSE Streamlit application.

### Step 2 — Observe the equipment readings

Monitor the displayed pressure, temperature, vibration and flow-rate values.

### Step 3 — Observe the status

Watch how the equipment status changes as the simulated readings change.

### Step 4 — Interpret the condition

Use the status indicator to understand whether the current simulated equipment condition is:

- Normal
- Warning
- Critical

---

## 5. Important Note

The current PULSE prototype uses **simulated equipment data** for demonstration.

It is not connected to physical industrial equipment or live sensors yet.

The prototype demonstrates the software monitoring concept and provides a foundation for future integration with physical sensors and embedded hardware.

---

## 6. Future Use

Future versions of PULSE may support:

- Physical sensor integration
- ESP32 or other embedded hardware
- Real-time equipment data
- Multiple equipment units
- Automated notifications
- PLC integration
- SCADA/DCS integration
- Predictive maintenance features

---

## 7. Project

PULSE was developed as part of the **30-Day Tech Build-a-thon with RadianceKing**.

**Theme:** One Project. Thirty Days. Endless Growth.

**Tagline:** Start Small. Build Daily. Launch Proudly.

---

## Developer

**Georgina Adhekugwu**

Computer Engineering undergraduate interested in data analytics, industrial automation, AI & automation, equipment monitoring and engineering safety.
