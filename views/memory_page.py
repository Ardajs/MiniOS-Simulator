import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from process import Process
from memory import MemoryManager
from components.ui import page_header


def render_memory():
    page_header(
        "Memory Management",
        "Simulate memory allocation algorithms and analyze fragmentation."
    )

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

        st.success("Memory allocation completed.")

        render_memory_result(memory, total_memory, algorithm)

    st.divider()

    render_fragmentation_scenario()


def render_memory_result(memory, total_memory, algorithm):
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


def render_fragmentation_scenario():
    st.subheader("Fragmentation Scenario")

    st.write(
        """
        This scenario demonstrates external fragmentation. 
        P1, P2, P3 and P4 are allocated first. Then P2 is deallocated,
        creating a free block in the middle of memory.
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
        render_memory_result(memory, 1024, "Before Fragmentation Allocation")

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
                "P5 could not be allocated. Total free memory may be enough, "
                "but no single free block is large enough."
            )

        st.subheader("After Allocating P5")
        render_memory_result(memory, 1024, f"{fragmentation_algorithm} Fragmentation Scenario")