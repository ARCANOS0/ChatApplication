# main.py
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

def main():
    print("=== Chat Application ===")
    print("1. Start Server")
    print("2. Start Client")
    
    choice = input("Choose (1/2): ").strip()
    
    if choice == "1":
        from Server.server import start_server
        start_server()
    elif choice == "2":
        from client.client import start_client
        start_client()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()