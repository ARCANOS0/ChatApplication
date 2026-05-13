import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# server/client_handler.py

def handle_client(client_socket, client_address):
    print(f"[NEW] {client_address} connected")

    try:
        while True:
            msg = client_socket.recv(1024).decode('utf-8')

            if not msg or msg.lower() == "exit":
                print(f"[DISCONNECTED] {client_address}")
                break

            print(f"[MESSAGE] {msg}")
            response = f"[RESPONSE] {msg} received!"
            client_socket.send(response.encode('utf-8'))

    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        client_socket.close()