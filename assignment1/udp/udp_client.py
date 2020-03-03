import socket
import time

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
SPECIAL_MSG = ">_<done-{}`<>"

def send(id=0):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		
		print("Connected to the server.")
		with open("upload.txt") as f:
			print("Starting a file (upload.txt) upload...")
			while True:
				line = f.readline()
				if not line:
					break
				index = line.find(":")
				seq_id = line[0:index]
				while True:
					try:
						s.sendto(f"{id}:{line}".encode(), (UDP_IP, UDP_PORT))
						s.settimeout(10)
						data, ip = s.recvfrom(BUFFER_SIZE)
						if data:
							print("Received ack("+seq_id+") from the server.")
							break
						print("received data: {}: {}".format(ip, data.decode()))
					except socket.timeout:
						print("Timeout exception!!")
						pass 
						
		print("File upload successfully completed.")
		while True:	
			s.sendto(f"{SPECIAL_MSG}".encode(), (UDP_IP, UDP_PORT))
			data, ip = s.recvfrom(BUFFER_SIZE)
			if data:
				break
		s.close()	
	except socket.error:
		print("Error! {}".format(socket.error))
		exit()


def get_client_id():
    id = input("Enter client id:")
    return id

send(get_client_id())