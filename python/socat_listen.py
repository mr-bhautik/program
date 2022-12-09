import socket
HOST = 'localhost'
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print('server started....')
while True: 
	conn, addr = server.accept()
	print('connected by {}'.format(addr))
	while True:
		data = conn.recv(1024)
		print(data.decode())
		send_data = input()
		conn.send(bytes(send_data.encode()))
	
conn.close()

	
