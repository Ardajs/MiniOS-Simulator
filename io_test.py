from process import Process
from io_simulation import simulate_io, simulate_multi_process_io


def test_single_process_io():
    print("\n" + "=" * 50)
    print("SINGLE PROCESS I/O TEST")
    print("=" * 50)

    p1 = Process(
        "P1",
        arrival_time=0,
        burst_time=10,
        priority=1,
        memory_required=200,
        io_time=4,
        io_duration=3
    )

    simulate_io(p1)


def test_multi_process_io():
    print("\n" + "=" * 50)
    print("MULTI PROCESS I/O TEST")
    print("=" * 50)

    processes = [
        Process(
            "P1",
            arrival_time=0,
            burst_time=6,
            priority=1,
            memory_required=200,
            io_time=2,
            io_duration=3
        ),
        Process(
            "P2",
            arrival_time=1,
            burst_time=4,
            priority=2,
            memory_required=150
        ),
        Process(
            "P3",
            arrival_time=2,
            burst_time=3,
            priority=3,
            memory_required=100
        )
    ]

    simulate_multi_process_io(processes)


if __name__ == "__main__":
    test_single_process_io()
    test_multi_process_io()