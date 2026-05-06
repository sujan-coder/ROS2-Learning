# 🤖 ROS2-Learning: Jazzy Basics

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

## 📂 Repository Structure
ROS2-Learning/
├── src/
│ ├── my_py_pkg/ # Python nodes
│ │ ├── my_py_pkg/
│ │ │ ├── my_first_node.py
│ │ │ ├── robot_news_station.py
│ │ │ ├── smartphone.py
│ │ │ ├── battery_node.py
│ │ │ └── battery_client.py
│ │ ├── setup.py
│ │ ├── package.xml
│ │ └── resource/
│ ├── my_cpp_pkg/ # C++ nodes
│ │ ├── src/
│ │ │ ├── my_first_node.cpp
│ │ │ └── robot_news_station.cpp
│ │ ├── include/
│ │ ├── CMakeLists.txt
│ │ └── package.xml
│ └── my_robot_interfaces/ # Custom .msg and .srv definitions
│ ├── msg/
│ │ └── HardwareStatus.msg
│ ├── srv/
│ │ └── ComputeBatteryStatus.srv
│ ├── CMakeLists.txt
│ └── package.xml
├── yaml_params/ # Parameter YAML files
│ └── robot_params.yaml
├── .gitignore
├── LICENSE
└── README.md
