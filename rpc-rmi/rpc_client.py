import socket
import threading

# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))
print("✅ Connected to the server. Type messages (type 'exit' to quit).")

def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg.lower() == "exit":
                print("❌ Server left the chat.")
                break
            print("Server:", msg)
        except:
            break

def send():
    while True:
        msg = input("You: ")
        client.send(msg.encode())
        if msg.lower() == "exit":
            break

# Start threads
threading.Thread(target=receive).start()
threading.Thread(target=send).start()

