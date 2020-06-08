# --*--coding:UTF-8 --*--

import platform  # Pour recuprérer le nom de l'OS
import socket
import subprocess  # Permet d'executer les commandes systemes
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from time import time


def ping(host: str, upHostList: list):  # Retourne vrai si l'hote repond au ping

    # Modifie d'option pour n'envoyer qu'un paquet en fonction de l'OS
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Créer la commande de ping
    command = ['ping', param, '1', '-i', '0.5', host]

    # Retourne vrai si le ping repond 0
    result = subprocess.call(command, stdout=subprocess.DEVNULL) == 0
    if result:
        upHostList.append(host)
    counter()
    return result


def counter():
    counter.count += 1

    if time() - counter.last_print > 0.1:
        counter.last_print = time()
        print("Scanned {} ports...".format(counter.count), end="\r")


counter.count = 0
counter.last_print = 0

# Declaration des variables
upHostList = []
threadList = []

# Recupere l'ip de l'ordinateur sur le sous réseau
reseau = socket.gethostbyname(socket.gethostname())
reseau = reseau.split('.')

# Effetue le ping sur une partie du sous reseau
with ThreadPoolExecutor(max_workers=200) as executor:
    hostList = []
    for nb in range(1, 255):
        ip = reseau
        ip[3] = str(nb)
        ip = '.'.join(reseau)
        hostList.append(ip)
        threadList.append(executor.submit(ping, ip, upHostList))

    # Attendre que le scan finisse
    wait(fs=threadList, return_when=ALL_COMPLETED)
    print(f"\rScanned {threadList.__len__()} posts...")
    print("done")
print(upHostList)
