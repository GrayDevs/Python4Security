#!/usr/bin/env python
# --*--coding:UTF-8 --*--

import threading
import socket

buffer = 1024
adresse = ('127.0.0.1', 1338)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(adresse)
    print("Connection réussie")
except:
    try:
        s.connect((adresse[0], adresse[1] + 1))
        print("Connection réussie")
    except:
        print("Connection echoué")
        exit(0)


def receive():
    while 1:
        reponse = s.recv(buffer)
        if reponse.decode('utf8') == "":
            break
        print(f"\ri :{reponse.decode('utf8')}", end="\n=>")


t = threading.Thread(target=receive)
t.start()

while True:
    # receive()
    requete = input().strip()
    s.send(bytes(requete, 'utf8'))
    if requete=='quit()':
        break

s.close()
print("fin du client TCP")
