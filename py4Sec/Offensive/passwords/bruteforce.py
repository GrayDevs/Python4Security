#-*- coding:UTF-8 -*
#!/bin/usr/env python

""" Script: Exemple d'attaque par force brute

Pour cette exercice, nous allons simplement tester en combien de temps une attaque bruteforce peut casser les mots de passe les plus commun.
Ce code peut bien évidemment être modifié pour tester des mots de passe sur un service en ligne mais comme nous le verrons, ce n'est certainement pas la tactique la plus adaptée.

Pour éviter d'avoir trop de boucle imbriqué, nous choisissons de développer notre script autour d'une base,
tout comme la base 16 (hexadécimale) qui contient les lettres A à F en plus des chiffres de 0 à 9.
Notre base contiendra quand à elle tout les caractères que l'on souhaite tester.

Pour générer un mot de passe, il suffira alors d'incrémenter un compteur (entier) et de le convertir dans notre base.

Améliorations possibles:
- Récupérer le/les mots de passe depuis un fichier
- improve base conversion
- interface console/gui
- Multi-threading
- bruteforce à partir d'un certain nombre de caractères, selon la politique de mot-de-passe de la cible
- Bonnes pratique de programmation: error handling, logging, répartir le code sur différentes fonctions, test unitaire
- ...
"""

import time
import string

# Global vars
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
specials = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ']
# possible_chars0 = numbers + lowers + uppers + specials
POSSIBLE_CHARS = list(string.printable)[:95]
BASE = len(POSSIBLE_CHARS)  # base utilisée pour la conversion
#assert possible_chars0 == possible_chars

MAX_ATTEMPTS = 10000000  # Pour les besoins de la démo, nous limitons le nombre d'essai.


def base_conversion(a, b):
	""" Convertis un nombre a
	:param a: <int> - entier en base 10
	:param b: <list> -
	:return:
	"""
	converted = []
	while a:
		converted.append(int(a % b))
		a //= b
	return converted[::-1]


def main():

	start = time.time()
	number_of_attempts = 0
	attack_success = False

	password = input("Enter the password to test:")

	# Cas particuliers
	if password == '':
		print('[!] Password is empty')
		attack_success = True

	elif password == POSSIBLE_CHARS[number_of_attempts]:
		print('[!] password is ' + POSSIBLE_CHARS[number_of_attempts])
		attack_success = True

	else:
		number_of_attempts += 1

	# début du bruteforce
	if not attack_success:
		while number_of_attempts < MAX_ATTEMPTS:
			lst = base_conversion(number_of_attempts, BASE)
			print(lst)
			word = ''
			for c in lst:
				word += str(POSSIBLE_CHARS[c])
			if password == word:
				attack_success = True
				print('** Results **')
				print('Password: ' + word)
				print('Attempts: ' + str(number_of_attempts))
				print('Time: ' + str((time.time() - start)) + ' sec')
				break
			else:
				number_of_attempts += 1

	# the password is beyond our maxattempts
	if not attack_success:
		print('Unsolved after ' + str(number_of_attempts) + ' attempts!')


if __name__ == "__main__":
	main()
	pass
