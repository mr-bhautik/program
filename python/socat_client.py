import socket
SERVER = 'localhost'
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.send(bytes('hello from client', 'utf-8'))
while True:
	data = client.recv(1024)
	print(data)
	senddata= input()
	client.send(bytes(senddata, 'utf-8'))
client.close()	

