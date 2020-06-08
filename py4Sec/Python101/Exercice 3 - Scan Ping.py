# --*--coding:UTF-8 --*--

import platform  # Pour recuprérer le nom de l'OS
import socket
import subprocess  # Permet d'executer les commandes systemes


def ping(host):  # Retourne vrai si l'hote repond au ping

    # Modifie d'option pour n'envoyer qu'un paquet en fonction de l'OS
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Créer la commande de ping
    command = ['ping', param, '1', '-i', '0.2', host]

    # Retourne vrai si le ping repond 0
    return subprocess.call(command, stdout=subprocess.DEVNULL) == 0


# Recupere l'ip de l'ordinateur sur le sous réseau
reseau = socket.gethostbyname(socket.gethostname())
reseau = reseau.split('.')

# Effetue le ping sur une partie du sous reseau
for nb in range(245, 250):
    ip = reseau
    ip[3] = str(nb)
    ip = '.'.join(reseau)
    print(f'ip : {ping(ip)}')
