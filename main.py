from scheduler_test import run_scheduler_tests
from memory_test import (
    test_first_fit,
    test_best_fit,
    test_worst_fit,
    test_memory_comparison,
)


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


if __name__ == "__main__":
    main()