import os
import re
import socket

#first project

data =   """GET http://myhome.com/hello.html/hello/ HTTP/1.1
Host: myhome.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
If-Modified-Since: Fri, 05 Aug 2022 03:33:53 GMT
If-None-Match: "6db-5e57622a6e321-gzip"
Cache-Control: max-age=0"""

data2 = """CONNECT www.youtube.com:443 HTTP/1.1
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Proxy-Connection: keep-alive
Connection: keep-alive
Host: www.youtube.com:443"""

data3 = """GET http://localhost/ HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
If-Modified-Since: Fri, 05 Aug 2022 03:33:53 GMT
If-None-Match: "6db-5e57622a6e321-gzip"
Cache-Control: max-age=0

"""
'''
first_line= data.split("\n")[0]
url = first_line.split(" ")[1]
host = url.split("//")[1]
file = host.split("com")[1]
working_path = os.getcwd()
path = working_path + file




if path[len(path)-1] == "/":
	path = path[:-1]+ "/index.html"
print(path)
'''

'''
line = re.findall("Host:.*",data3,re.MULTILINE)[0]
host = line.split(": ")[1]

ty1 = re.compile(".*:.*")

if ty1.match(host):
	host_name = host.split(":")[0]
	port_no = host.split(":")[1]
else:
	host_name = host
	port_no = 80


print(host_name)
print(port_no)

s = socket.socket()
s.connect((host_name, port_no))
s.send(data.encode())
print(s.recv(1024).decode())
'''


#second project

file = open('common.txt', 'r')
line = file.readlines()



i=0
while i<= len(line)-1:
	


file.close()

	 