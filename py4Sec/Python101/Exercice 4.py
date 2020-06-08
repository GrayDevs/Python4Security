# --*--coding:UTF-8 --*--

import socket
from concurrent.futures import ThreadPoolExecutor, Executor
from datetime import datetime
from sys import argv
from time import time

# Liste port par type de scan
printer = [170, 515, 631, 3396, 9100, 9303]
linuxPort = [20, 21, 22, 23, 25, 68, 80, 111, 443, 445, 631, 993, 995, 5353]
windowsPort = [135, 137, 138, 139, 445]
macPort = [22, 445, 548, 631]
allPort = printer + linuxPort + windowsPort + macPort


# Permet de conter les ports scanne
class Counter:
    def __init__(self):
        self.count = 0
        self.last_print = 0

    def iterate(self):
        self.count += 1

        if time() - self.last_print > 0.1:
            self.last_print = time()
            print(f"Scanned {self.count} ports...", end="\r")


# Permet de lancer les scan TCP et udp par rapport scan
def task(reseau: str, portList: list, executor: Executor):
    adresse = net2 + str(reseau)

    for port in portList:
        executor.submit(tcpScan, hostList, port, adresse)
        executor.submit(udpScan, hostList, port, adresse)


# scan les ports TCP et attend une réponse
def tcpScan(hostUpList: list, tcpPort: int, addr: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((addr, tcpPort))
    if result == 0 or result == 103:
        addhost(hostUpList, addr, tcpPort, 'tcp')

    s.close()

    counter.iterate()


# scan les port UDP et attend une réponse
def udpScan(hostUpList: list, udpPort: int, addr: str):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = "Hello"
        s.sendto(bytes(data, 'utf-8'), (addr, udpPort))
        s.settimeout(1)
        r = s.recvfrom(1024)
        addhost(hostUpList, addr, udpPort, 'udp')
    except:
        pass

    counter.iterate()


# Permet d'afficher si un port ouvert a été trouvé
def addhost(list: list, hostAddr: str, port: int, protocol: str):
    if hostAddr in list:
        list.append(hostAddr)
        print(f'{hostAddr}, port : {port}, protocole {protocol}--> Live')


hostList = list()

t1 = datetime.now()

net = socket.gethostbyname(socket.gethostname())
net1 = net.split('.')
a = '.'
net2 = ""

for i in range(3):
    net2 += net1[i] + a

start = int(argv[1])
end = int(argv[2])
end = end + 1
counter = Counter()

# Separation scan en thread
with ThreadPoolExecutor(max_workers=200) as executor:
    for i in range(start, end):
        # Start new thread
        task(net2 + str(i), allPort, executor)

print('\r\n' + str(hostList))
