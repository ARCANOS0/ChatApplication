# TODO : for this file I need to implement some standard configs for the whole project 

"""

in the specfications there are : 

1- the port number is based on the last 5 digits of the ID (e.g ID 2320106 : PORT = 20106)
2- if the last 5 digits are higher than the 65535, we will use the last 4 digits only (e.g 8008)
3- If the port number is less than 1024, students must add 10000 to ensure it is within the


ONE client connection per server 
"""

# global variables 

STUDENT_ID = "0000000" # TODO : change it later based on the level of implementation 

HOST = "127.0.0.1" # local host 


# exctracting logic 
def assign_port(id : str) -> int : 
    converted_id = int(id[-5:]) # get the last 5 digits of the id
    if converted_id > 65535 :
        converted_id = int(id[-4:]) # get the last 4 digits of the id
    elif converted_id < 1024 :
        converted_id += 10000 # add 10000 to ensure it is within the valid range

    return converted_id 


# global variable for the port number
PORT = assign_port(STUDENT_ID)
