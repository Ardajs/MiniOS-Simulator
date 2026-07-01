import copy
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from process import Process
from scheduler import fcfs, sjf, priority_scheduling, round_robin
from components.ui import page_header


def render_cpu():
    page_header(
        "CPU Scheduling",
        "Compare CPU scheduling algorithms and visualize process execution with Gantt charts."
    )

    st.subheader("Process List")

    processes = [
        Process("P1", 0, 7, 3, 200),
        Process("P2", 2, 4, 1, 300),
        Process("P3", 4, 1, 4, 150),
        Process("P4", 5, 4, 2, 250),
    ]

    process_data = []

    for p in processes:
        process_data.append({
            "PID": p.pid,
            "Arrival Time": p.arrival_time,
            "Burst Time": p.burst_time,
            "Priority": p.priority,
            "Memory": p.memory_required,
            "State": p.state
        })

    st.dataframe(pd.DataFrame(process_data), use_container_width=True)

    st.subheader("Algorithm Selection")

    algorithm = st.selectbox(
        "Select scheduling algorithm",
        [
            "FCFS",
            "SJF",
            "Priority",
            "Round Robin"
        ]
    )

    quantum = 2

    if algorithm == "Round Robin":
        quantum = st.number_input(
            "Time Quantum",
            min_value=1,
            value=2
        )

    if st.button("Run CPU Scheduling Simulation"):
        simulation_processes = copy.deepcopy(processes)

        if algorithm == "FCFS":
            result = fcfs(simulation_processes)

        elif algorithm == "SJF":
            result = sjf(simulation_processes)

        elif algorithm == "Priority":
            result = priority_scheduling(simulation_processes)

        elif algorithm == "Round Robin":
            result = round_robin(simulation_processes, quantum)

        gantt_chart, avg_waiting_time, avg_turnaround_time, cpu_utilization = result

        st.success("Simulation completed.")

        st.subheader("Gantt Chart Table")

        gantt_df = pd.DataFrame(gantt_chart)
        st.dataframe(gantt_df, use_container_width=True)

        st.subheader("Gantt Chart Visualization")

        fig = go.Figure()

        for item in gantt_chart:
            fig.add_trace(
                go.Bar(
                    x=[item["finish"] - item["start"]],
                    y=["CPU"],
                    base=[item["start"]],
                    orientation="h",
                    name=item["pid"],
                    text=item["pid"],
                    textposition="inside"
                )
            )

        fig.update_layout(
            title=f"{algorithm} Gantt Chart",
            xaxis_title="Time",
            yaxis_title="",
            barmode="stack",
            showlegend=True,
            height=300
        )

        fig.update_xaxes(
            tickmode="linear",
            dtick=1
        )

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Performance Metrics")

        col1, col2, col3 = st.columns(3)

        col1.metric("Average Waiting Time", f"{avg_waiting_time:.2f}")
        col2.metric("Average Turnaround Time", f"{avg_turnaround_time:.2f}")
        col3.metric("CPU Utilization", f"{cpu_utilization:.2f}%")

    st.divider()

    st.subheader("Compare All Scheduling Algorithms")

    if st.button("Compare All Algorithms"):
        fcfs_result = fcfs(copy.deepcopy(processes))
        sjf_result = sjf(copy.deepcopy(processes))
        priority_result = priority_scheduling(copy.deepcopy(processes))
        rr_result = round_robin(copy.deepcopy(processes), quantum=2)

        comparison_data = [
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

        comparison_df = pd.DataFrame(comparison_data)

        st.dataframe(comparison_df, use_container_width=True)

        best_waiting = comparison_df.loc[
            comparison_df["Average Waiting Time"].idxmin()
        ]

        best_turnaround = comparison_df.loc[
            comparison_df["Average Turnaround Time"].idxmin()
        ]

        col1, col2 = st.columns(2)

        col1.success(
            f"Best Waiting Time: {best_waiting['Algorithm']} "
            f"({best_waiting['Average Waiting Time']:.2f})"
        )

        col2.success(
            f"Best Turnaround Time: {best_turnaround['Algorithm']} "
            f"({best_turnaround['Average Turnaround Time']:.2f})"
        )