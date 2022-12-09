import socket
import sys
import re

print("-" *75)
print("python dir_buster ")
print("-" *75)

wordlist = "/home/kali/Documents/program/python/common.txt"
uses = "python3 dir_buster.py host_name port_no wordlists"

if len(sys.argv) < 3 or len(sys.argv) > 4:
	print(uses)
	sys.exit()


host_name = sys.argv[1]
port_no = int(sys.argv[2])
try:
	ip_addr = socket.gethostbyname(host_name)
except:
	print("not find host")

def grep_data(x):
	first_line = x.split("\n")[0]
	responce_type = first_line.split(" ")[1]
	return responce_type

def send_request(x):
	s.connect((ip_addr, port_no))
	data = "HEAD /{}.html HTTP/1.1".format(x)
	s.send(data)
	recv_data = s.recv(1024)
	r_data = grep_data(recv_data)
	return r_data


def main():
	s = socket.socket()
	try:
		
		while True:

			file = open('common.txt', 'r')
			line = file.readlines()
			i=0
			while i<= len(line)-1:
				typedata = send_request(line[i])
				print("reaqust at",line[i], typedata)



	except:
		print("socket not created")


