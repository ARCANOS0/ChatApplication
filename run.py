# run.py
import sys
import os
import threading
import time
from common.config import assign_port

# Ensure imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def launch_server(port):
    from Server.server import start_server
    start_server(port)

def launch_client(port, student_id):
    from app import ChatClient
    app = ChatClient(port, student_id)
    app.run()

if __name__ == "__main__":
    print("=== Chat Application Entry ===")
    student_id = input("Enter your Academic ID: ").strip()
    derived_port = assign_port(student_id)
    
    print(f"\nTarget Port (derived from ID): {derived_port}")
    print("1. Host Server + Start GUI")
    print("2. Join Existing Chat (Join a port)")
    
    choice = input("Choice (1/2): ").strip()

    if choice == "1":
        # Run server in background
        srv_thread = threading.Thread(target=launch_server, args=(derived_port,), daemon=True)
        srv_thread.start()
        time.sleep(0.5)
        # Start GUI in foreground
        launch_client(derived_port, student_id)

    elif choice == "2":
        target = input(f"Enter Port to connect to (Enter for {derived_port}): ")
        port_to_use = int(target) if target else derived_port
        launch_client(port_to_use, student_id)