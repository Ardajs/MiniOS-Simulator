from scheduler_test import run_scheduler_tests
from memory_test import (
    test_first_fit,
    test_best_fit,
    test_worst_fit,
    test_memory_comparison,
)
from io_test import test_single_process_io, test_multi_process_io
from deadlock_test import test_deadlock_scenario, test_no_deadlock_scenario


def main():
    print("\nMINIOS SIMULATOR")
    print("=" * 50)

    print("\n1. CPU Scheduling Module")
    run_scheduler_tests()

    print("\n2. Memory Management Module")
    test_first_fit()
    test_best_fit()
    test_worst_fit()
    test_memory_comparison()

    print("\n3. I/O Waiting Module")
    test_single_process_io()
    test_multi_process_io()

    print("\n4. Deadlock Detection Module")
    test_deadlock_scenario()
    test_no_deadlock_scenario()


if __name__ == "__main__":
    main()