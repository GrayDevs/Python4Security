import re
import urllib.request
import urllib.parse

url = 'http://www.celsa.fr/contacts.php'
values = {'s':'basics',
			'submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()
DataString = str(respData)

Mailadress = re.findall(r"[\w.-]+?@[\w.-]+?\.[\w.-]+?\b", str(DataString))
ContactInfo = re.findall(r"\d{2}\s\d{2}\s\d{2}\s\d{2}\s\d{2}", str(DataString))

#(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)
#[\w.-]+?@\w+?\.\w+?\b



'''for eachMail in Mailadress:
	print(eachMail)

for eachC in ContactInfo:
	print(eachC)'''

ContactDict = {}

x = 0
for eachMail in Mailadress:
    ContactDict[eachMail] = ContactInfo[x]
    x += 1
    if x == 20:
        break

print(ContactDict)

if not ContactInfo: 
	print('Nothing found')
