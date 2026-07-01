import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from deadlock import DeadlockManager
from components.ui import page_header



def render_deadlock():
    page_header(
        "Deadlock Detection",
        "Analyze resource allocation graphs, detect deadlocks and simulate recovery."
    )

    st.write(
        """
        This module demonstrates deadlock detection using a Resource Allocation Graph.
        A deadlock occurs when processes wait for each other in a circular chain.
        """
    )

    scenario = st.selectbox(
        "Select Scenario",
        [
            "Deadlock Scenario",
            "No Deadlock Scenario"
        ]
    )

    manager = create_deadlock_manager(scenario)

    render_resources(manager)
    render_allocations(manager)
    render_requests(manager)
    render_resource_allocation_graph(manager)
    render_deadlock_actions(manager)


def create_deadlock_manager(scenario):
    manager = DeadlockManager()

    if scenario == "Deadlock Scenario":
        manager.add_resource("R1")
        manager.add_resource("R2")

        manager.allocate_resource("P1", "R1")
        manager.allocate_resource("P2", "R2")

        manager.request_resource("P1", "R2")
        manager.request_resource("P2", "R1")

    elif scenario == "No Deadlock Scenario":
        manager.add_resource("R1")
        manager.add_resource("R2")
        manager.add_resource("R3")

        manager.allocate_resource("P1", "R1")
        manager.allocate_resource("P2", "R2")

        manager.request_resource("P1", "R3")

    return manager


def render_resources(manager):
    st.subheader("Resources")

    resource_data = []

    for resource_id, resource in manager.resources.items():
        resource_data.append({
            "Resource": resource_id,
            "Allocated To": resource.allocated_to if resource.allocated_to else "FREE"
        })

    st.dataframe(pd.DataFrame(resource_data), use_container_width=True)


def render_allocations(manager):
    st.subheader("Allocations")

    allocation_data = []

    for pid, resources in manager.allocations.items():
        allocation_data.append({
            "Process": pid,
            "Allocated Resources": ", ".join(resources)
        })

    st.dataframe(pd.DataFrame(allocation_data), use_container_width=True)


def render_requests(manager):
    st.subheader("Requests")

    request_data = []

    for pid, resources in manager.requests.items():
        request_data.append({
            "Process": pid,
            "Requested Resources": ", ".join(resources)
        })

    st.dataframe(pd.DataFrame(request_data), use_container_width=True)


def render_resource_allocation_graph(manager):
    graph = manager.build_resource_allocation_graph()

    st.subheader("Resource Allocation Graph")

    graph_data = []

    for node, edges in graph.items():
        graph_data.append({
            "Node": node,
            "Edges": ", ".join(edges) if edges else "-"
        })

    st.dataframe(pd.DataFrame(graph_data), use_container_width=True)

    st.subheader("Graph Visualization")

    fig = go.Figure()

    y_position = 0

    for node, edges in graph.items():
        fig.add_trace(
            go.Scatter(
                x=[0],
                y=[y_position],
                mode="markers+text",
                text=[node],
                textposition="middle right",
                marker=dict(size=20),
                name=node
            )
        )

        for edge in edges:
            fig.add_trace(
                go.Scatter(
                    x=[0, 1],
                    y=[y_position, y_position],
                    mode="lines+text",
                    text=["", edge],
                    textposition="middle right",
                    showlegend=False
                )
            )

        y_position += 1

    fig.update_layout(
        title="Resource Allocation Graph",
        xaxis=dict(showticklabels=False),
        yaxis=dict(showticklabels=False),
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)


def render_deadlock_actions(manager):
    st.subheader("Deadlock Actions")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Detect Deadlock"):
            cycle = manager.detect_cycle()

            if cycle:
                st.error("DEADLOCK DETECTED")

                st.subheader("Deadlock Cycle")
                st.code(" -> ".join(cycle))

            else:
                st.success("NO DEADLOCK")

    with col2:
        if st.button("Recover From Deadlock"):
            cycle = manager.detect_cycle()

            if cycle:
                st.warning("Deadlock detected. Recovery started.")

                victim_process = None

                for node in cycle:
                    if node.startswith("P"):
                        victim_process = node
                        break

                if victim_process:
                    manager.terminate_process(victim_process)

                    st.success(
                        f"{victim_process} terminated and resources released."
                    )

                    new_cycle = manager.detect_cycle()

                    if new_cycle:
                        st.error("Deadlock still exists.")
                        st.code(" -> ".join(new_cycle))
                    else:
                        st.success("Deadlock resolved successfully.")
                        render_recovered_resources(manager)

            else:
                st.info("No deadlock found. Recovery is not required.")


def render_recovered_resources(manager):
    st.subheader("System State After Recovery")

    recovered_resource_data = []

    for resource_id, resource in manager.resources.items():
        recovered_resource_data.append({
            "Resource": resource_id,
            "Allocated To": resource.allocated_to if resource.allocated_to else "FREE"
        })

    st.dataframe(
        pd.DataFrame(recovered_resource_data),
        use_container_width=True
    )