import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import copy

from process import Process
from scheduler import fcfs, sjf, priority_scheduling, round_robin
from memory import MemoryManager


st.set_page_config(
    page_title="MiniOS Simulator",
    page_icon="💻",
    layout="wide"
)


st.title("💻 MiniOS Simulator")

st.write(
    """
    This project simulates core operating system concepts such as
    CPU Scheduling, Memory Management, I/O Waiting and Deadlock Detection.
    """
)


st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "Home",
        "CPU Scheduling",
        "Memory Management",
        "I/O Waiting",
        "Deadlock Detection"
    ]
)


if page == "Home":
    st.header("Operating System Simulator")

    st.success("Welcome to MiniOS Simulator!")

    st.markdown(
        """
        ### Modules

        - CPU Scheduling
        - Memory Management
        - I/O Waiting Simulation
        - Deadlock Detection and Recovery
        """
    )


elif page == "CPU Scheduling":
    st.header("CPU Scheduling Module")

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

    st.subheader("Select Scheduling Algorithm")

    algorithm = st.selectbox(
        "Algorithm",
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

        st.success("Simulation completed!")

        st.subheader("Gantt Chart")

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

        metric_col1, metric_col2, metric_col3 = st.columns(3)

        metric_col1.metric(
            "Average Waiting Time",
            f"{avg_waiting_time:.2f}"
        )

        metric_col2.metric(
            "Average Turnaround Time",
            f"{avg_turnaround_time:.2f}"
        )

        metric_col3.metric(
            "CPU Utilization",
            f"{cpu_utilization:.2f}%"
        )

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

elif page == "Memory Management":
    st.header("Memory Management Module")

    st.subheader("Memory Configuration")

    total_memory = st.number_input(
        "Total Memory (MB)",
        min_value=128,
        value=1024,
        step=128
    )

    algorithm = st.selectbox(
        "Memory Allocation Algorithm",
        [
            "First Fit",
            "Best Fit",
            "Worst Fit"
        ]
    )

    st.subheader("Process List")

    processes = [
        Process("P1", 0, 5, 2, 200),
        Process("P2", 1, 3, 1, 300),
        Process("P3", 2, 4, 3, 150),
        Process("P4", 3, 6, 2, 250),
    ]

    process_data = []

    for p in processes:
        process_data.append({
            "PID": p.pid,
            "Memory Required (MB)": p.memory_required
        })

    st.dataframe(pd.DataFrame(process_data), use_container_width=True)

    if st.button("Run Memory Allocation"):
        memory = MemoryManager(total_memory)

        for process in processes:
            if algorithm == "First Fit":
                memory.first_fit_allocate(process)

            elif algorithm == "Best Fit":
                memory.best_fit_allocate(process)

            elif algorithm == "Worst Fit":
                memory.worst_fit_allocate(process)

        st.success("Memory allocation completed!")

        memory_layout = []

        for block in memory.blocks:
            memory_layout.append({
                "PID": "FREE" if block.is_free() else block.pid,
                "Start": block.start,
                "Size": block.size,
                "Status": "Free" if block.is_free() else "Allocated"
            })

        layout_df = pd.DataFrame(memory_layout)

        st.subheader("Memory Layout")
        st.dataframe(layout_df, use_container_width=True)

        st.subheader("Memory Statistics")

        stats = memory.get_memory_statistics()
        external_fragmentation = memory.get_external_fragmentation()

        col1, col2, col3 = st.columns(3)

        col1.metric("Used Memory", f"{stats['used_memory']} MB")
        col2.metric("Free Memory", f"{stats['free_memory']} MB")
        col3.metric("Memory Utilization", f"{stats['memory_utilization']:.2f}%")

        col4, col5, col6 = st.columns(3)

        col4.metric("Free Blocks", stats["free_blocks"])
        col5.metric("Largest Free Block", f"{stats['largest_free_block']} MB")
        col6.metric("External Fragmentation", f"{external_fragmentation} MB")

        st.subheader("Memory Visualization")

        fig = go.Figure()

        for block in memory.blocks:
            label = "FREE" if block.is_free() else block.pid

            fig.add_trace(
                go.Bar(
                    x=[block.size],
                    y=["Memory"],
                    base=[block.start],
                    orientation="h",
                    name=label,
                    text=f"{label} {block.size}MB",
                    textposition="inside"
                )
            )

        fig.update_layout(
            title=f"{algorithm} Memory Layout",
            xaxis_title="Memory Address (MB)",
            yaxis_title="",
            barmode="stack",
            showlegend=True,
            height=300
        )

        fig.update_xaxes(
            range=[0, total_memory],
            tickmode="linear",
            dtick=128
        )

        st.plotly_chart(fig, use_container_width=True)


    st.divider()

    st.subheader("Fragmentation Scenario")

    st.write(
        """
        This scenario demonstrates external fragmentation.
        
        Initial memory allocations:
        - P1 = 200 MB
        - P2 = 300 MB
        - P3 = 150 MB
        - P4 = 250 MB

        Then P2 is deallocated, creating a free block in the middle of memory.
        """
    )

    fragmentation_algorithm = st.selectbox(
        "Fragmentation Test Algorithm",
        [
            "First Fit",
            "Best Fit",
            "Worst Fit"
        ],
        key="fragmentation_algorithm"
    )

    new_process_memory = st.number_input(
        "New Process Memory Requirement (MB)",
        min_value=50,
        value=350,
        step=50
    )

    if st.button("Run Fragmentation Scenario"):
        memory = MemoryManager(1024)

        p1 = Process("P1", 0, 5, 2, 200)
        p2 = Process("P2", 1, 3, 1, 300)
        p3 = Process("P3", 2, 4, 3, 150)
        p4 = Process("P4", 3, 6, 2, 250)
        p5 = Process("P5", 4, 2, 1, new_process_memory)

        memory.first_fit_allocate(p1)
        memory.first_fit_allocate(p2)
        memory.first_fit_allocate(p3)
        memory.first_fit_allocate(p4)

        memory.deallocate("P2")

        st.subheader("Before Allocating P5")

        before_layout = []

        for block in memory.blocks:
            before_layout.append({
                "PID": "FREE" if block.is_free() else block.pid,
                "Start": block.start,
                "Size": block.size,
                "Status": "Free" if block.is_free() else "Allocated"
            })

        st.dataframe(pd.DataFrame(before_layout), use_container_width=True)

        before_stats = memory.get_memory_statistics()
        before_external_fragmentation = memory.get_external_fragmentation()

        col1, col2, col3 = st.columns(3)

        col1.metric("Free Memory", f"{before_stats['free_memory']} MB")
        col2.metric("Largest Free Block", f"{before_stats['largest_free_block']} MB")
        col3.metric("External Fragmentation", f"{before_external_fragmentation} MB")

        if fragmentation_algorithm == "First Fit":
            allocated = memory.first_fit_allocate(p5)

        elif fragmentation_algorithm == "Best Fit":
            allocated = memory.best_fit_allocate(p5)

        elif fragmentation_algorithm == "Worst Fit":
            allocated = memory.worst_fit_allocate(p5)

        if allocated:
            st.success("P5 allocated successfully.")
        else:
            st.error(
                "P5 could not be allocated. "
                "Total free memory may be enough, but no single free block is large enough."
            )

        st.subheader("After Allocating P5")

        after_layout = []

        for block in memory.blocks:
            after_layout.append({
                "PID": "FREE" if block.is_free() else block.pid,
                "Start": block.start,
                "Size": block.size,
                "Status": "Free" if block.is_free() else "Allocated"
            })

        st.dataframe(pd.DataFrame(after_layout), use_container_width=True)

        after_stats = memory.get_memory_statistics()
        after_external_fragmentation = memory.get_external_fragmentation()

        col4, col5, col6 = st.columns(3)

        col4.metric("Free Memory", f"{after_stats['free_memory']} MB")
        col5.metric("Largest Free Block", f"{after_stats['largest_free_block']} MB")
        col6.metric("External Fragmentation", f"{after_external_fragmentation} MB")

        st.subheader("Fragmentation Memory Visualization")

        fig = go.Figure()

        for block in memory.blocks:
            label = "FREE" if block.is_free() else block.pid

            fig.add_trace(
                go.Bar(
                    x=[block.size],
                    y=["Memory"],
                    base=[block.start],
                    orientation="h",
                    name=label,
                    text=f"{label} {block.size}MB",
                    textposition="inside"
                )
            )

        fig.update_layout(
            title=f"{fragmentation_algorithm} Fragmentation Scenario",
            xaxis_title="Memory Address (MB)",
            yaxis_title="",
            barmode="stack",
            showlegend=True,
            height=300
        )

        fig.update_xaxes(
            range=[0, 1024],
            tickmode="linear",
            dtick=128
        )

        st.plotly_chart(fig, use_container_width=True)


elif page == "I/O Waiting":
    st.header("I/O Waiting Module")

    st.info("I/O Waiting dashboard will be added here.")


elif page == "Deadlock Detection":
    st.header("Deadlock Detection Module")

    st.info("Deadlock Detection dashboard will be added here.")