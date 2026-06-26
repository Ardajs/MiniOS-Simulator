class SystemReport:

    def __init__(self):
        self.cpu_results = None
        self.memory_results = None
        self.io_results = None
        self.deadlock_results = None

    def set_cpu_results(self, results):
        self.cpu_results = results

    def set_memory_results(self, results):
        self.memory_results = results

    def set_io_results(self, results):
        self.io_results = results

    def set_deadlock_results(self, results):
        self.deadlock_results = results

    def print_summary(self):

        print("\n")
        print("=" * 70)
        print("MINIOS SIMULATION REPORT")
        print("=" * 70)

        if self.cpu_results:
            print("\nCPU Scheduling")
            print(self.cpu_results)

        if self.memory_results:
            print("\nMemory Management")
            print(self.memory_results)

        if self.io_results:
            print("\nI/O Simulation")
            print(self.io_results)

        if self.deadlock_results:
            print("\nDeadlock Detection")
            print(self.deadlock_results)