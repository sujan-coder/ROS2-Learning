# 🤖 ROS2-Learning: Jazzy Jalisco 

[![ROS2](https://img.shields.io/badge/ROS2-Jazzy-blue)](https://docs.ros.org/en/jazzy/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-24.04-orange)](https://ubuntu.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A structured, hands-on learning journey for **ROS2 Jazzy** fundamentals. This repository documents my path from beginner concepts to working with custom nodes, interfaces, and parameters.

## 🎯 Purpose

This repo is designed for anyone who wants to:
- Learn core ROS2 concepts by **doing**, not just reading.
- Understand how to build both **Python** and **C++** nodes in the same workspace.
- Create **custom messages and services**.
- Use **parameters** for dynamic node configuration.
- Build a solid foundation before moving to complex robotics projects.

## 🧠 Concepts Covered

| Concept | Implementation | Language |
|---------|----------------|-----------|
| Simple Node | `my_first_node` | Python / C++ |
| Publisher | `robot_news_station` | Python |
| Subscriber | `smartphone` | Python |
| Custom Message | `HardwareStatus.msg` | Interface |
| Service Server | `battery_node` | Python |
| Service Client | `battery_client` | Python |
| ROS2 Parameters | `yaml_params/robot_params.yaml` | Python |

## 🛠️ Setup & Build

Follow these steps to build and run the workspace on Ubuntu 24.04:

### Prerequisites
- Ubuntu 24.04 (or 22.04 with ROS2 Jazzy)
- [ROS2 Jazzy installed](https://docs.ros.org/en/jazzy/Installation.html)
- Basic knowledge of terminal and colcon

### 1. Clone the repository
```bash
git clone https://github.com/sujan-coder/ROS2-Learning.git
cd ROS2-Learning
