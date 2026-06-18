from process import Process
from scheduler import fcfs, sjf, priority_scheduling, round_robin
import copy


def print_results(algorithm_name, gantt_chart, avg_waiting_time, avg_turnaround_time, cpu_utilization):
    print("\n" + "=" * 40)
    print(algorithm_name)
    print("=" * 40)

    print("Gantt Chart:")
    for item in gantt_chart:
        print(f"{item['pid']} : {item['start']} -> {item['finish']}")

    print("\nAverage Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)
    print("CPU Utilization:", cpu_utilization, "%")


processes = [
    Process("P1", 0, 7, 3, 200),
    Process("P2", 2, 4, 1, 300),
    Process("P3", 4, 1, 4, 150),
    Process("P4", 5, 4, 2, 250)
]

fcfs_processes = copy.deepcopy(processes)
sjf_processes = copy.deepcopy(processes)
priority_processes = copy.deepcopy(processes)
rr_processes = copy.deepcopy(processes)

fcfs_result = fcfs(fcfs_processes)
sjf_result = sjf(sjf_processes)
priority_result = priority_scheduling(priority_processes)
rr_result = round_robin(rr_processes, quantum=2)

print_results("FCFS Scheduling", *fcfs_result)
print_results("SJF Scheduling", *sjf_result)
print_results("Priority Scheduling", *priority_result)
print_results("Round Robin Scheduling", *rr_result)



def print_comparison_table(results):
    print("\n")
    print("=" * 70)
    print("ALGORITHM COMPARISON")
    print("=" * 70)

    print(
        f"{'Algorithm':<15}"
        f"{'Waiting':<15}"
        f"{'Turnaround':<15}"
        f"{'CPU Util (%)':<15}"
    )

    print("-" * 70)

    for row in results:
        print(
            f"{row['algorithm']:<15}"
            f"{row['waiting']:<15.2f}"
            f"{row['turnaround']:<15.2f}"
            f"{row['cpu']:<15.2f}"
        )

comparison_results = [
    {
        "algorithm": "FCFS",
        "waiting": fcfs_result[1],
        "turnaround": fcfs_result[2],
        "cpu": fcfs_result[3]
    },
    {
        "algorithm": "SJF",
        "waiting": sjf_result[1],
        "turnaround": sjf_result[2],
        "cpu": sjf_result[3]
    },
    {
        "algorithm": "Priority",
        "waiting": priority_result[1],
        "turnaround": priority_result[2],
        "cpu": priority_result[3]
    },
    {
        "algorithm": "RR",
        "waiting": rr_result[1],
        "turnaround": rr_result[2],
        "cpu": rr_result[3]
    }
]
print_comparison_table(comparison_results)

best_waiting = min(
    comparison_results,
    key=lambda x: x["waiting"]
)

best_turnaround = min(
    comparison_results,
    key=lambda x: x["turnaround"]
)

print("\nBest Waiting Time:")
print(best_waiting["algorithm"])

print("\nBest Turnaround Time:")
print(best_turnaround["algorithm"])