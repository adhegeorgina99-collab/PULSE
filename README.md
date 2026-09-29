# PULSE
### Industrial Equipment Condition Monitoring System

PULSE is a software prototype for monitoring industrial equipment conditions using simulated real-time equipment data.

The project explores how parameters such as **pressure, temperature, vibration, and flow rate** can be continuously monitored to identify abnormal operating conditions and support safer equipment operation.

## 🚀 Project Overview

PULSE was developed as part of the **30-Day Tech Build-a-thon by RadianceKing**, under the theme:

> One Project. Thirty Days. Endless Growth.

The project combines my interests in **computer engineering, data analytics, automation, industrial systems, and safety**.

The current version focuses on building and testing the software monitoring concept. Future development can extend the system toward physical sensors and embedded hardware.

## 🎯 Problem

Industrial equipment can operate under changing conditions, and abnormal readings may indicate a developing problem.

PULSE explores a simple monitoring approach where equipment parameters are continuously observed and classified into different operating states.

The goal is to make abnormal conditions easier to identify through a live monitoring interface.

## ⚙️ Parameters Monitored

PULSE currently monitors:

- Pressure
- Temperature
- Vibration
- Flow Rate

The system uses predefined threshold conditions to determine the equipment status.

### Status Levels

- 🟢 **NORMAL** — Parameters are within the expected operating range.
- 🟡 **WARNING** — One or more parameters are approaching an abnormal range.
- 🔴 **CRITICAL** — One or more parameters have exceeded the defined critical threshold.

## 🖥️ Current Prototype

The current PULSE prototype:

1. Generates changing equipment readings.
2. Processes the generated data.
3. Evaluates the equipment parameters against defined thresholds.
4. Determines the equipment status.
5. Displays the information through a live Streamlit dashboard.
6. Provides visual monitoring of changing equipment conditions.

The current prototype uses simulated data for demonstration purposes.

**PULSE is not yet a physical sensor-based monitoring system.** The long-term concept is to integrate real sensors and embedded hardware into the monitoring architecture.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Google Sheets
- GitHub

## 📊 Monitoring Logic

The prototype uses threshold-based rules to classify equipment conditions.

Example parameters include:

| Parameter | Monitoring Purpose |
|---|---|
| Pressure | Detect abnormal pressure conditions |
| Temperature | Identify excessive temperature |
| Vibration | Identify unusual vibration levels |
| Flow Rate | Detect reduced or abnormal flow |

The thresholds are configurable within the prototype.

## ▶️ Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/adhegeorgina99-collab/PULSE.git
