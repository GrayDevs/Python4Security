# -*-coding:UTF-8 -*
# !/usr/bin/env python

""" Exercise: Password list generator for password spaying

# TODO
1) File management                  (utils) - DONE
2) create simple rules              (list) - DONE
3) create new password with rules
4) save tmp as a new file
5) cmdline
6) allow for custom rules
	from file or cli

# Exemple of what could be appended
- target firstname/surname/pseudo
- target city/country/area (fr, FRA, FRANCE, EMEA, ASIA, ...)
- target company (cisco, verizon, ibm, ...)

# rules key word
day     - append days
month   - append month
year    - append year
l       - lowercase
u       - uppercase
c       - capitalize
ic      - invert Capitalize
t       - Toggle Case
r       - Reverse
d       - Duplicate
$X      - append character
^X      - prepend character
"""

import datetime
from py4Sec.utils import file_handler


RULE = "c"


def main():

	# Common list
	nyear = 1
	year = datetime.datetime.now().year
	list_year = [year - i for i in range(nyear)]
	list_month = ["january", "february", "mars", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
	list_seasons = ["spring", "summer", "fall", "autumn", "winter"]
	list_number = ["123", "1234", "12345"]
	list_special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
	dict_nr = {'a': '@', 'o': '0', 'e': '3'}

	# open the wordlist
	wordlist = file_handler.file_operation('../../resources/wordlist_en.txt', 'open', 'r')
	file_handler.touch("tmp")
	tmp = file_handler.file_operation('tmp', 'open')
	for word in wordlist.readlines():
		print(word.strip('\n'))
		# copy wordlist into tmp
		# append word+month
		# append word+season
		# append numbers
		# append special char

		pass
	pass


if __name__ == "__main__":
	main()
