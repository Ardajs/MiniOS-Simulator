from deadlock import DeadlockManager


def test_deadlock_scenario():
    print("\n" + "=" * 50)
    print("DEADLOCK SCENARIO TEST")
    print("=" * 50)

    manager = DeadlockManager()

    manager.add_resource("R1")
    manager.add_resource("R2")

    manager.allocate_resource("P1", "R1")
    manager.allocate_resource("P2", "R2")

    manager.request_resource("P1", "R2")
    manager.request_resource("P2", "R1")

    manager.display_state()
    manager.display_graph()
    manager.detect_deadlock()

    manager.recover_from_deadlock()
    manager.display_state()
    manager.display_graph()


def test_no_deadlock_scenario():
    print("\n" + "=" * 50)
    print("NO DEADLOCK SCENARIO TEST")
    print("=" * 50)

    manager = DeadlockManager()

    manager.add_resource("R1")
    manager.add_resource("R2")
    manager.add_resource("R3")

    manager.allocate_resource("P1", "R1")
    manager.allocate_resource("P2", "R2")

    manager.request_resource("P1", "R3")

    manager.display_state()
    manager.display_graph()
    manager.detect_deadlock()


if __name__ == "__main__":
    test_deadlock_scenario()
    test_no_deadlock_scenario()