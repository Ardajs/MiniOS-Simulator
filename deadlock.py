class Resource:
    def __init__(self, resource_id):
        self.resource_id = resource_id
        self.allocated_to = None

    def __str__(self):
        if self.allocated_to:
            return f"{self.resource_id} -> {self.allocated_to}"
        return f"{self.resource_id} -> FREE"
    
class DeadlockManager:
    def __init__(self):
        self.resources = {}
        self.allocations = {}
        self.requests = {}
    
    def add_resource(self, resource_id):
        self.resources[resource_id] = Resource(resource_id)


    def allocate_resource(self, pid, resource_id):

        resource = self.resources[resource_id]

        if resource.allocated_to is None:

            resource.allocated_to = pid

            if pid not in self.allocations:
                self.allocations[pid] = []

            self.allocations[pid].append(resource_id)

            print(f"{resource_id} allocated to {pid}")

            return True

        print(f"{resource_id} already allocated")

        return False
    
    def request_resource(self, pid, resource_id):

        if pid not in self.requests:
            self.requests[pid] = []

        self.requests[pid].append(resource_id)

        print(f"{pid} requests {resource_id}")

    def display_state(self):

        print("\nResources")

        for resource in self.resources.values():
            print(resource)

        print("\nAllocations")

        for pid, resources in self.allocations.items():
            print(pid, "->", resources)

        print("\nRequests")

        for pid, resources in self.requests.items():
            print(pid, "->", resources)


    def build_resource_allocation_graph(self):
        graph = {}

        for pid, resource_list in self.allocations.items():
            if pid not in graph:
                graph[pid] = []

            for resource_id in resource_list:
                if resource_id not in graph:
                    graph[resource_id] = []

                graph[resource_id].append(pid)

        for pid, resource_list in self.requests.items():
            if pid not in graph:
                graph[pid] = []

            for resource_id in resource_list:
                if resource_id not in graph:
                    graph[resource_id] = []

                graph[pid].append(resource_id)

        return graph
    
    def display_graph(self):
        graph = self.build_resource_allocation_graph()

        print("\nResource Allocation Graph")

        for node, edges in graph.items():
            print(node, "->", edges)

    def detect_cycle(self):
        graph = self.build_resource_allocation_graph()

        visited = set()
        recursion_stack = set()
        path = []

        def dfs(node):
            visited.add(node)
            recursion_stack.add(node)
            path.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    result = dfs(neighbor)
                    if result:
                        return result

                elif neighbor in recursion_stack:
                    cycle_start_index = path.index(neighbor)
                    cycle = path[cycle_start_index:] + [neighbor]
                    return cycle

            recursion_stack.remove(node)
            path.pop()
            return None

        for node in graph:
            if node not in visited:
                result = dfs(node)
                if result:
                    return result

        return None


    def detect_deadlock(self):
        cycle = self.detect_cycle()

        if cycle:
            print("\nDEADLOCK DETECTED")
            print("Deadlock Cycle:")
            print(" -> ".join(cycle))
            return True

        print("\nNO DEADLOCK")
        return False
    

    def release_resources(self, pid):
        if pid not in self.allocations:
            print(f"{pid} has no allocated resources.")
            return

        for resource_id in self.allocations[pid]:
            self.resources[resource_id].allocated_to = None
            print(f"{resource_id} released from {pid}")

        del self.allocations[pid]

    def terminate_process(self, pid):
        print(f"\nTerminating {pid} to resolve deadlock...")

        self.release_resources(pid)

        if pid in self.requests:
            del self.requests[pid]

        for request_pid in list(self.requests.keys()):
            self.requests[request_pid] = [
                resource_id
                for resource_id in self.requests[request_pid]
                if resource_id in self.resources
            ]

        print(f"{pid} terminated.")

    def recover_from_deadlock(self):
        cycle = self.detect_cycle()

        if not cycle:
            print("\nNo deadlock to recover from.")
            return False

        print("\nDeadlock Recovery Started")
        print("Cycle:", " -> ".join(cycle))

        victim_process = None

        for node in cycle:
            if node.startswith("P"):
                victim_process = node
                break

        if victim_process is None:
            print("No process found to terminate.")
            return False

        self.terminate_process(victim_process)

        print("\nChecking system after recovery...")
        self.detect_deadlock()

        return True


