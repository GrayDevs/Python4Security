#-*- coding:UTF-8 -*
#!/bin/usr/env python

""" Script: Simple password generator
"""

# Libs
import argparse
import string
# import random  # usable but less secure
import secrets


# Functions
def generate_pwd(pwd_length):
	password = ''
	for n in range(pwd_length):
		x = secrets.randbelow(94)
		password += string.printable[x]
	return password


def main():
	# Processing command line arguments
	parser = argparse.ArgumentParser()

	# Positional arguments (option), these are always required
	# parser.add_argument('length', help='the length of the password to generate', type=int)

	# Optional arguments
	parser.add_argument('-l', '--length', help='the length of the password to generate', dest='length', default=16, type=int)
	args = parser.parse_args()
	pwd_length = args.length

	# default pwd
	if pwd_length is None:
		pwd_length = 16

	password = generate_pwd(pwd_length)
	print(password)
	assert len(password) == pwd_length


if __name__ == "__main__":
	main()
