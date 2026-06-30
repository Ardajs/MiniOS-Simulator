# MiniOS Simulator

An interactive Operating System simulator developed in Python to demonstrate core operating system concepts including Process Management, CPU Scheduling, Memory Management, I/O Waiting, and Deadlock Detection.

The project provides both a console-based simulator and a modern Streamlit dashboard for visualizing how operating systems manage processes and hardware resources.

---

# Project Overview

Operating systems are one of the most important software layers in computer systems. They are responsible for managing CPU time, memory, processes, I/O devices, and shared resources.

MiniOS Simulator is an educational project that simplifies these concepts into an interactive simulation platform. Instead of explaining algorithms only theoretically, this project allows users to visualize how an operating system behaves under different scenarios.

The simulator was developed as an Operating Systems course project and aims to provide a practical understanding of classical operating system algorithms.

---

# Features

## Process Management

- Process Creation
- Process States
- State Transitions
- Process Information Management

Supported states

- NEW
- READY
- RUNNING
- WAITING
- TERMINATED

---

## CPU Scheduling

Implemented algorithms

- FCFS (First Come First Serve)
- SJF (Shortest Job First)
- Priority Scheduling
- Round Robin Scheduling

Performance metrics

- Average Waiting Time
- Average Turnaround Time
- CPU Utilization

Visualization

- Gantt Chart
- Interactive Gantt Chart
- Algorithm Comparison Table
- Best Algorithm Recommendation

---

## Memory Management

Implemented algorithms

- First Fit
- Best Fit
- Worst Fit

Features

- Memory Allocation
- Memory Deallocation
- Free Block Merging
- External Fragmentation Analysis
- Memory Statistics
- Memory Usage Visualization
- Interactive Fragmentation Scenario

---

## I/O Waiting Simulation

Features

- I/O Waiting State
- READY → RUNNING → WAITING transitions
- Multiple Process Simulation
- Event Log
- I/O Gantt Chart
- CPU Utilization
- Waiting Time Analysis

---

## Deadlock Detection

Features

- Resource Allocation
- Resource Requests
- Resource Allocation Graph
- Cycle Detection
- Deadlock Detection
- Deadlock Recovery

---

## Streamlit Dashboard

Interactive web interface including

- Home
- CPU Scheduling
- Memory Management
- I/O Waiting
- Deadlock Detection
- System Report

---

# Technologies

Core Technologies

- Python 3
- Streamlit
- Plotly
- Pandas

Programming Concepts

- Object-Oriented Programming
- Data Structures
- Scheduling Algorithms
- Memory Allocation Algorithms
- Graph Algorithms

---

# Project Structure

```
MiniOS-Simulator
│
├── app.py
│
├── views/
│   ├── home.py
│   ├── cpu.py
│   ├── memory_page.py
│   ├── io_page.py
│   ├── deadlock_page.py
│   └── system_report_page.py
│
├── components/
│   ├── styles.py
│   └── ui.py
│
├── process.py
├── scheduler.py
├── memory.py
├── io_simulation.py
├── deadlock.py
├── system_report.py
│
├── scheduler_test.py
├── memory_test.py
├── io_test.py
├── deadlock_test.py
│
├── requirements.txt
└── README.md
```

---

# Architecture

The application follows a modular architecture.

```
                    MiniOS Simulator

                           │
                           ▼
                        app.py
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
         ▼                 ▼                 ▼
      views            components      Core Modules
         │                 │                 │
         ▼                 ▼                 ▼
 CPU Scheduling       Shared UI         scheduler.py
 Memory Management    CSS Styles        memory.py
 I/O Waiting                          io_simulation.py
 Deadlock Detection                     deadlock.py
 System Report
```

This architecture separates the user interface from the operating system simulation logic, making the project easier to maintain and extend.

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/MiniOS-Simulator.git
```

Go into the project folder

```bash
cd MiniOS-Simulator
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

Console version

```bash
python main.py
```

Streamlit Dashboard

```bash
streamlit run app.py
```

---

# Dashboard Modules

## Home

Displays

- Project overview
- Module descriptions
- Feature summary

---

## CPU Scheduling Dashboard

Features

- Process Table
- Algorithm Selection
- Round Robin Quantum Selection
- Gantt Chart
- Interactive Gantt Visualization
- Performance Metrics
- Scheduling Comparison
- Best Algorithm Recommendation

---

## Memory Management Dashboard

Features

- Memory Configuration
- Allocation Algorithm Selection
- Memory Layout
- Memory Statistics
- External Fragmentation
- Fragmentation Scenario
- Memory Visualization

---

## I/O Waiting Dashboard

Features

- Process Table
- Event Log
- I/O Waiting Simulation
- Gantt Chart
- Waiting Time Metrics
- CPU Utilization

---

## Deadlock Dashboard

Features

- Resource Allocation
- Resource Requests
- Resource Allocation Graph
- Deadlock Detection
- Deadlock Recovery

---

## System Report

Summarizes

- CPU Scheduling Results
- Memory Statistics
- Deadlock Status

---

# Example CPU Scheduling Output

```
FCFS

Average Waiting Time : 5.00
Average Turnaround   : 9.00
CPU Utilization      : 100%
```

---

# Example Memory Statistics

```
Used Memory          : 600 MB
Free Memory          : 424 MB
Largest Free Block   : 300 MB
External Fragmentation : 124 MB
```

---

# Example Deadlock

```
P1 -> R2
P2 -> R1
R1 -> P1
R2 -> P2

Deadlock Detected
```

---

# Learning Outcomes

This project demonstrates

- Process Scheduling
- Memory Allocation
- Process State Management
- CPU Scheduling Algorithms
- Memory Fragmentation
- I/O Waiting
- Deadlock Detection
- Deadlock Recovery
- Interactive System Visualization

---

# Development Progress

## Completed

### Process Management

- Process Creation
- Process States
- State Transitions

### CPU Scheduling

- FCFS
- SJF
- Priority Scheduling
- Round Robin
- Gantt Chart
- Interactive Visualization
- Performance Metrics
- Algorithm Comparison

### Memory Management

- First Fit
- Best Fit
- Worst Fit
- Memory Allocation
- Memory Deallocation
- Fragmentation Analysis
- Memory Visualization

### I/O Waiting

- Waiting Simulation
- Event Log
- Performance Metrics
- Visualization

### Deadlock

- Resource Allocation
- Cycle Detection
- Deadlock Detection
- Recovery Algorithm

### Dashboard

- Modular Streamlit Architecture
- Shared UI Components
- Centralized Styling

---

# Future Improvements

Planned features

- Live Process Creation
- Interactive Memory Editor
- Dynamic Resource Allocation
- Process Timeline Animation
- Export Simulation Report (PDF)
- Dark Theme
- User-defined Scheduling Algorithms
- Paging Simulation
- Segmentation Simulation
- Virtual Memory Simulation
- Banker’s Algorithm
- Multilevel Queue Scheduling
- Multilevel Feedback Queue Scheduling

---

# Why This Project?

MiniOS Simulator is designed as both a learning platform and a demonstration project.

Instead of presenting operating system concepts only theoretically, it allows users to interact with simulations and immediately observe the effects of different scheduling, memory management, I/O, and deadlock algorithms.

The modular architecture also makes it easy to extend the simulator with additional operating system components.

---

# Author

Arda Alan

Computer Engineering Student

Duzce University

---

# License

This project is developed for educational purposes.
