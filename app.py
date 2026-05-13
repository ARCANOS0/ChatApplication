import tkinter as tk
from tkinter import scrolledtext
from tkinter import simpledialog
import socket
import threading
import sys
import os

# Path setup
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.config import HOST, PORT

class ChatClient:
    def __init__(self):

# !! the tk must be at the beginning before anything else 
        self.window = tk.Tk()
        self.window.title("Real-Time Chat")
        
        # ? asking user to put ID before proceeding, so I can assign the port number based on the ID and not the fixed one 
        #? as in the config.py file 
        self.student_id =  tk.simpledialog.askstring("Student", "Enter your ID: ")
        if not self.student_id :
            self.student_id = "Hamada"

        # 1. Chat Display Area
        self.chat_area = scrolledtext.ScrolledText(self.window, state='disabled')
        self.chat_area.pack(padx=20, pady=5)
        # Socket Setup
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect((HOST, PORT))
            self.client.send(self.student_id.encode('utf-8'))
            # Start a thread to listen for messages from server
            thread = threading.Thread(target=self.receive_messages)
            thread.daemon = True # Closes thread when window closes
            thread.start()
        except Exception as e:
            print(f"Connection failed: {e}")
            self.window.destroy()
        
        # 2. Message Entry Area
        self.msg_entry = tk.Entry(self.window)
        self.msg_entry.pack(padx=20, pady=5, fill=tk.X)
        self.msg_entry.bind("<Return>", lambda event: self.send_message())
        
        # 3. Send Button
        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)


    def send_message(self):
        msg = self.msg_entry.get()
        if msg:
            self.client.send(msg.encode('utf-8'))
            self.display_message(f"You: {msg}")
            self.msg_entry.delete(0, tk.END)
            if msg.lower() == "exit":
                self.window.destroy()

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message:
                    self.display_message(message)
                else:
                    break
            except:
                break

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END) # Scroll to bottom

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    client_app = ChatClient()
    client_app.run()