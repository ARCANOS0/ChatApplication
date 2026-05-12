# to solve the issue of python not recognizing the file as a pakcage 
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

if parent_dir not in sys.path:
    sys.path.append(parent_dir)



# server accepts connections & responds 
from common.config import*
import socket as soc 

def start_server() :
    server = soc.socket(soc.AF_INET, soc.SOCK_STREAM) 
    # this line is important 3shan bt2ol ll OS to establish connection TCP & to use IPv4 

    server.bind((HOST, PORT))
    # bind means connect, ربط حرفياً
    # * bind takes tuple, this is why we put HOST & PORT inside of other parenthsis 
    server.listen(5)
    """listen has a backlog arg, means how many unconnected client can wait on the queue 
       before refusing new clients 
    """

    while(True) :

        client, client_address = server.accept()
        print(f"Client connected at client {client_address}")

        try:
            msg = client.recv(1024).decode('utf-8')

            if msg :
                print(f"message received from client {msg}")
                response = "msg received! Client!"
                client.send(response.encode('utf-8'))
        
        except Exception as e :
            print(f"Error {e}")

        finally :
            client.close()
