# server/server.py
import sys
import os
import socket as soc
import threading

# Path setup to allow importing from 'common'
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from common.config import HOST, PORT
from client_handler import handle_client

def start_server():
    server = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
    
    # Allow restarting the server immediately without "Address already in use" error
    server.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR, 1)
    
    try:
        server.bind((HOST, PORT))
        server.listen()
        print(f"[LISTENING] Server is running on {HOST}:{PORT}")

        while True:
            # Accept new connection
            client_socket, client_address = server.accept()
            
            # Create a new thread for each client (Level 2 Requirement)
            thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            thread.start()
            
            # Show how many active connections there are
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

    except Exception as e:
        print(f"[CRITICAL ERROR] {e}")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()