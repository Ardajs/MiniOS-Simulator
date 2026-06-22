from process import Process
from memory import MemoryManager


def test_first_fit():
    print("\n" + "=" * 50)
    print("FIRST FIT TEST")
    print("=" * 50)

    memory = MemoryManager(1024)

    processes = [
        Process("P1", 0, 5, 2, 200),
        Process("P2", 1, 3, 1, 300),
        Process("P3", 2, 4, 3, 150),
        Process("P4", 3, 6, 2, 250),
    ]

    for process in processes:
        memory.first_fit_allocate(process)

    memory.display_memory()
    memory.display_memory_bar()
    memory.display_statistics()


def test_best_fit():
    print("\n" + "=" * 50)
    print("BEST FIT TEST")
    print("=" * 50)

    memory = MemoryManager(1024)

    p1 = Process("P1", 0, 5, 2, 200)
    p2 = Process("P2", 1, 3, 1, 300)
    p3 = Process("P3", 2, 4, 3, 150)
    p4 = Process("P4", 3, 6, 2, 250)
    p5 = Process("P5", 4, 2, 1, 100)

    memory.first_fit_allocate(p1)
    memory.first_fit_allocate(p2)
    memory.first_fit_allocate(p3)
    memory.first_fit_allocate(p4)

    memory.deallocate("P2")

    print("\nBefore Best Fit Allocation:")
    memory.display_memory_bar()

    memory.best_fit_allocate(p5)

    print("\nAfter Best Fit Allocation:")
    memory.display_memory()
    memory.display_memory_bar()
    memory.display_statistics()


def test_worst_fit():
    print("\n" + "=" * 50)
    print("WORST FIT TEST")
    print("=" * 50)

    memory = MemoryManager(1024)

    p1 = Process("P1", 0, 5, 2, 200)
    p2 = Process("P2", 1, 3, 1, 300)
    p3 = Process("P3", 2, 4, 3, 150)
    p4 = Process("P4", 3, 6, 2, 250)
    p5 = Process("P5", 4, 2, 1, 100)

    memory.first_fit_allocate(p1)
    memory.first_fit_allocate(p2)
    memory.first_fit_allocate(p3)
    memory.first_fit_allocate(p4)

    memory.deallocate("P2")

    print("\nBefore Worst Fit Allocation:")
    memory.display_memory_bar()

    memory.worst_fit_allocate(p5)

    print("\nAfter Worst Fit Allocation:")
    memory.display_memory()
    memory.display_memory_bar()
    memory.display_statistics()


def test_memory_comparison():
    print("\n" + "=" * 70)
    print("MEMORY ALLOCATION COMPARISON")
    print("=" * 70)

    results = []

    algorithms = [
        ("First Fit", lambda memory, process: memory.first_fit_allocate(process)),
        ("Best Fit", lambda memory, process: memory.best_fit_allocate(process)),
        ("Worst Fit", lambda memory, process: memory.worst_fit_allocate(process)),
    ]

    for algorithm_name, allocation_method in algorithms:
        memory = MemoryManager(1024)

        p1 = Process("P1", 0, 5, 2, 200)
        p2 = Process("P2", 1, 3, 1, 300)
        p3 = Process("P3", 2, 4, 3, 150)
        p4 = Process("P4", 3, 6, 2, 250)
        p5 = Process("P5", 4, 2, 1, 100)

        memory.first_fit_allocate(p1)
        memory.first_fit_allocate(p2)
        memory.first_fit_allocate(p3)
        memory.first_fit_allocate(p4)

        memory.deallocate("P2")

        allocation_method(memory, p5)

        stats = memory.get_memory_statistics()
        external_fragmentation = memory.get_external_fragmentation()

        results.append({
            "algorithm": algorithm_name,
            "used_memory": stats["used_memory"],
            "free_memory": stats["free_memory"],
            "free_blocks": stats["free_blocks"],
            "largest_free_block": stats["largest_free_block"],
            "external_fragmentation": external_fragmentation,
        })

    print(
        f"{'Algorithm':<15}"
        f"{'Used':<10}"
        f"{'Free':<10}"
        f"{'Free Blocks':<15}"
        f"{'Largest Free':<15}"
        f"{'Ext. Frag.':<15}"
    )

    print("-" * 70)

    for row in results:
        print(
            f"{row['algorithm']:<15}"
            f"{row['used_memory']:<10}"
            f"{row['free_memory']:<10}"
            f"{row['free_blocks']:<15}"
            f"{row['largest_free_block']:<15}"
            f"{row['external_fragmentation']:<15}"
        )


if __name__ == "__main__":
    test_first_fit()
    test_best_fit()
    test_worst_fit()
    test_memory_comparison()