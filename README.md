# 📶🛜📡📡📶🛜 WiPulse

<p align="center">
  <img src="assets/hero-dashboard.png" alt="WiPulse Dashboard">
</p>


**Real-time contactless respiration monitoring using Wi-Fi Channel State Information (CSI), OpenWrt routers, Python signal processing, and a modern Apple-inspired dashboard.**

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![OpenWrt](https://img.shields.io/badge/OpenWrt-Compatible-green)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![Status](https://img.shields.io/badge/Status-Research-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![GitHub last commit](https://img.shields.io/github/last-commit/ziffythealien-blip/WiPulse)
![GitHub repo size](https://img.shields.io/github/repo-size/ziffythealien-blip/WiPulse)
![GitHub stars](https://img.shields.io/github/stars/ziffythealien-blip/WiPulse?style=social)

---

## 🚀 Overview

WiPulse is an experimental Wi-Fi sensing platform that uses **Channel State Information (CSI)** to detect and monitor human respiratory activity without requiring any wearable devices.

By analyzing subtle changes in Wi-Fi signal reflections caused by chest movement, the system can estimate breathing patterns in real time and display them through an intuitive web dashboard.

The project combines:

* OpenWrt-powered routers
* OWMCSI CSI extraction
* Python scientific computing
* Real-time signal processing
* Modern web visualization

---

## 🏗️ System Architecture

```text
Human Body Movement
         │
         ▼
 ┌──────────────────┐
 │ Wi-Fi Reflections│
 └────────┬─────────┘
          │
          ▼
 ┌──────────────────┐
 │ OpenWrt Router   │
 │ + OWMCSI         │
 └────────┬─────────┘
          │ UDP CSI Packets
          ▼
 ┌──────────────────┐
 │ Python Backend   │
 │ Signal Processing│
 └────────┬─────────┘
          │ REST API
          ▼
 ┌──────────────────┐
 │ WiPulse Dashboard│
 │ Charts & Metrics │
 └──────────────────┘
```

---

## 🧩 Features

* Real-time CSI acquisition
* OpenWrt integration
* OWMCSI support
* UDP packet streaming
* Digital signal processing
* Butterworth filtering
* FFT frequency analysis
* Contactless respiration monitoring
* Real-time visualization
* Historical data storage
* Alert generation
* Modern Apple-inspired UI

---

## 🧰 Technology Stack

### Router Side

#### OpenWrt

OpenWrt replaces the factory firmware and provides a Linux-based environment capable of running CSI extraction tools.

#### OWMCSI

OWMCSI captures Channel State Information from supported MediaTek and Qualcomm chipsets and streams CSI data over UDP.

---

### Backend

Python 3 with:

* NumPy
* SciPy
* Flask
* Flask-CORS

Responsibilities:

* Receive CSI packets
* Decode CSI frames
* Extract amplitude information
* Filter noise
* Estimate respiration frequency
* Generate metrics
* Serve API endpoints

---

### Frontend

The web dashboard provides:

* Live charts
* Breathing indicators
* User status visualization
* Historical monitoring
* Alert notifications

The frontend communicates directly with the Flask backend.

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/ziffythealien-blip/WiPulse.git
cd WiPulse
```

### Install Dependencies

```bash
pip install flask flask-cors numpy scipy
```

or

```bash
pip install -r requirements.txt
```

---

## 📡 Router Configuration

Install:

* OpenWrt
* OWMCSI

Start CSI streaming:

```bash
owmcsi -i wlan0 -d 192.168.1.100 -p 5500
```

Parameters:

| Parameter | Description        |
| --------- | ------------------ |
| -i        | Wireless interface |
| -d        | Destination IP     |
| -p        | UDP Port           |

Example:

```bash
owmcsi -i wlan0 -d 192.168.1.100 -p 5500
```

The router will continuously stream CSI packets to the backend.

---

## 🔬 Signal Processing Pipeline

The backend performs:

1. UDP packet reception
2. CSI extraction
3. Amplitude calculation
4. Noise reduction
5. Butterworth band-pass filtering
6. Respiration frequency isolation
7. FFT analysis
8. Respiratory rate estimation
9. Data packaging
10. API transmission to dashboard

---

## 📁 Repository Structure

```text
WiPulse/
│
├── app.py
├── index.html
├── requirements.txt
├── README.md
│
├── assets/
│   ├── dashboard.png
│   ├── architecture.png
│   └── demo.gif
│
├── docs/
│   └── setup-openwrt.md
│
└── samples/
    └── sample_data.json
```

---

## 🖥️ Dashboard

Add screenshots inside:

```text
assets/dashboard.png
```

Then display them:

```markdown
![Dashboard](assets/dashboard.png)
```

You can also add:

```markdown
![Demo](assets/demo.gif)
```

---

## ⚠️ Disclaimer

This project is intended for:

* Research
* Education
* Experimentation
* Prototyping

The measurements generated by WiPulse are **not medical-grade** and must not be used for diagnosis, treatment, or clinical decision-making.

---

## 🛣️ Roadmap

### Current

* CSI acquisition
* Respiration monitoring
* Real-time dashboard

### Planned

* Heart rate estimation
* Multi-user tracking
* Sleep monitoring
* Occupancy detection
* Activity recognition
* Machine learning models
* Mobile companion application
* Long-term analytics

---

## 🤝 Contributing

Contributions, ideas, bug reports, and pull requests are welcome.

Feel free to fork the project and submit improvements.

---

## 📜 License

This project is licensed under the MIT License.

See the LICENSE file for details.
