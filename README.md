# PredictX

### AI-Powered Predictive Maintenance for Intelligent Machines

<p align="center">
  <img src="https://img.shields.io/badge/AI-Machine%20Learning-blue?style=flat-square">
  <img src="https://img.shields.io/badge/IoT-ESP32-orange?style=flat-square">
  <img src="https://img.shields.io/badge/Backend-Flask-black?style=flat-square">
  <img src="https://img.shields.io/badge/Python-3.x-yellow?style=flat-square&logo=python">
  <img src="https://img.shields.io/badge/Industry-4.0-purple?style=flat-square">
</p>

<p align="center">
  <b>Predict failures before they become downtime.</b>
</p>

---

## Overview

**PredictX** is an AI-driven predictive maintenance system that combines **IoT-based sensing and Machine Learning** to monitor machine health and identify abnormal operating conditions in real time.

The system continuously collects physical and electrical parameters from a motor through an **ESP32-based sensing unit**, processes the incoming data, and uses a trained Machine Learning model to determine the current operating condition.

The core idea is simple:

> **Sense → Analyze → Predict → Act**

Instead of relying solely on periodic inspection or waiting for equipment failure, PredictX enables **continuous condition monitoring and early fault detection**.

---

## Why PredictX?

Unplanned machine failures can result in significant downtime, maintenance costs, and productivity losses.

Traditional maintenance approaches are often:

* **Reactive** — maintenance after failure
* **Preventive** — maintenance based on fixed schedules

PredictX moves toward:

### **Predictive Maintenance**

Using real-time machine data to identify abnormal behavior early and support more informed maintenance decisions.

---

## System Architecture

```text
                    ┌─────────────────────┐
                    │      MACHINE        │
                    │      / MOTOR        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       SENSORS       │
                    │                     │
                    │ Temperature         │
                    │ Vibration           │
                    │ Current             │
                    │ Voltage             │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       ESP32         │
                    │   Edge Acquisition  │
                    └──────────┬──────────┘
                               │
                         Serial Data
                               │
                               ▼
                    ┌─────────────────────┐
                    │   PYTHON / FLASK    │
                    │   Data Processing   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   MACHINE LEARNING  │
                    │      MODEL          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   HEALTH / FAULT    │
                    │     PREDICTION      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   WEB INTERFACE     │
                    │   & ALERT SYSTEM    │
                    └─────────────────────┘
```

---

## Key Capabilities

### Real-Time Condition Monitoring

Continuous acquisition of machine parameters enables the system to observe changing operating conditions rather than relying on periodic measurements.

### AI-Based Fault Classification

A trained Machine Learning model analyzes sensor data and classifies the machine's operating condition.

### Multi-Parameter Analysis

Instead of depending on a single sensor, PredictX considers multiple parameters to obtain a more meaningful representation of machine health.

### Edge-to-Application Pipeline

The ESP32 acts as the edge data acquisition layer while Python and Flask handle processing, prediction, and visualization.

### Early Fault Detection

Abnormal conditions can be identified before they potentially develop into more serious equipment failures.

---

## Machine Learning Pipeline

```text
                Sensor / Historical Data
                         │
                         ▼
                  Data Preparation
                         │
                         ▼
                   Feature Set
                         │
                         ▼
                 Model Training
                         │
                         ▼
                  Model Evaluation
                         │
                         ▼
                  Trained ML Model
                         │
                         ▼
               Real-Time Inference
                         │
                         ▼
              Machine Health Status
```

The current prototype is trained using machine operating data representing conditions such as:

* Normal operation
* High temperature
* Motor obstruction
* Voltage fluctuation

The trained model is then integrated into the real-time monitoring pipeline.

---

## Technology Stack

| Layer                   | Technology            |
| ----------------------- | --------------------- |
| **Embedded / Edge**     | ESP32, Arduino/C      |
| **Data Acquisition**    | IoT Sensors           |
| **Backend**             | Python, Flask         |
| **Machine Learning**    | Scikit-learn          |
| **Data Processing**     | Pandas                |
| **Model Serialization** | Joblib                |
| **Frontend**            | HTML, CSS, JavaScript |
| **Communication**       | Serial                |

---

## Hardware

The prototype is built around an **ESP32-based motor monitoring system** with sensors for measuring parameters such as:

* 🌡️ Temperature
* 📳 Vibration
* ⚡ Voltage
* 🔌 Current

These measurements form the basis for real-time machine condition analysis.

---

## Fault Detection

PredictX currently demonstrates detection of several abnormal operating conditions:

| Condition               | Interpretation                               |
| ----------------------- | -------------------------------------------- |
| **Normal**              | Machine operating within expected conditions |
| **High Temperature**    | Abnormal thermal behavior                    |
| **Motor Obstruction**   | Possible mechanical/load abnormality         |
| **Voltage Fluctuation** | Abnormal electrical supply behavior          |

The system can be extended to support additional failure modes as more representative data becomes available.

---

## From Monitoring to Prediction

The long-term objective of PredictX is not simply to display sensor values.

It is to transform raw machine data into **actionable intelligence**.

```text
Raw Data
   ↓
Machine State
   ↓
Anomaly Detection
   ↓
Fault Classification
   ↓
Maintenance Decision
```

This creates the foundation for a scalable **condition-based maintenance platform**.

---

## Getting Started

### Prerequisites

* Python 3.x
* ESP32 development environment
* Arduino IDE
* Required Python dependencies
* Compatible sensors and motor setup

### Installation

Clone the repository:

```bash
git clone https://github.com/RiteshReddy568/Predictx.git
cd Predictx
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirments.txt
```

Start the application:

```bash
python app.py
```

Then open the local Flask address in your browser.

---

## Project Status

**Prototype — Active Development**

The current system demonstrates the complete pipeline from:

**Physical sensing → Data acquisition → Machine Learning → Real-time prediction → Web visualization**

Future development is focused on improving intelligence, scalability, and deployment readiness.

---

## Roadmap

* [ ] Advanced anomaly detection
* [ ] Automated root-cause analysis
* [ ] Remaining Useful Life (RUL) estimation
* [ ] Historical machine-health analytics
* [ ] Cloud-based monitoring
* [ ] Remote notifications
* [ ] Multi-machine support
* [ ] Edge ML deployment
* [ ] Industrial-scale deployment architecture

---

## Applications

PredictX can serve as a foundation for predictive maintenance across applications such as:

* Manufacturing equipment
* Industrial motors
* Pumps
* HVAC systems
* Rotating machinery
* Production-line equipment
* Industrial IoT systems

---

## Vision

PredictX aims to evolve from a prototype into an intelligent machine-health platform capable of answering three critical questions:

> **Is the machine healthy?**
> **If not, what is going wrong?**
> **What should be done before failure occurs?**

---

## Author

**Ritesh Reddy**

[GitHub](https://github.com/RiteshReddy568)

---

<p align="center">
  <b>PredictX</b><br>
  <sub>Intelligent monitoring. Early detection. Predictive maintenance.</sub>
</p>
