# 🚁 Crazyflie Autonomous UAV Navigation

> Python-based autonomous flight experiment using the Bitcraze Crazyflie platform and high-level trajectory control.

## Overview

This project demonstrates autonomous Crazyflie flight through a programmed sequence of takeoff, circular trajectories, altitude changes, return-to-origin, and landing.

The flight path is generated mathematically and sent to the Crazyflie's high-level commander through the Bitcraze Python library (`cflib`).

## ✨ Demonstrated Capabilities

- Crazyflie radio communication
- Python-based flight control
- Autonomous takeoff and landing
- Circular trajectory generation
- Clockwise and counter-clockwise flight
- Altitude transition from 0.5 m to 1.0 m
- Kalman estimation reset before flight
- Return-to-origin maneuver

## 🏗️ Flight Sequence

```text
Connect
  ↓
Reset Kalman Estimation
  ↓
Takeoff → 0.5 m
  ↓
Clockwise Circle
  ↓
Ascend → 1.0 m
  ↓
Counter-clockwise Circle
  ↓
Return to Origin
  ↓
Land
```

## 📐 Trajectory Generation

The circular path is generated from:

```text
x = r cos(θ)
y = r sin(θ)
```

where `r` is the circle radius and `θ` is incremented over 36 waypoints.

Current demonstration parameters:

| Parameter | Value |
|---|---:|
| Circle radius | 0.5 m |
| First altitude | 0.5 m |
| Second altitude | 1.0 m |
| Waypoints / circle | 36 |
| Flight direction | Clockwise + counter-clockwise |

## 🛠️ Requirements

- Bitcraze Crazyflie
- Crazyradio / compatible Crazyflie radio link
- Python 3
- `cflib`
- Suitable indoor flight environment

Install the Python library:

```bash
pip install cflib
```

## 🚀 Running

1. Charge and prepare the Crazyflie.
2. Connect the Crazyradio adapter.
3. Verify the radio URI in the script.
4. Place the Crazyflie in a safe, open indoor area.
5. Run:

```bash
python "dual circle.py"
```

> **Safety:** Autonomous flight should be performed only in an appropriate test area with sufficient clearance and a manual recovery procedure available.

## ⚙️ Configuration

The radio URI can be supplied through the environment or changed in the script:

```python
URI = uri_helper.uri_from_env(
    default="radio://0/90/2M/E7E7E7E7E5"
)
```

## 📁 Repository

```text
crazyflie-uav-navigation/
├── dual circle.py
└── README.md
```

## 🗺️ Future Work

- Lighthouse-based position tracking
- Closed-loop position control
- Logged trajectory analysis
- More complex 3D trajectories
- Autonomous obstacle avoidance
- Multi-Crazyflie swarm coordination

## 👨‍💻 Author

**Mohammed Yusuf Khatai**  
Electronics & Telecommunication Engineering Student

## 📄 License

MIT License
