import socket

print('creation du socket ...')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket fait')
print("connection a l'hote distant")
s.connect(('www.google.com', 80))
print('connection faite')
s.sendall(b'GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n')
while 1:
    data = s.recv(1024)
    print(data)
    if data == b"":
        break
s.close()
print('Fin')