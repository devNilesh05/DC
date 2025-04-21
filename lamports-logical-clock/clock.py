import time

class LamportClock:
    def __init__(self, process_id):
        self.process_id = process_id
        self.timestamp = 0

    def send_message(self):
        # Simulate sending a message with a delay
        time.sleep(2)  # 2 seconds delay
        self.timestamp += 1
        print(f"Process {self.process_id} sends a message with timestamp {self.timestamp}")
        return self.timestamp

    def receive_message(self, timestamp_received):
        # Simulate receiving a message with a delay
        time.sleep(2)  # 2 seconds delay
        self.timestamp = max(self.timestamp, timestamp_received) + 1
        print(f"Process {self.process_id} receives a message with timestamp {timestamp_received}. Updated timestamp: {self.timestamp}")

# Simulating multiple processes communicating
if __name__ == "__main__":
    # Create processes
    process1 = LamportClock(1)
    process2 = LamportClock(2)
    process3 = LamportClock(3)

    # Process 1 sends a message
    timestamp1 = process1.send_message()

    # Process 2 receives the message from Process 1
    process2.receive_message(timestamp1)

    # Process 2 sends a message
    timestamp2 = process2.send_message()

    # Process 3 receives the message from Process 2
    process3.receive_message(timestamp2)

    # Process 1 receives the message from Process 2
    process1.receive_message(timestamp2)

    # Process 3 sends a message
    timestamp3 = process3.send_message()

    # Process 1 receives the message from Process 3
    process1.receive_message(timestamp3)

    # Process 2 receives the message from Process 3
    process2.receive_message(timestamp3)


