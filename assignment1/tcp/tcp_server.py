import socket
import asyncio

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "pong"

"""
A sync function used to handle one single client connection.
This means whenever a client connect with the server, this function
will run for that single client.
"""
async def handle_client(reader, writer):
	# We always suppose client will send their client id to the server
	# as the first message
	client_id = (await reader.read(BUFFER_SIZE)).decode('utf8').strip()
	print("Connected Client:" + client_id + ".")
	
	try:	
		request = (await reader.read(BUFFER_SIZE)).decode('utf8').strip()
		while not(request == 'exit' or request == 'close' or request == 'quit'):
			print("Received data:%s:%s" % (client_id, request))
			writer.write(MESSAGE.strip().encode('utf8'))
			await writer.drain()
			request = (await reader.read(BUFFER_SIZE)).decode('utf8').strip()
			if not request:
				break 
		writer.close()
	except:
		pass
	
async def listen_forever():
	# We first start the server asynchrously
	server = await asyncio.start_server(handle_client, TCP_IP, TCP_PORT)

	print("Server started at port " + str(TCP_PORT))	

	# Make server run forever
	async with server:
		try:
			await server.serve_forever()
		except KeyboardInterrupt:
			# We will receive this keyboard interrupt exception
			# when user ctrl+c try to stop the server
			return

if __name__ == "__main__":
	asyncio.run(listen_forever())
