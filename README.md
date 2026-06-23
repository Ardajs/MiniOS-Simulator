# MiniOS Simulator

A simplified Operating System Simulator developed in Python to demonstrate fundamental operating system concepts such as process management, CPU scheduling, memory management, and resource allocation.

---

# Project Overview

Modern operating systems such as Windows and Linux manage processes, memory, and hardware resources simultaneously.

MiniOS Simulator provides a simplified educational model of these mechanisms by implementing:

* Process Management
* CPU Scheduling
* Memory Management
* I/O Waiting Simulation
* Performance Metrics
* Fragmentation Analysis

The goal of the project is to help students understand operating system concepts through practical simulation and visualization.

---

# Features

## Process Management

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
WAITING
TERMINATED
```

---

# CPU Scheduling Module

Implemented scheduling algorithms:

### FCFS (First Come First Serve)

Processes are executed according to arrival order.

### SJF (Shortest Job First)

The shortest available process is selected first.

### Priority Scheduling

Processes are selected according to priority values.

### Round Robin

Time-sharing scheduling using configurable time quantum.

---

## CPU Metrics

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
```

---

## Scheduling Comparison

Implemented comparison between:

* FCFS
* SJF
* Priority Scheduling
* Round Robin

---

# Memory Management Module

The simulator supports dynamic memory allocation strategies.

---

## Memory Allocation Algorithms

### First Fit

Allocates memory in the first available block large enough for the process.

### Best Fit

Allocates memory in the smallest suitable free block.

### Worst Fit

Allocates memory in the largest available free block.

---

## Memory Operations

### Memory Allocation

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

### Memory Deallocation

Example:

```text
[P1][P2][P3][FREE]
```

After removing P2:

```text
[P1][FREE][P3][FREE]
```

---

### Free Block Merging

Adjacent free blocks are automatically merged.

Example:

```text
[FREE 300 MB][FREE 374 MB]
```

↓

```text
[FREE 674 MB]
```

---

## Memory Statistics

The simulator provides:

* Total Memory
* Used Memory
* Free Memory
* Number of Free Blocks
* Largest Free Block
* Memory Utilization

Example:

```text
Total Memory: 1024 MB
Used Memory: 600 MB
Free Memory: 424 MB
Free Blocks: 2
Largest Free Block: 300 MB
Memory Utilization: 58.59%
```

---

## Fragmentation Analysis

External fragmentation is calculated as:

```text
External Fragmentation =
Total Free Memory - Largest Free Block
```

Example:

```text
Free Memory = 424 MB
Largest Free Block = 300 MB

External Fragmentation = 124 MB
```

---

## Memory Visualization

Example:

```text
| P1 200MB | FREE 300MB | P3 150MB | P4 250MB |
```

---

# I/O Waiting Module

The simulator supports process waiting states caused by I/O operations.

---

## Single Process I/O Simulation

Example:

```text
RUNNING
↓
WAITING
↓
RUNNING
↓
TERMINATED
```

---

## Multi Process I/O Simulation

When a process enters WAITING state:

```text
P1 WAITING
CPU switches to P2
CPU switches to P3
P1 becomes READY again
```

---

## I/O Metrics

The simulator calculates:

* Completion Time
* Turnaround Time
* Waiting Time
* I/O Waiting Time
* CPU Utilization

---

# Testing Infrastructure

Dedicated test files are included:

```text
scheduler_test.py
memory_test.py
io_test.py
```

---

# Project Structure

```text
MiniOS-Simulator
│
├── main.py
├── process.py
├── scheduler.py
├── scheduler_test.py
├── memory.py
├── memory_test.py
├── io_simulation.py
├── io_test.py
├── README.md
└── requirements.txt
```

---

# Technologies Used

* Python 3
* Object-Oriented Programming (OOP)

Future Technologies:

* Streamlit
* Plotly
* Matplotlib

---

# Development Progress

## Completed

### Process Management

* Process Creation
* Process States

### CPU Scheduling

* FCFS
* SJF
* Priority Scheduling
* Round Robin
* Gantt Chart
* Performance Metrics
* Scheduling Comparison

### Memory Management

* First Fit
* Best Fit
* Worst Fit
* Memory Deallocation
* Free Block Merging
* Memory Statistics
* External Fragmentation Analysis
* Memory Comparison
* Memory Visualization

### I/O Waiting

* Single Process I/O
* Multi Process I/O
* WAITING State
* I/O Metrics

### Testing

* CPU Scheduling Tests
* Memory Management Tests
* I/O Simulation Tests

---

## In Progress

* Deadlock Detection

---

## Planned

* Resource Allocation Graph
* Deadlock Visualization
* Streamlit Dashboard
* Interactive Charts
* Real-Time Simulation
* Process Visualization

---

# Educational Objectives

This project helps students understand:

* Operating System Fundamentals
* CPU Scheduling Algorithms
* Memory Allocation Strategies
* Fragmentation Analysis
* Process State Transitions
* I/O Management
* System Performance Evaluation

---

# Author

Arda Alan

Computer Engineering Student

Düzce University
