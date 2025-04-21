import socket
import threading

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen(1)
print("📡 Server is running. Waiting for client...")

conn, addr = server.accept()
print(f"✅ Client connected: {addr}")

def receive():
    while True:
        try:
            msg = conn.recv(1024).decode()
            if msg.lower() == "exit":
                print("❌ Client left the chat.")
                break
            print("Client:", msg)
        except:
            break

def send():
    while True:
        msg = input("You: ")
        conn.send(msg.encode())
        if msg.lower() == "exit":
            break

# Start threads
threading.Thread(target=receive).start()
threading.Thread(target=send).start()
