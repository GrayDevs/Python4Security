import MySQLdb

# Connection
db = MySQLdb.connect(host='localhost', user='root', passwd='test', db='mysql')
# Effetuer requete
db.query("SELECT * FROM mysql.user")
resultat = db.use_result()
ligne = 0
while ligne != ():
    ligne = resultat.fetch_row()
    print(ligne)
    db.use_result()
