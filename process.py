class Process:
    def __init__(self, pid, arrival_time, burst_time, priority, memory_required):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.memory_required = memory_required
        self.state = "NEW"

    def set_state(self, new_state):
        self.state = new_state

    def __str__(self):
        return (
            f"PID: {self.pid}, "
            f"Arrival: {self.arrival_time}, "
            f"Burst: {self.burst_time}, "
            f"Priority: {self.priority}, "
            f"Memory: {self.memory_required} MB, "
            f"State: {self.state}"
        )