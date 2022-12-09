import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = socket.gethostbyname('www.google.com')
    s.connect((ip, 80))
    request = "GET / HTTP/1.1\n\n"
    s.send(request.encode())
    global data 
    data = s.recv(1000).decode()
main()
print(data)