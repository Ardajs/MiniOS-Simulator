#  Views

The `views` package contains all Streamlit pages used in the MiniOS Simulator. Each page represents a specific operating system module and provides an interactive interface for simulations, visualizations, and performance analysis.

---

##  Folder Structure

```
views/
├── home.py                  # Home dashboard
├── cpu.py                   # CPU Scheduling Simulation
├── memory_page.py           # Memory Management Simulation
├── io_page.py               # I/O Waiting Simulation
├── deadlock_page.py         # Deadlock Detection & Recovery
└── system_report_page.py    # Overall System Report
```

---

#  Modules

##  Home (`home.py`)

The home page introduces the simulator and provides a high-level overview of all operating system modules.

### Features

- Project introduction
- Module descriptions
- Interactive dashboard
- Navigation entry point

---

##  CPU Scheduling (`cpu.py`)

Provides an interactive interface for comparing CPU scheduling algorithms.

### Supported Algorithms

- FCFS
- SJF
- Priority Scheduling
- Round Robin

### Features

- Process table
- Algorithm selection
- Adjustable Time Quantum
- Gantt Chart visualization
- Performance metrics
- Algorithm comparison table

Displayed Metrics

- Average Waiting Time
- Average Turnaround Time
- CPU Utilization

---

##  Memory Management (`memory_page.py`)

Simulates dynamic memory allocation strategies.

### Supported Algorithms

- First Fit
- Best Fit
- Worst Fit

### Features

- Memory allocation simulation
- Memory layout visualization
- Memory statistics
- External fragmentation analysis
- Fragmentation scenario simulation

Displayed Metrics

- Used Memory
- Free Memory
- Memory Utilization
- Largest Free Block
- External Fragmentation

---

##  I/O Waiting (`io_page.py`)

Demonstrates how processes enter the WAITING state during I/O operations.

### Features

- Single and multiple process simulation
- Event log
- Process state transitions
- Gantt Chart
- I/O waiting metrics

Displayed Metrics

- Completion Time
- Waiting Time
- Turnaround Time
- I/O Waiting Time
- CPU Utilization

---

##  Deadlock Detection (`deadlock_page.py`)

Visualizes resource allocation and demonstrates deadlock detection and recovery.

### Features

- Resource Allocation Graph
- Resource allocation table
- Resource request table
- Deadlock detection
- Cycle visualization
- Deadlock recovery simulation

Supported Scenarios

- Deadlock Scenario
- No Deadlock Scenario

---

##  System Report (`system_report_page.py`)

Generates an overall summary of the operating system simulation.

### Includes

- CPU Scheduling Summary
- Memory Management Summary
- Deadlock Summary

Displayed Information

- Best scheduling algorithm
- Memory utilization
- External fragmentation
- Deadlock status
- Recovery results

---

#  Purpose

The Views package provides a modern, interactive, and educational interface that enables users to explore operating system concepts through real-time simulations and visual analytics.

Each page is designed to be independent, reusable, and easy to extend with new operating system modules.
