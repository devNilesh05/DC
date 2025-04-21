import random
import time
import threading


class Process:
    def __init__(self, process_id, total_processes):
        self.process_id = process_id
        self.total_processes = total_processes
        self.is_leader = False
        self.state = "active"  # can be 'active' or 'inactive'
        self.messages_received = 0

    def send_election(self):
        print(f"Process {self.process_id} starts an election.")
        self.messages_received = 0
        
        # Send election messages to all processes with higher IDs
        for pid in range(self.process_id + 1, self.total_processes + 1):
            print(f"Process {self.process_id} sends an election message to Process {pid}.")
            time.sleep(1)
            # Simulate process receiving election messages
            self.receive_election(pid)
        
        if self.messages_received == 0:
            self.declare_leader()

    def receive_election(self, sender_id):
        """Simulate receiving election message from a higher ID process"""
        if sender_id > self.process_id:
            print(f"Process {self.process_id} received an election message from Process {sender_id}.")
            self.messages_received += 1
            self.send_ok(sender_id)

    def send_ok(self, sender_id):
        """Simulate sending an 'OK' message to a lower ID process"""
        print(f"Process {self.process_id} sends an OK message to Process {sender_id}.")
        time.sleep(1)

    def declare_leader(self):
        """Declare itself as the leader since no higher ID process responded"""
        self.is_leader = True
        print(f"Process {self.process_id} declares itself as the leader.")

    def start_election(self):
        """Start the election process"""
        if self.state == "active":
            self.send_election()


# Simulate the process of an election
def election_simulation(total_processes):
    processes = [Process(i, total_processes) for i in range(1, total_processes + 1)]

    # Simulate a leader failure
    failed_process_id = random.randint(1, total_processes)
    print(f"\nProcess {failed_process_id} has failed and needs to be replaced.\n")

    # Start the election from a process that detects the failure
    for process in processes:
        if process.process_id != failed_process_id:
            election_thread = threading.Thread(target=process.start_election)
            election_thread.start()
            election_thread.join()

    # Find the leader
    for process in processes:
        if process.is_leader:
            print(f"\nProcess {process.process_id} is the new leader.\n")
            break


# Example usage
if __name__ == "__main__":
    total_processes = 5  # Total number of processes in the system
    election_simulation(total_processes)
