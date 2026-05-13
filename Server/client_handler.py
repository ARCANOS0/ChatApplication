import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from common.config import HOST, PORT


def handle_client(client_socket, client_address, function, clients):

#!! next few lines connected to app.py file to handle the student ID before proceeding to the chat interface 
    student_id = client_socket.recv(1024).decode('utf-8')


    print(f"[NEW] {student_id} connected") # this was client_address, but now it changed and became the ID of the student

    try:
        while True:
            msg = client_socket.recv(1024).decode('utf-8')

            if not msg or msg.lower() == "exit":
                print(f"[DISCONNECTED] {client_address}")
                break

            print(f"[MESSAGE from {student_id}]: {msg}")

            broadcast_msg = f"[{client_address[1]}]: {msg}"
            function(broadcast_msg, client_socket)
            # response = f"[RESPONSE] {msg} received!"
            # client_socket.send(response.encode('utf-8'))

    except Exception as e:
        print(f"[ERROR] {e}")
        
    finally:
        if client_socket in clients:
            clients.remove(client_socket)
        client_socket.close()
        print(f"[DISCONNECTED] {client_address} left.")