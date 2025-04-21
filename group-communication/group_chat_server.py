import socket
import threading

clients = []

def handle_client(client_socket, address):
    print(f"[+] New connection from {address}")
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg.lower() == 'exit':
                print(f"[-] {address} left the chat.")
                clients.remove(client_socket)
                client_socket.close()
                break
            broadcast(msg, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, sender_socket):
    """Broadcast message to all clients except the sender."""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5000))
    server.listen(5)
    print("[*] Server started on port 5000...")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    main()
