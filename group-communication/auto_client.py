import socket
import threading

def receive_messages(sock):
    """Receive messages from the server and print them."""
    while True:
        try:
            message = sock.recv(1024).decode()
            print("\n" + message)
        except:
            print("Disconnected from server.")
            sock.close()
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5000))

    name = input("Enter your name: ")
    print("Type 'exit' to leave the chat.\n")

    # Start a thread to listen for messages from the server
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    while True:
        msg = input()
        if msg.lower() == 'exit':
            client.send('exit'.encode())
            break
        message = f"{name}: {msg}"
        client.send(message.encode())

    client.close()

if __name__ == "__main__":
    main()


