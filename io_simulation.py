from process import Process


def simulate_io(process):
    print("\nStarting I/O Simulation")
    print("=" * 40)

    current_time = 0

    process.set_state("RUNNING")

    print(f"Time {current_time}: {process.pid} RUNNING")

    while current_time < process.burst_time:

        current_time += 1

        if (
            process.io_time is not None
            and current_time == process.io_time
            and not process.io_completed
        ):

            process.set_state("WAITING")

            print(
                f"Time {current_time}: "
                f"{process.pid} WAITING "
                f"({process.io_duration}s)"
            )

            current_time += process.io_duration

            process.io_completed = True

            process.set_state("RUNNING")

            print(
                f"Time {current_time}: "
                f"{process.pid} RUNNING"
            )

    process.set_state("TERMINATED")

    print(
        f"Time {current_time}: "
        f"{process.pid} TERMINATED"
    )


def simulate_multi_process_io(processes):
    print("\nMULTI PROCESS I/O SIMULATION")
    print("=" * 50)

    current_time = 0
    completed = 0
    n = len(processes)

    ready_queue = []
    waiting_list = []
    gantt_chart = []

    cpu_busy_time = 0

    for process in processes:
        process.io_waiting_time = 0
        process.completion_time = 0

    while completed < n:

        for process in processes:
            if process.arrival_time <= current_time and process.state == "NEW":
                process.set_state("READY")
                ready_queue.append(process)
                print(f"Time {current_time}: {process.pid} READY")

        for process in waiting_list[:]:
            if current_time >= process.io_finish_time:
                process.io_waiting_time += process.io_duration
                process.set_state("READY")
                ready_queue.append(process)
                waiting_list.remove(process)
                print(f"Time {current_time}: {process.pid} I/O completed → READY")

        if not ready_queue:
            print(f"Time {current_time}: CPU IDLE")
            current_time += 1
            continue

        process = ready_queue.pop(0)
        process.set_state("RUNNING")

        start_time = current_time
        print(f"Time {current_time}: {process.pid} RUNNING")

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

            print(
                f"Time {current_time}: {process.pid} WAITING "
                f"until Time {process.io_finish_time}"
            )

        elif process.remaining_time == 0:
            process.set_state("TERMINATED")
            process.completion_time = current_time
            completed += 1
            print(f"Time {current_time}: {process.pid} TERMINATED")

        else:
            process.set_state("READY")
            ready_queue.append(process)

    print("\nGantt Chart:")
    for item in gantt_chart:
        print(f"{item['pid']} : {item['start']} -> {item['finish']}")

    print("\nI/O Simulation Metrics:")
    print(
        f"{'PID':<10}"
        f"{'Completion':<15}"
        f"{'Turnaround':<15}"
        f"{'Waiting':<15}"
        f"{'I/O Wait':<15}"
    )

    print("-" * 70)

    total_turnaround_time = 0
    total_waiting_time = 0
    total_io_waiting_time = 0

    for process in processes:
        turnaround_time = process.completion_time - process.arrival_time
        waiting_time = turnaround_time - process.burst_time - process.io_waiting_time

        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
        total_io_waiting_time += process.io_waiting_time

        print(
            f"{process.pid:<10}"
            f"{process.completion_time:<15}"
            f"{turnaround_time:<15}"
            f"{waiting_time:<15}"
            f"{process.io_waiting_time:<15}"
        )

    avg_turnaround_time = total_turnaround_time / n
    avg_waiting_time = total_waiting_time / n
    avg_io_waiting_time = total_io_waiting_time / n
    cpu_utilization = (cpu_busy_time / current_time) * 100

    print("\nAverage Turnaround Time:", avg_turnaround_time)
    print("Average Waiting Time:", avg_waiting_time)
    print("Average I/O Waiting Time:", avg_io_waiting_time)
    print(f"CPU Utilization: {cpu_utilization:.2f}%")