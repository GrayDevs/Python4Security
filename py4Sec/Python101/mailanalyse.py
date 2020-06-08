import sys, email, time, re, os

def getserver(msg):
	if not 'X-Received' in msg:	
		return None
	server = msg['X-Received'].rsplit('with', 1)[0]
	try:
		return server
	except:
		return None

def getdate(msg):
	if not 'date' in msg:
		return None
	datehdr = msg['date'].strip()
	try:
		return datehdr
	except:
		return None

def getsender(msg):
	if not 'From' in msg:
		return None
	sender = msg['From'].strip()
	try:
		return sender
	except:
		return None

def getreceiver(msg):
	if not 'To' in msg:
		return None
	receiver = msg['To'].strip()
	try:
		return receiver
	except:
		return None

#def find IP
#	if re.match(ipregex, msg) is not None:
 # 	print (ipregex)

exemple = '''193.50.230.155

qbfst
bbgn
s
srtnr
d19.252.87.177
226.118.114.39
72.171.66.20
182.201.106.241
49.76.189.182
'''






msg = email.message_from_file(sys.stdin)
#msg = open("test.txt")
msg2 = str(msg)

ipregex = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", msg2)



dateval = getdate(msg)
senderval = getsender(msg)
receiverval = getreceiver(msg)
serverval = getserver(msg)


if receiverval is None:
	receiverval = ("Inconnu.")


if senderval is None:
	print ("Pas d'auteur valide, message envoyé à", receiverval)
else:
	print ("Le message a été envoyé par", senderval,"à", receiverval)

if dateval is None:
	print ("Pas de date valide trouvée.")
else:
	print ("Envoyé à", dateval)

if serverval is None:
	print ("Pas de server valide trouvé.")
else:
	print ("Envoyé depuis le serveur", serverval)

if ipregex is None:
	print ("Pas de d'addresse IP trouvée.")
else:
	print ("addresse IP d'envoi:", ipregex)

