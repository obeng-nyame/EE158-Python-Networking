"""
EE 158: Introduction to Python and Computer Network
Task: Environment Verification & Basic Data Parsing Blueprint
"""


def verify_system_pipeline(data_metrics):
    print("[SYSTEM INFO] Initializing local data verification engine...")

    for hardware_id, status in data_metrics.items():
        if status == "Active":
            print(
                f"[STATUS] Node {hardware_id}: Functional. Pipeline compiled successfully.")
        else:
            print(f"[WARNING] Node {hardware_id}: Action required.")


if __name__ == "__main__":
    # Simulating initial network node statuses
    test_nodes = {
        "0x01": "Active",
        "0x02": "Active",
        "0x03": "Pending"
    }
    verify_system_pipeline(test_nodes)
