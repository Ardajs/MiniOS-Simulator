def fcfs(processes):
    processes.sort(key=lambda p: p.arrival_time)

    current_time = 0
    gantt_chart = []

    total_waiting_time = 0
    total_turnaround_time = 0
    total_burst_time = 0

    for process in processes:
        if current_time < process.arrival_time:
            gantt_chart.append({
                "pid": "IDLE",
                "start": current_time,
                "finish": process.arrival_time
            })
            current_time = process.arrival_time

        process.set_state("RUNNING")

        start_time = current_time
        finish_time = current_time + process.burst_time

        waiting_time = start_time - process.arrival_time
        turnaround_time = finish_time - process.arrival_time

        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        total_burst_time += process.burst_time

        gantt_chart.append({
            "pid": process.pid,
            "start": start_time,
            "finish": finish_time
        })

        current_time = finish_time
        process.set_state("TERMINATED")

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    total_time = gantt_chart[-1]["finish"]
    cpu_utilization = (total_burst_time / total_time) * 100

    return gantt_chart, avg_waiting_time, avg_turnaround_time, cpu_utilization



def sjf(processes):
    processes.sort(key=lambda p: p.arrival_time)

    current_time = 0
    completed = 0
    n = len(processes)

    gantt_chart = []

    total_waiting_time = 0
    total_turnaround_time = 0
    total_burst_time = sum(p.burst_time for p in processes)

    while completed < n:
        ready_queue = []

        for process in processes:
            if process.arrival_time <= current_time and process.state != "TERMINATED":
                ready_queue.append(process)

        if not ready_queue:
            next_process = min(
                [p for p in processes if p.state != "TERMINATED"],
                key=lambda p: p.arrival_time
            )

            gantt_chart.append({
                "pid": "IDLE",
                "start": current_time,
                "finish": next_process.arrival_time
            })

            current_time = next_process.arrival_time
            continue

        ready_queue.sort(key=lambda p: p.burst_time)

        process = ready_queue[0]

        process.set_state("RUNNING")

        start_time = current_time
        finish_time = current_time + process.burst_time

        waiting_time = start_time - process.arrival_time
        turnaround_time = finish_time - process.arrival_time

        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time

        gantt_chart.append({
            "pid": process.pid,
            "start": start_time,
            "finish": finish_time
        })

        current_time = finish_time
        process.set_state("TERMINATED")
        completed += 1

    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    total_time = gantt_chart[-1]["finish"]
    cpu_utilization = (total_burst_time / total_time) * 100

    return gantt_chart, avg_waiting_time, avg_turnaround_time, cpu_utilization


def priority_scheduling(processes):
    processes.sort(key=lambda p: p.arrival_time)

    current_time = 0
    completed = 0
    n = len(processes)

    gantt_chart = []

    total_waiting_time = 0
    total_turnaround_time = 0
    total_burst_time = sum(p.burst_time for p in processes)

    while completed < n:
        ready_queue = []

        for process in processes:
            if process.arrival_time <= current_time and process.state != "TERMINATED":
                ready_queue.append(process)

        if not ready_queue:
            next_process = min(
                [p for p in processes if p.state != "TERMINATED"],
                key=lambda p: p.arrival_time
            )

            gantt_chart.append({
                "pid": "IDLE",
                "start": current_time,
                "finish": next_process.arrival_time
            })

            current_time = next_process.arrival_time
            continue

        ready_queue.sort(key=lambda p: p.priority)

        process = ready_queue[0]

        process.set_state("RUNNING")

        start_time = current_time
        finish_time = current_time + process.burst_time

        waiting_time = start_time - process.arrival_time
        turnaround_time = finish_time - process.arrival_time

        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time

        gantt_chart.append({
            "pid": process.pid,
            "start": start_time,
            "finish": finish_time
        })

        current_time = finish_time
        process.set_state("TERMINATED")
        completed += 1

    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    total_time = gantt_chart[-1]["finish"]
    cpu_utilization = (total_burst_time / total_time) * 100

    return gantt_chart, avg_waiting_time, avg_turnaround_time, cpu_utilization



def round_robin(processes, quantum):
    processes.sort(key=lambda p: p.arrival_time)

    current_time = 0
    completed = 0
    n = len(processes)

    ready_queue = []
    gantt_chart = []

    total_burst_time = sum(p.burst_time for p in processes)
    finish_times = {}

    while completed < n:
        for process in processes:
            if (
                process.arrival_time <= current_time
                and process.state == "NEW"
            ):
                process.set_state("READY")
                ready_queue.append(process)

        if not ready_queue:
            next_process = min(
                [p for p in processes if p.state != "TERMINATED"],
                key=lambda p: p.arrival_time
            )

            gantt_chart.append({
                "pid": "IDLE",
                "start": current_time,
                "finish": next_process.arrival_time
            })

            current_time = next_process.arrival_time
            continue

        process = ready_queue.pop(0)
        process.set_state("RUNNING")

        start_time = current_time

        if process.remaining_time > quantum:
            run_time = quantum
        else:
            run_time = process.remaining_time

        current_time += run_time
        process.remaining_time -= run_time

        finish_time = current_time

        gantt_chart.append({
            "pid": process.pid,
            "start": start_time,
            "finish": finish_time
        })

        for new_process in processes:
            if (
                new_process.arrival_time <= current_time
                and new_process.state == "NEW"
            ):
                new_process.set_state("READY")
                ready_queue.append(new_process)

        if process.remaining_time > 0:
            process.set_state("READY")
            ready_queue.append(process)
        else:
            process.set_state("TERMINATED")
            finish_times[process.pid] = current_time
            completed += 1

    total_waiting_time = 0
    total_turnaround_time = 0

    for process in processes:
        turnaround_time = finish_times[process.pid] - process.arrival_time
        waiting_time = turnaround_time - process.burst_time

        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time

    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    total_time = gantt_chart[-1]["finish"]
    cpu_utilization = (total_burst_time / total_time) * 100

    return gantt_chart, avg_waiting_time, avg_turnaround_time, cpu_utilization