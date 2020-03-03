import socket
import sys
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "ping"

def send(id=0):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	# We first send our id to server.
	s.send(id.strip().encode('utf8'))
	message = None 
	while not(message == 'quit' or message == 'exit' or message == 'close'):
		message = input("Sending data: ")
		s.send(message.strip().encode('utf8'))
		data = s.recv(BUFFER_SIZE)
		if not data:
			break # happened when server itself closed
		print("Received data:" + data.decode().strip())
	s.close()

def send_ping(id, delay, num):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	# We first send our id to server.
	s.send(id.strip().encode('utf8'))
	for i in range(num):
		time.sleep(delay)
		s.send(MESSAGE.strip().encode('utf8'))
		print("Sending data:" + MESSAGE)
		data = s.recv(BUFFER_SIZE)
		if not data:
			break # happened when server itself closed
		print("Received data:" + data.decode().strip())
	s.close()
	
def get_client_id():
    id = input("Enter client id:")
    return id

if __name__ == "__main__":
	if len(sys.argv) == 1:
		send(get_client_id())
	elif len(sys.argv) == 4:
		send_ping(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))		
	else:
		print("python3 tcp_client.py [client id] [delay in seconds between messages] [number of 'ping' messages]")
