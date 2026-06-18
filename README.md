# MiniOS-Simulator
Interactive Operating System Simulator implementing FCFS, SJF, Priority, and Round Robin scheduling algorithms with performance analysis.

# MiniOS Simulator

A simplified Operating System Simulator developed in Python to demonstrate fundamental operating system concepts such as process management, CPU scheduling, memory management, and resource allocation.

## Project Overview

Modern operating systems such as Windows and Linux manage hardware resources efficiently while allowing multiple processes to run concurrently. This project aims to simulate core operating system mechanisms in an educational and interactive way.

The simulator provides implementations of common CPU scheduling algorithms and performance analysis tools, allowing users to compare scheduling strategies and observe their effects on system performance.

---

## Features

### Process Management

Each process contains:

* Process ID (PID)
* Arrival Time
* Burst Time
* Priority
* Memory Requirement
* Process State

Supported states:

```text
NEW → READY → RUNNING → TERMINATED
```

---

### CPU Scheduling Algorithms

Implemented algorithms:

* FCFS (First Come First Serve)
* SJF (Shortest Job First)
* Priority Scheduling
* Round Robin Scheduling

---

### Performance Metrics

The simulator calculates:

* Average Waiting Time
* Average Turnaround Time
* CPU Utilization

---

### Gantt Chart Generation

Scheduling results are displayed as a Gantt Chart representation:

```text
P1 : 0 -> 2
P2 : 2 -> 4
P1 : 4 -> 6
P3 : 6 -> 7
...
```

---

### Algorithm Comparison

Algorithms can be compared using:

| Algorithm   | Avg Waiting Time | Avg Turnaround Time | CPU Utilization |
| ----------- | ---------------- | ------------------- | --------------- |
| FCFS        | ✓                | ✓                   | ✓               |
| SJF         | ✓                | ✓                   | ✓               |
| Priority    | ✓                | ✓                   | ✓               |
| Round Robin | ✓                | ✓                   | ✓               |

---

## Project Structure

```text
MiniOS-Simulator
│
├── main.py
├── process.py
├── scheduler.py
└── README.md
```

---

## Example Process Input

```python
Process("P1", 0, 7, 3, 200)
Process("P2", 2, 4, 1, 300)
Process("P3", 4, 1, 4, 150)
Process("P4", 5, 4, 2, 250)
```

---

## Example Output

```text
FCFS Scheduling

Average Waiting Time: 4.75
Average Turnaround Time: 8.75
CPU Utilization: 100%

SJF Scheduling

Average Waiting Time: 4.00
Average Turnaround Time: 8.00
CPU Utilization: 100%
```

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)

Planned:

* Streamlit
* Plotly
* Matplotlib

---

## Future Improvements

### Memory Management

* First Fit
* Best Fit
* Worst Fit
* Memory Fragmentation Analysis

### Process State Visualization

* READY
* RUNNING
* WAITING
* TERMINATED

### Deadlock Detection

* Resource Allocation Graph
* Deadlock Detection Algorithms

### Interactive Dashboard

* Streamlit Interface
* Real-Time Simulation
* Interactive Charts

---

## Educational Objectives

This project was developed to better understand:

* Process Scheduling
* CPU Resource Management
* Operating System Fundamentals
* Performance Analysis
* Algorithm Comparison

---

## Author

Arda Alan

Computer Engineering Student
Düzce University
