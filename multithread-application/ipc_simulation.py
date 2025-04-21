from multiprocessing import Process, Queue
import threading
import time

def chat_process_A(send_queue, recv_queue):
    def send_messages():
        while True:
            msg = input("[Process A] You: ")
            send_queue.put(msg)
            if msg.lower() == "exit":
                break

    def receive_messages():
        while True:
            msg = recv_queue.get()
            print(f"[Process A] Received: {msg}")
            if msg.lower() == "exit":
                break

    threading.Thread(target=send_messages).start()
    threading.Thread(target=receive_messages).start()

def chat_process_B(send_queue, recv_queue):
    def send_messages():
        responses = [
            "Hi A!",
            "I'm Process B.",
            "Nice to talk to you.",
            "exit"
        ]
        for msg in responses:
            time.sleep(2)
            send_queue.put(msg)
            print(f"[Process B] Sent: {msg}")
            if msg.lower() == "exit":
                break

    def receive_messages():
        while True:
            msg = recv_queue.get()
            print(f"[Process B] Received: {msg}")
            if msg.lower() == "exit":
                break

    threading.Thread(target=send_messages).start()
    threading.Thread(target=receive_messages).start()

if __name__ == "__main__":
    queue_A_to_B = Queue()
    queue_B_to_A = Queue()

    p1 = Process(target=chat_process_A, args=(queue_A_to_B, queue_B_to_A))
    p2 = Process(target=chat_process_B, args=(queue_B_to_A, queue_A_to_B))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("✅ Bidirectional chat simulation complete.")

