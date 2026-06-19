# MiniOS Simulator

A simplified Operating System Simulator developed in Python to demonstrate fundamental operating system concepts such as process management, CPU scheduling, memory management, and resource allocation.

## Project Overview

Modern operating systems such as Windows and Linux manage hardware resources efficiently while allowing multiple processes to run concurrently. This project aims to simulate core operating system mechanisms in an educational and interactive way.

The simulator provides implementations of common CPU scheduling algorithms and performance analysis tools, allowing users to compare scheduling strategies and observe their effects on system performance.

---

## Implemented Features

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
NEW
READY
RUNNING
TERMINATED
```

---

## CPU Scheduling Algorithms

### FCFS (First Come First Serve)

Processes are executed according to their arrival order.

### SJF (Shortest Job First)

The shortest available job is selected first.

### Priority Scheduling

Processes are selected based on priority values.

### Round Robin

Time-sharing scheduling using configurable time quantum.

---

## Scheduling Metrics

The simulator calculates:

* Average Waiting Time
* Average Turnaround Time
* CPU Utilization

---

## Gantt Chart Generation

Example:

```text
P1 : 0 -> 2
P2 : 2 -> 4
P1 : 4 -> 6
P3 : 6 -> 7
P2 : 7 -> 9
P4 : 9 -> 11
```

---

## Scheduling Comparison

Algorithms can be compared using performance metrics.

| Algorithm   | Waiting Time | Turnaround Time | CPU Utilization |
| ----------- | ------------ | --------------- | --------------- |
| FCFS        | ✓            | ✓               | ✓               |
| SJF         | ✓            | ✓               | ✓               |
| Priority    | ✓            | ✓               | ✓               |
| Round Robin | ✓            | ✓               | ✓               |

---

# Memory Management

The simulator includes dynamic memory allocation mechanisms similar to those used by operating systems.

---

## Memory Allocation Algorithms

### First Fit

Allocates memory in the first free block large enough for the process.

### Best Fit

Allocates memory in the smallest suitable free block.

### Worst Fit

Allocates memory in the largest available free block.

---

## Memory Operations

### Allocation

Example:

```text
[FREE 1024 MB]

P1 = 200 MB
```

Result:

```text
[P1 200 MB][FREE 824 MB]
```

---

### Deallocation

Example:

```text
[P1][P2][P3][FREE]
```

Remove P2:

```text
[P1][FREE][P3][FREE]
```

---

### Free Block Merging

Adjacent free blocks are automatically merged.

Before:

```text
[FREE 300 MB][FREE 374 MB]
```

After:

```text
[FREE 674 MB]
```

---

## Fragmentation Testing

The simulator supports custom fragmentation scenarios to compare allocation algorithms.

Implemented:

* Memory allocation testing
* Memory deallocation testing
* Free block merging
* Fragmentation analysis scenarios

---

## Project Structure

```text
MiniOS-Simulator
│
├── main.py
├── process.py
├── scheduler.py
├── memory.py
├── README.md
└── requirements.txt
```

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)

Future:

* Streamlit
* Plotly
* Matplotlib

---

## Development Progress

### Completed

* Process Management
* FCFS Scheduling
* SJF Scheduling
* Priority Scheduling
* Round Robin Scheduling
* CPU Metrics
* Gantt Chart Generation
* Scheduling Comparison
* Memory Block Structure
* First Fit Allocation
* Best Fit Allocation
* Worst Fit Allocation
* Memory Deallocation
* Free Block Merging
* Fragmentation Test Infrastructure

### In Progress

* Memory Statistics
* External Fragmentation Metrics

### Planned

* Process Waiting State (I/O Simulation)
* Deadlock Detection
* Resource Allocation Graph
* Streamlit Dashboard
* Interactive Visualization
* Real-Time Simulation

---

## Educational Objectives

This project aims to provide hands-on experience with:

* Operating System Fundamentals
* CPU Scheduling
* Memory Management
* Fragmentation Analysis
* Resource Allocation
* Performance Evaluation

---

## Future Roadmap

### Phase 1

* Memory Statistics
* Fragmentation Metrics

### Phase 2

* I/O Waiting Simulation
* Process State Transitions

### Phase 3

* Deadlock Detection
* Resource Allocation Graph

### Phase 4

* Streamlit Dashboard
* Interactive Visualizations
* Real-Time Simulation

---

## Author

Arda Alan

Computer Engineering Student

Düzce University
