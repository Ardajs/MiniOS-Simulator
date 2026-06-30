import streamlit as st

from components.styles import load_styles

from views.home import render_home
from views.cpu import render_cpu
from views.memory_page import render_memory
from views.io_page import render_io
from views.deadlock_page import render_deadlock
from views.system_report_page import render_system_report


st.set_page_config(
    page_title="MiniOS Simulator",
    layout="wide"
)

load_styles()

st.sidebar.markdown("## Navigation")

page = st.sidebar.radio(
    "Select module",
    [
        "Home",
        "CPU Scheduling",
        "Memory Management",
        "I/O Waiting",
        "Deadlock Detection",
        "System Report"
    ]
)

if page == "Home":
    render_home()

elif page == "CPU Scheduling":
    render_cpu()

elif page == "Memory Management":
    render_memory()

elif page == "I/O Waiting":
    render_io()

elif page == "Deadlock Detection":
    render_deadlock()

elif page == "System Report":
    render_system_report()