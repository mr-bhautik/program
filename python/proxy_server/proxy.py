import socket
import re

def grep_data(x):
	line = re.findall("Host:.*",x,re.MULTILINE)[0]
	host = line.split(": ")[1]

	ty1 = re.compile(".*:.*")

	if ty1.match(host):
		host_name = host.split(":")[0]
		port_no = host.split(":")[1]
	else:
		host_name = host
		port_no = 80
	return port_no , host_name
 
def send_data(x, y , z):
	client = socket.socket()
	
	client.connect((x, int(y)))
	print('connect to server')
	client.send(z.encode())
	print('send data to server')
	recice_from_server = client.recv(10240)
	
	return recice_from_server


if __name__ == '__main__':
	HOST = "localhost"
	PORT = 8080
	s = socket.socket()
	print('socket created')
	s.bind((HOST, PORT))
	s.listen(1)
	print('start listening...')
	while True:
	
		conn, addr = s.accept()
		print('connection from {}'.format(addr))
		data = conn.recv(1024).decode()
		print(data)
		port_no , host_name = grep_data(data)
		recive_data = send_data(host_name , port_no, data)
		print("client data:\n", recive_data.decode())
		conn.send(recive_data)
		print('send data to client')
	
