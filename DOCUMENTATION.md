# PULSE — Technical Documentation

## 1. Project Overview

PULSE (Industrial Equipment Condition Monitoring System) is a software prototype designed to demonstrate how industrial equipment parameters can be monitored and assessed using automated alerts.

The prototype simulates equipment readings and displays them through a live monitoring dashboard. It is intended to demonstrate how continuous monitoring can support equipment awareness and safety.

## 2. Problem Statement

Industrial equipment requires regular monitoring to identify abnormal operating conditions. Depending entirely on manual observation can make it difficult to notice changing conditions promptly.

PULSE explores how software-based monitoring and automated status classification can help make equipment readings easier to observe and interpret.

## 3. Project Objectives

* Monitor simulated industrial equipment parameters.
* Display changing readings through a dashboard.
* Identify abnormal readings using predefined thresholds.
* Classify equipment conditions as Normal, Warning, or Critical.
* Demonstrate the potential of automation in industrial monitoring.

## 4. System Overview

PULSE currently operates as a software prototype.

Its basic workflow is:

1. Generate simulated equipment readings.
2. Process the readings.
3. Evaluate the readings against configured thresholds.
4. Assign an equipment status.
5. Display the readings and status on the monitoring dashboard.

The prototype currently uses simulated data rather than readings from physical sensors.

## 5. Monitored Parameters

The system monitors the following parameters:

| Parameter   | Description                              |
| ----------- | ---------------------------------------- |
| Pressure    | Simulated equipment pressure readings    |
| Temperature | Simulated equipment temperature readings |
| Vibration   | Simulated equipment vibration readings   |
| Flow rate   | Simulated equipment flow-rate readings   |

These parameters are used to demonstrate how changes in equipment conditions can be monitored.

## 6. Alert Classification

PULSE uses three equipment status categories:

* **NORMAL:** The readings are within the configured operating thresholds.
* **WARNING:** One or more readings have crossed a warning threshold.
* **CRITICAL:** One or more readings have crossed a critical threshold.

These classifications are intended for demonstration purposes. They are not certified industrial safety limits.

## 7. Technology Stack

The prototype uses the following technologies:

* **Python:** Application logic and simulated data generation.
* **Streamlit:** Interactive monitoring dashboard.
* **Pandas:** Data handling and processing.
* **Plotly:** Data visualization.
* **GitHub:** Source code hosting and project version control.

## 8. Dashboard

The Streamlit dashboard provides a visual interface for monitoring the simulated equipment readings.

It allows users to observe changing parameter values and the corresponding equipment status.

The dashboard demonstrates how software can present equipment information in a form that is easier to interpret.

## 9. Current Limitations

The current version of PULSE is a software prototype.

* It uses simulated readings rather than live sensor data.
* It has not yet been integrated with physical industrial equipment.
* Its thresholds are demonstration settings and should not be treated as certified safety limits.
* It has not been validated for use in actual industrial operations.

## 10. Future Development

Planned areas for further development include:

* Integrating physical sensors and microcontrollers.
* Exploring PLC and SCADA integration.
* Improving the monitoring and alerting system.
* Testing with real equipment data.
* Exploring predictive maintenance capabilities.
* Improving the dashboard and deployment options.

## 11. Project Status

PULSE has progressed from an initial concept to a functional software prototype with a live monitoring dashboard.

Further development and testing are required before it can be considered for real industrial applications.

## 12. Developer

**Adhekugwu Georgina**
Computer Engineering Undergraduate
Federal University of Petroleum Resources, Effurun
