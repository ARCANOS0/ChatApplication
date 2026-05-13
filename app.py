# app.py
import tkinter as tk
from tkinter import scrolledtext
import socket
import threading
from common.config import HOST

class ChatClient:
    def __init__(self, port, student_id): # Receive values from run.py
        self.window = tk.Tk()
        self.window.title(f"Chat - ID: {student_id}")
        self.student_id = student_id
        self.port = port

        # 1. Chat Display
        self.chat_area = scrolledtext.ScrolledText(self.window, state='disabled')
        self.chat_area.pack(padx=20, pady=5)

        # 2. Socket Setup
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect((HOST, self.port))
            # Immediately send ID to server so it knows who we are
            self.client.send(self.student_id.encode('utf-8'))
            
            thread = threading.Thread(target=self.receive_messages, daemon=True)
            thread.start()
        except Exception as e:
            print(f"Connection failed: {e}")
            self.window.destroy()
            return

        # 3. Message Entry
        self.msg_entry = tk.Entry(self.window)
        self.msg_entry.pack(padx=20, pady=5, fill=tk.X)
        self.msg_entry.bind("<Return>", lambda e: self.send_message())
        
        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

    def send_message(self):
        msg = self.msg_entry.get()
        if msg:
            self.client.send(msg.encode('utf-8'))
            self.display_message(f"You: {msg}")
            self.msg_entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message: self.display_message(message)
                else: break
            except: break

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

    def run(self):
        self.window.mainloop()