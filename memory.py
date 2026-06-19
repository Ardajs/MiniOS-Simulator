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