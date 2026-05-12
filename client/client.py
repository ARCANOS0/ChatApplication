import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

if parent_dir not in sys.path:
    sys.path.append(parent_dir)


from common.config import*

import socket as soc


#  simple implementation of host name & printing the host name 



def start_client() :
    client = soc.socket(soc.AF_INET, soc.SOCK_STREAM)


    try :
      
    #  connection to the localhost & the port assigned based on the function in common.py
      client.connect((HOST, PORT))
      print(f"Connected Sucessefuly to {PORT}") # print 3shan kollo yb2a wade7 

      msg = "Hello from client!" # ? test 
      client.send(msg.encode('utf-8'))

    #   yalla n receive the response 
      response = client.recv(1024).decode('utf-8')  
      # !! Attention: recv(buffer) which means max size of msg in bytes, usaully 1024 byte 

      print(f"response from srever {response}")

    except Exception as e :
     
        print(f"Error: {e}")

    finally : 
      client.close()
     


