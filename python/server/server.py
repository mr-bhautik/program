import socket
import os
import re

def grep_data(x):
	working_path = os.getcwd()
	first_line= x.split("\n")[0]
	url = first_line.split(" ")[1]
	path = working_path + url

	if path[len(path)-1] == "/":
		path = path[:-1]+ "/index.html"

	return path

def main():

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print('[+] socket created')
	s.bind(('localhost', 80))
	print('[+] servere created')
	s.listen(1)
	print('[*] start listening....')	
	while True:
		conn, addr = s.accept()
		print('[+] connected from {}'.format(addr))
	
		while True:	

			recvdata = conn.recv(4096)
				
			print('[*] get data from client\n\ndata:')
			print(recvdata.decode())
			request = recvdata.decode()
			
			path = grep_data(request)
			try:
				file = open(path)
				data = "HTTP/1.1 200 OK\n" + file.read()
			except :
				data = """<h1>forbidden</h1>
				<h2>bad requeast</h2>
				<h2>file is not available in server</h2>


				"""
					
							
			print('send data to client')
			conn.send(bytes(data.encode()))
			print("data sent", data)
			file.close()
		
	conn.close()
if __name__ == '__main__':
	
		main()