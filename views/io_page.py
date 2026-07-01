import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from process import Process
from components.ui import page_header


def render_io():
    page_header(
        "I/O Waiting",
        "Simulate processes entering WAITING state because of I/O operations."
    )

    st.write(
        """
        This module demonstrates how processes leave the CPU during I/O operations
        and return to the READY queue after the I/O operation is completed.
        """
    )

    st.subheader("Process List")

    processes = [
        Process(
            "P1",
            arrival_time=0,
            burst_time=6,
            priority=1,
            memory_required=200,
            io_time=2,
            io_duration=3
        ),
        Process(
            "P2",
            arrival_time=1,
            burst_time=4,
            priority=2,
            memory_required=150
        ),
        Process(
            "P3",
            arrival_time=2,
            burst_time=3,
            priority=3,
            memory_required=100
        )
    ]

    process_data = []

    for p in processes:
        process_data.append({
            "PID": p.pid,
            "Arrival Time": p.arrival_time,
            "Burst Time": p.burst_time,
            "Priority": p.priority,
            "Memory": p.memory_required,
            "I/O Time": p.io_time,
            "I/O Duration": p.io_duration,
            "State": p.state
        })

    st.dataframe(pd.DataFrame(process_data), use_container_width=True)

    if st.button("Run I/O Simulation"):
        run_io_simulation(processes)


def run_io_simulation(processes):
    current_time = 0
    completed = 0
    n = len(processes)

    ready_queue = []
    waiting_list = []
    gantt_chart = []

    cpu_busy_time = 0
    event_log = []

    for process in processes:
        process.io_waiting_time = 0
        process.completion_time = 0

    while completed < n:
        for process in processes:
            if process.arrival_time <= current_time and process.state == "NEW":
                process.set_state("READY")
                ready_queue.append(process)
                event_log.append({
                    "Time": current_time,
                    "Process": process.pid,
                    "Event": "READY"
                })

        for process in waiting_list[:]:
            if current_time >= process.io_finish_time:
                process.io_waiting_time += process.io_duration
                process.set_state("READY")
                ready_queue.append(process)
                waiting_list.remove(process)
                event_log.append({
                    "Time": current_time,
                    "Process": process.pid,
                    "Event": "I/O Completed -> READY"
                })

        if not ready_queue:
            event_log.append({
                "Time": current_time,
                "Process": "-",
                "Event": "CPU IDLE"
            })
            current_time += 1
            continue

        process = ready_queue.pop(0)
        process.set_state("RUNNING")

        start_time = current_time

        event_log.append({
            "Time": current_time,
            "Process": process.pid,
            "Event": "RUNNING"
        })

        current_time += 1
        cpu_busy_time += 1
        process.remaining_time -= 1

        gantt_chart.append({
            "pid": process.pid,
            "start": start_time,
            "finish": current_time
        })

        executed_time = process.burst_time - process.remaining_time

        if (
            process.io_time is not None
            and executed_time == process.io_time
            and not process.io_completed
        ):
            process.set_state("WAITING")
            process.io_completed = True
            process.io_finish_time = current_time + process.io_duration
            waiting_list.append(process)

            event_log.append({
                "Time": current_time,
                "Process": process.pid,
                "Event": f"WAITING until Time {process.io_finish_time}"
            })

        elif process.remaining_time == 0:
            process.set_state("TERMINATED")
            process.completion_time = current_time
            completed += 1

            event_log.append({
                "Time": current_time,
                "Process": process.pid,
                "Event": "TERMINATED"
            })

        else:
            process.set_state("READY")
            ready_queue.append(process)

    st.success("I/O simulation completed.")

    render_event_log(event_log)
    render_io_gantt_chart(gantt_chart)
    render_io_metrics(processes, n, cpu_busy_time, current_time)


def render_event_log(event_log):
    st.subheader("Event Log")
    st.dataframe(pd.DataFrame(event_log), use_container_width=True)


def render_io_gantt_chart(gantt_chart):
    st.subheader("I/O Gantt Chart Table")

    gantt_df = pd.DataFrame(gantt_chart)
    st.dataframe(gantt_df, use_container_width=True)

    st.subheader("I/O Gantt Chart Visualization")

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
        title="I/O Waiting Gantt Chart",
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


def render_io_metrics(processes, n, cpu_busy_time, current_time):
    st.subheader("I/O Metrics")

    metrics_data = []

    total_turnaround_time = 0
    total_waiting_time = 0
    total_io_waiting_time = 0

    for process in processes:
        turnaround_time = process.completion_time - process.arrival_time
        waiting_time = (
            turnaround_time
            - process.burst_time
            - process.io_waiting_time
        )

        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
        total_io_waiting_time += process.io_waiting_time

        metrics_data.append({
            "PID": process.pid,
            "Completion Time": process.completion_time,
            "Turnaround Time": turnaround_time,
            "Waiting Time": waiting_time,
            "I/O Waiting Time": process.io_waiting_time
        })

    metrics_df = pd.DataFrame(metrics_data)

    st.dataframe(metrics_df, use_container_width=True)

    avg_turnaround_time = total_turnaround_time / n
    avg_waiting_time = total_waiting_time / n
    avg_io_waiting_time = total_io_waiting_time / n
    cpu_utilization = (cpu_busy_time / current_time) * 100

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Avg Turnaround", f"{avg_turnaround_time:.2f}")
    col2.metric("Avg Waiting", f"{avg_waiting_time:.2f}")
    col3.metric("Avg I/O Waiting", f"{avg_io_waiting_time:.2f}")
    col4.metric("CPU Utilization", f"{cpu_utilization:.2f}%")