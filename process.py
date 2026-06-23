class Process:
    def __init__(
        self,
        pid,
        arrival_time,
        burst_time,
        priority,
        memory_required,
        io_time=None,
        io_duration=0
    ):
        self.pid = pid

        self.arrival_time = arrival_time
        self.burst_time = burst_time

        self.remaining_time = burst_time

        self.priority = priority
        self.memory_required = memory_required

        self.state = "NEW"

        self.io_time = io_time
        self.io_duration = io_duration

        self.io_completed = False

    def set_state(self, new_state):
        self.state = new_state