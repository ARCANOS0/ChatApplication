# run.py — at project ROOT
import sys
import os
import threading

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def launch_server():
    from Server.server import start_server
    start_server()

def launch_client():
    from app import ChatClient
    app = ChatClient()
    app.run()

if __name__ == "__main__":
    print("=== Chat Application ===")
    print("1. Start Server + Client (first user)")
    print("2. Join existing chat (additional users)")
    
    choice = input("Choose (1/2): ").strip()

    if choice == "1":
        # start server in background thread
        server_thread = threading.Thread(target=launch_server)
        server_thread.daemon = True
        server_thread.start()
        # small delay so server is ready before client connects
        import time
        time.sleep(0.5)
        launch_client()  # GUI runs in main thread

    elif choice == "2":
        launch_client()  # just connect to existing server