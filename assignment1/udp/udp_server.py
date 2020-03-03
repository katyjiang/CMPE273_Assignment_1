import socket
import time

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
SPECIAL_MSG = ">_<done-{}`<>"
clients_dict={}

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))

    while True:
        # get the data sent to us

        data, ip = s.recvfrom(BUFFER_SIZE)
        if ip not in clients_dict.keys():
        	clients_dict[ip]=True
        	print("Accepting a file upload...")
        if data.decode("utf-8") == SPECIAL_MSG:
        	print("Upload successfully completed.")
        
        #Test time out
        #time.sleep(20) 

        s.sendto("ack".encode(), ip)


listen_forever()