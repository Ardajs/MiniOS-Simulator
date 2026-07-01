import copy
import pandas as pd
import streamlit as st

from process import Process
from scheduler import fcfs, sjf, priority_scheduling, round_robin
from memory import MemoryManager
from deadlock import DeadlockManager
from components.ui import page_header


def render_system_report():
    page_header(
        "System Report",
        "Generate a summary report of CPU scheduling, memory management and deadlock status."
    )

    st.write(
        """
        This page provides a high-level summary of the MiniOS Simulator.
        It combines results from CPU scheduling, memory management and deadlock detection.
        """
    )

    if st.button("Generate System Report"):
        render_cpu_summary()
        st.divider()

        render_memory_summary()
        st.divider()

        render_deadlock_summary()


def render_cpu_summary():
    st.subheader("CPU Scheduling Summary")

    processes = [
        Process("P1", 0, 7, 3, 200),
        Process("P2", 2, 4, 1, 300),
        Process("P3", 4, 1, 4, 150),
        Process("P4", 5, 4, 2, 250),
    ]

    fcfs_result = fcfs(copy.deepcopy(processes))
    sjf_result = sjf(copy.deepcopy(processes))
    priority_result = priority_scheduling(copy.deepcopy(processes))
    rr_result = round_robin(copy.deepcopy(processes), quantum=2)

    cpu_data = [
        {
            "Algorithm": "FCFS",
            "Average Waiting Time": fcfs_result[1],
            "Average Turnaround Time": fcfs_result[2],
            "CPU Utilization (%)": fcfs_result[3],
        },
        {
            "Algorithm": "SJF",
            "Average Waiting Time": sjf_result[1],
            "Average Turnaround Time": sjf_result[2],
            "CPU Utilization (%)": sjf_result[3],
        },
        {
            "Algorithm": "Priority",
            "Average Waiting Time": priority_result[1],
            "Average Turnaround Time": priority_result[2],
            "CPU Utilization (%)": priority_result[3],
        },
        {
            "Algorithm": "Round Robin",
            "Average Waiting Time": rr_result[1],
            "Average Turnaround Time": rr_result[2],
            "CPU Utilization (%)": rr_result[3],
        },
    ]

    cpu_df = pd.DataFrame(cpu_data)
    st.dataframe(cpu_df, use_container_width=True)

    best_waiting = cpu_df.loc[cpu_df["Average Waiting Time"].idxmin()]
    best_turnaround = cpu_df.loc[cpu_df["Average Turnaround Time"].idxmin()]

    col1, col2, col3 = st.columns(3)

    col1.metric("Best Waiting Time", best_waiting["Algorithm"])
    col2.metric("Best Turnaround Time", best_turnaround["Algorithm"])
    col3.metric("Average CPU Utilization", f"{cpu_df['CPU Utilization (%)'].mean():.2f}%")


def render_memory_summary():
    st.subheader("Memory Management Summary")

    memory = MemoryManager(1024)

    processes = [
        Process("P1", 0, 5, 2, 200),
        Process("P2", 1, 3, 1, 300),
        Process("P3", 2, 4, 3, 150),
        Process("P4", 3, 6, 2, 250),
    ]

    for process in processes:
        memory.first_fit_allocate(process)

    memory.deallocate("P2")

    stats = memory.get_memory_statistics()
    external_fragmentation = memory.get_external_fragmentation()

    memory_data = [
        {"Metric": "Total Memory", "Value": f"{stats['total_memory']} MB"},
        {"Metric": "Used Memory", "Value": f"{stats['used_memory']} MB"},
        {"Metric": "Free Memory", "Value": f"{stats['free_memory']} MB"},
        {"Metric": "Free Blocks", "Value": stats["free_blocks"]},
        {"Metric": "Largest Free Block", "Value": f"{stats['largest_free_block']} MB"},
        {"Metric": "External Fragmentation", "Value": f"{external_fragmentation} MB"},
        {"Metric": "Memory Utilization", "Value": f"{stats['memory_utilization']:.2f}%"},
    ]

    st.dataframe(pd.DataFrame(memory_data), use_container_width=True)

    col1, col2, col3 = st.columns(3)

    col1.metric("Used Memory", f"{stats['used_memory']} MB")
    col2.metric("Free Memory", f"{stats['free_memory']} MB")
    col3.metric("External Fragmentation", f"{external_fragmentation} MB")


def render_deadlock_summary():
    st.subheader("Deadlock Detection Summary")

    manager = DeadlockManager()

    manager.add_resource("R1")
    manager.add_resource("R2")

    manager.allocate_resource("P1", "R1")
    manager.allocate_resource("P2", "R2")

    manager.request_resource("P1", "R2")
    manager.request_resource("P2", "R1")

    cycle = manager.detect_cycle()

    if cycle:
        st.error("Deadlock detected in sample scenario.")
        st.code(" -> ".join(cycle))

        manager.recover_from_deadlock()

        new_cycle = manager.detect_cycle()

        if new_cycle:
            st.warning("Deadlock still exists after recovery.")
            st.code(" -> ".join(new_cycle))
        else:
            st.success("Deadlock resolved after recovery.")

    else:
        st.success("No deadlock detected.")