import streamlit as st


def page_header(title, description):
    st.markdown(
        f"""
        <div class="main-title">{title}</div>
        <div class="subtitle">{description}</div>
        """,
        unsafe_allow_html=True
    )


def section_card(title, description):
    st.markdown(
        f"""
        <div class="section-card">
            <div class="module-title">{title}</div>
            <div class="module-description">{description}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def info_card(title, items):
    list_items = "".join([f"<li>{item}</li>" for item in items])

    st.markdown(
        f"""
        <div class="section-card">
            <div class="module-title">{title}</div>
            <ul class="feature-list">
                {list_items}
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

def pcb_card(process):
    st.markdown(
        f"""
        <div class="section-card">
            <div class="module-title">Process Control Block - {process.pid}</div>
            <div class="module-description">
                <b>PID:</b> {process.pid}<br>
                <b>State:</b> {process.state}<br>
                <b>Arrival Time:</b> {process.arrival_time}<br>
                <b>Burst Time:</b> {process.burst_time}<br>
                <b>Remaining Time:</b> {process.remaining_time}<br>
                <b>Priority:</b> {process.priority}<br>
                <b>Memory Required:</b> {process.memory_required} MB<br>
                <b>I/O Time:</b> {process.io_time}<br>
                <b>I/O Duration:</b> {process.io_duration}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )