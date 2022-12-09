#!/bin/python3

import socket
import sys
import time
import threading

print("-"*71)
print("python port scanner")
print("-"*71)

uses = "uses:\n python3 port_scan.py host_name start_port end_port"

if len(sys.argv) < 2 or len(sys.argv) == 3:
	print(uses)
	sys.exit()

if len(sys.argv) == 2:
	start_port = 1
	end_port = 1000

elif len(sys.argv) == 4:
	start_port = int(sys.argv[2])
	end_port = int(sys.argv[3])

try :
	ip_addr = socket.gethostbyname(sys.argv[1])
except:
	print("Host name is not found")

start_time = time.time()

total_port = end_port - start_port

if total_port < 0:
	print('port no is not give in reverse')
	print(uses)
	sys.exit()

if end_port > 65535:
	print("port must be 0-65535")
	sys.exit()


def scanning(port):
	s = socket.socket()
	s.settimeout(1.5)
	conn = s.connect_ex((ip_addr, port))
	if not conn:
		print("port {} is open".format(port))
		 
	s.close()

for port in range(start_port, end_port+1):
	t1 = threading.Thread(target = scanning, args = (port,))
	t1.start()


total_time = time.time() - start_time
print("\nall {} port scanned in {}s ".format(total_port, total_time) )