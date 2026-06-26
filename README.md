# MiniOS Simulator

A Python-based Operating System Simulator developed to demonstrate core operating system concepts including Process Management, CPU Scheduling, Memory Management, I/O Waiting, Deadlock Detection, and System Performance Analysis.

---

# Project Overview

Modern operating systems such as Windows and Linux manage processes, memory, and hardware resources simultaneously.

MiniOS Simulator provides an educational and interactive environment for understanding how operating systems work internally by simulating:

* Process Management
* CPU Scheduling
* Memory Management
* I/O Waiting Operations
* Deadlock Detection and Recovery
* System Performance Metrics

The project is designed for Computer Engineering students who want to learn operating system concepts through practical implementation.

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

Supported Process States:

```text
NEW
READY
RUNNING
WAITING
TERMINATED
```

---

# CPU Scheduling Module

The simulator implements classical CPU Scheduling algorithms.

## FCFS (First Come First Serve)

Processes are executed according to arrival order.

## SJF (Shortest Job First)

The process with the shortest burst time is selected first.

## Priority Scheduling

Processes are selected according to their priority value.

## Round Robin Scheduling

Time-sharing scheduling using configurable time quantum.

---

## CPU Performance Metrics

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

Comparison between:

* FCFS
* SJF
* Priority Scheduling
* Round Robin

based on:

* Waiting Time
* Turnaround Time
* CPU Utilization

---

# Memory Management Module

The simulator supports dynamic memory allocation techniques commonly used in operating systems.

---

## Memory Allocation Algorithms

### First Fit

Allocates memory in the first free block large enough to satisfy the request.

### Best Fit

Allocates memory in the smallest suitable free block.

### Worst Fit

Allocates memory in the largest available free block.

---

## Memory Allocation Example

Initial Memory:

```text
[FREE 1024 MB]
```

After allocating P1 (200 MB):

```text
[P1 200 MB][FREE 824 MB]
```

---

## Memory Deallocation

Example:

Before:

```text
[P1][P2][P3][FREE]
```

After removing P2:

```text
[P1][FREE][P3][FREE]
```

---

## Free Block Merging

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

## External Fragmentation Analysis

External Fragmentation is calculated as:

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

## Memory Comparison

Comparison between:

* First Fit
* Best Fit
* Worst Fit

using:

* Used Memory
* Free Memory
* Number of Free Blocks
* Largest Free Block
* External Fragmentation

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
P1 resumes execution
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

# Deadlock Detection Module

The simulator supports resource allocation and deadlock analysis using a Resource Allocation Graph.

---

## Resource Management

Resources can be:

```text
Allocated
Requested
Released
```

by processes.

---

## Resource Allocation Graph

Example:

```text
P1 -> R2
R2 -> P2
P2 -> R1
R1 -> P1
```

---

## Deadlock Detection

The simulator automatically detects cycles in the Resource Allocation Graph.

Example Output:

```text
DEADLOCK DETECTED
```

---

## Deadlock Cycle Visualization

The simulator displays the exact cycle causing the deadlock.

Example:

```text
Deadlock Cycle:

P1 -> R2 -> P2 -> R1 -> P1
```

---

## Deadlock Recovery

Recovery is performed by:

1. Selecting a victim process
2. Terminating the process
3. Releasing its resources
4. Rechecking the system

Example:

```text
Deadlock Recovery Started

Terminating P1...

R1 released from P1

NO DEADLOCK
```

---

# Testing Infrastructure

The project includes dedicated test modules.

```text
scheduler_test.py
memory_test.py
io_test.py
deadlock_test.py
```

---


# Streamlit Dashboard

The project now includes an interactive Streamlit-based dashboard that allows users to simulate and visualize operating system components through a graphical interface.

## Dashboard Features

### Home

- Project overview
- Module navigation

### CPU Scheduling Dashboard

- Process table
- Algorithm selection
- Round Robin quantum configuration
- Interactive Gantt Chart
- Gantt Chart visualization
- Performance metrics
- Algorithm comparison table
- Best algorithm recommendation

### Memory Management Dashboard

- Total memory configuration
- Allocation algorithm selection
- Memory layout visualization
- Memory statistics
- External fragmentation analysis
- Interactive fragmentation scenario
- Memory allocation visualization

### Planned Dashboard Modules

- I/O Waiting Dashboard
- Deadlock Dashboard
- System Summary Dashboard

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
├── deadlock.py
├── deadlock_test.py
├── README.md
└── requirements.txt
```

---

# Technologies Used

* Python 3
* Object-Oriented Programming (OOP)

Planned:

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
* Gantt Chart Generation
* Performance Metrics
* Scheduling Comparison

### Memory Management

* First Fit
* Best Fit
* Worst Fit
* Memory Allocation
* Memory Deallocation
* Free Block Merging
* Memory Statistics
* External Fragmentation Analysis
* Memory Visualization
* Memory Comparison

### I/O Waiting

* Single Process I/O Simulation
* Multi Process I/O Simulation
* WAITING State
* I/O Metrics

### Deadlock Detection

* Resource Allocation
* Resource Requests
* Resource Allocation Graph
* Cycle Detection
* Deadlock Detection
* Deadlock Cycle Visualization
* Deadlock Recovery

### Testing

* CPU Scheduling Tests
* Memory Management Tests
* I/O Simulation Tests
* Deadlock Tests

---

## Planned Features

* Streamlit Dashboard
* Interactive Charts
* Real-Time Visualization
* Process Timeline Visualization
* Resource Monitoring Dashboard

---

# Educational Objectives

This project helps students understand:

* Operating System Fundamentals
* CPU Scheduling Algorithms
* Memory Allocation Strategies
* Fragmentation Analysis
* Process State Transitions
* I/O Management
* Deadlock Detection and Recovery
* System Performance Evaluation

---

# Author

Arda Alan

Computer Engineering Student

Düzce University
