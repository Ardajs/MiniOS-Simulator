import streamlit as st
from components.ui import page_header, section_card, info_card


def render_home():
    page_header(
        "MiniOS Simulator",
        "Interactive operating system simulation platform for process scheduling, memory management, I/O operations and deadlock analysis."
    )

    section_card(
        "Project Overview",
        "MiniOS Simulator is an educational Python project that demonstrates how operating systems manage CPU, memory, process states, I/O waiting and resource deadlocks."
    )

    col1, col2 = st.columns(2)

    with col1:
        info_card(
            "CPU Scheduling",
            [
                "FCFS Scheduling",
                "SJF Scheduling",
                "Priority Scheduling",
                "Round Robin Scheduling",
                "Gantt Chart and performance metrics"
            ]
        )

        info_card(
            "I/O Waiting",
            [
                "Single process I/O simulation",
                "Multi process I/O simulation",
                "WAITING state transitions",
                "I/O waiting time metrics"
            ]
        )

    with col2:
        info_card(
            "Memory Management",
            [
                "First Fit allocation",
                "Best Fit allocation",
                "Worst Fit allocation",
                "Memory statistics",
                "External fragmentation analysis"
            ]
        )

        info_card(
            "Deadlock Detection",
            [
                "Resource allocation graph",
                "Cycle detection",
                "Deadlock cycle visualization",
                "Deadlock recovery"
            ]
        )