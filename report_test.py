from system_report import SystemReport

report = SystemReport()

report.set_cpu_results(
    {
        "Best Algorithm": "SJF",
        "Average Waiting Time": 4.25,
        "CPU Utilization": 100
    }
)

report.set_memory_results(
    {
        "Used Memory": 700,
        "Free Memory": 324,
        "External Fragmentation": 24
    }
)

report.set_io_results(
    {
        "Average I/O Waiting": 2.0
    }
)

report.set_deadlock_results(
    {
        "Deadlock": False
    }
)

report.print_summary()