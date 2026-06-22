class MemoryBlock:
    def __init__(self, start, size, pid=None):
        self.start = start
        self.size = size
        self.pid = pid

    def is_free(self):
        return self.pid is None

    def __str__(self):
        if self.is_free():
            return f"[FREE | Start: {self.start} | Size: {self.size} MB]"
        else:
            return f"[{self.pid} | Start: {self.start} | Size: {self.size} MB]"


class MemoryManager:
    def __init__(self, total_size):
        self.total_size = total_size
        self.blocks = [
            MemoryBlock(0, total_size)
        ]

    def display_memory(self):
        print("\nMemory Layout:")
        for block in self.blocks:
            print(block)

    def first_fit_allocate(self, process):
        for i, block in enumerate(self.blocks):
            if block.is_free() and block.size >= process.memory_required:

                allocated_block = MemoryBlock(
                    block.start,
                    process.memory_required,
                    process.pid
                )

                remaining_size = block.size - process.memory_required

                if remaining_size > 0:
                    free_block = MemoryBlock(
                        block.start + process.memory_required,
                        remaining_size
                    )

                    self.blocks[i] = allocated_block
                    self.blocks.insert(i + 1, free_block)
                else:
                    self.blocks[i] = allocated_block

                print(f"{process.pid} allocated successfully.")
                return True

        print(f"{process.pid} could not be allocated.")
        return False
    
    def best_fit_allocate(self, process):
        best_index = -1
        best_size = None

        for i, block in enumerate(self.blocks):
            if block.is_free() and block.size >= process.memory_required:
                if best_size is None or block.size < best_size:
                    best_size = block.size
                    best_index = i

        if best_index == -1:
            print(f"{process.pid} could not be allocated.")
            return False

        block = self.blocks[best_index]

        allocated_block = MemoryBlock(
            block.start,
            process.memory_required,
            process.pid
        )

        remaining_size = block.size - process.memory_required

        if remaining_size > 0:
            free_block = MemoryBlock(
                block.start + process.memory_required,
                remaining_size
            )

            self.blocks[best_index] = allocated_block
            self.blocks.insert(best_index + 1, free_block)
        else:
            self.blocks[best_index] = allocated_block

        print(f"{process.pid} allocated successfully using Best Fit.")
        return True
    
    def worst_fit_allocate(self, process):
        worst_index = -1
        worst_size = -1

        for i, block in enumerate(self.blocks):
            if block.is_free() and block.size >= process.memory_required:
                if block.size > worst_size:
                    worst_size = block.size
                    worst_index = i

        if worst_index == -1:
            print(f"{process.pid} could not be allocated.")
            return False

        block = self.blocks[worst_index]

        allocated_block = MemoryBlock(
            block.start,
            process.memory_required,
            process.pid
        )

        remaining_size = block.size - process.memory_required

        if remaining_size > 0:
            free_block = MemoryBlock(
                block.start + process.memory_required,
                remaining_size
            )

            self.blocks[worst_index] = allocated_block
            self.blocks.insert(worst_index + 1, free_block)
        else:
            self.blocks[worst_index] = allocated_block

        print(f"{process.pid} allocated successfully using Worst Fit.")
        return True
    
    

    def deallocate(self, pid):
        for block in self.blocks:
            if block.pid == pid:
                block.pid = None
                print(f"{pid} deallocated successfully.")

                self.merge_free_blocks()

                return True

        print(f"{pid} not found in memory.")
        return False

    def merge_free_blocks(self):
        i = 0

        while i < len(self.blocks) - 1:
            current_block = self.blocks[i]
            next_block = self.blocks[i + 1]

            if current_block.is_free() and next_block.is_free():
                current_block.size += next_block.size
                self.blocks.pop(i + 1)
            else:
                i += 1



    def get_memory_statistics(self):
        used_memory = 0
        free_memory = 0
        free_blocks = 0
        largest_free_block = 0

        for block in self.blocks:
            if block.is_free():
                free_memory += block.size
                free_blocks += 1

                if block.size > largest_free_block:
                    largest_free_block = block.size
            else:
                used_memory += block.size

        memory_utilization = (used_memory / self.total_size) * 100

        return {
            "total_memory": self.total_size,
            "used_memory": used_memory,
            "free_memory": free_memory,
            "free_blocks": free_blocks,
            "largest_free_block": largest_free_block,
            "memory_utilization": memory_utilization
        }
    
    def display_statistics(self):
        stats = self.get_memory_statistics()
        external_fragmentation = self.get_external_fragmentation()

        print("\nMemory Statistics:")
        print(f"Total Memory: {stats['total_memory']} MB")
        print(f"Used Memory: {stats['used_memory']} MB")
        print(f"Free Memory: {stats['free_memory']} MB")
        print(f"Free Blocks: {stats['free_blocks']}")
        print(f"Largest Free Block: {stats['largest_free_block']} MB")
        print(f"External Fragmentation: {external_fragmentation} MB")
        print(f"Memory Utilization: {stats['memory_utilization']:.2f}%")


    def get_external_fragmentation(self):
        stats = self.get_memory_statistics()

        free_memory = stats["free_memory"]
        largest_free_block = stats["largest_free_block"]

        if free_memory == 0:
            return 0

        external_fragmentation = free_memory - largest_free_block

        return external_fragmentation
    

    def display_memory_bar(self):
        print("\nMemory Bar:")

        bar = "|"

        for block in self.blocks:
            if block.is_free():
                label = f" FREE {block.size}MB "
            else:
                label = f" {block.pid} {block.size}MB "

            bar += label + "|"

        print(bar)