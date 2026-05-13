# client/client.py
import sys
import os
import socket as soc

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from common.config import HOST, PORT

def start_client():
    client = soc.socket(soc.AF_INET, soc.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        print(f"[CONNECTED] Joined server on port {PORT}")
        print("Type 'exit' to disconnect.")

        while True:
            msg = input("You: ")
            client.send(msg.encode('utf-8'))

            if msg.lower() == "exit":
                break

            response = client.recv(1024).decode('utf-8')
            print(f"{response}")

    except Exception as e:
        print(f"[CONNECTION ERROR] {e}")
    finally:
        print("Closing connection...")
        client.close()

if __name__ == "__main__":
    start_client()