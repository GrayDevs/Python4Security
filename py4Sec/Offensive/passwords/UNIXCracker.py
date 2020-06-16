#-*-coding:UTF-8 -*
#!/usr/bin/env python

""" Exercice: Créer un cracker de mot de passe UNIX

Resources:
- un fichier passwd
- un dictionnaire, ici nous utiliserons rockyou.txt

Hint: Un mot de pass UNIX est construit de la façon suivante:
    crypt('password','salt') = salt+encrypted_pwd.

Hint: crypt('egg','HX') = HX9LLTdc/jiDE.
"""

import crypt


def test_pwd(encrypted_pwd):
    salt = encrypted_pwd[0:2]
    dictionary = open('../../../resources/rockyou.txt')
    for word in dictionary.readlines():
        # make shure that line separator is LF and not CRLF or CR
        word = word.strip('\n')
        encrypted_word = crypt.crypt(word, salt)
        if (encrypted_word == encrypted_pwd):
            print("[+] Password PWNed:", word)
            return
    print("[-] No corresponding Password.")
    return


def main():
    passwd_file = open("../../../resources/passwd")
    for line in passwd_file.readlines():
        if ":" in line:
            user = line.split(':')[0]
            encrypted_pwd = line.split(':')[1].strip(' ')
            print("[*] Cracking password for:", user)
            test_pwd(encrypted_pwd)


if __name__ == "__main__":
    main()
