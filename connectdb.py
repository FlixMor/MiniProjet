import mysql.connector as mysql

def connect_db():
    db = mysql.connect(
        user = 'root',
        password = '',
        host = 'localhost',
        database = 'ecole'
    )
    return db

def insertion(code_permanent, nom, prenom, date_naissance, specialite):
    sql = "INSERT INTO etudiant(code_permanent, nom, prenom, date_naissance, specialite) VALUE(%s, %s, %s,%s, %s)"
    #remplace les %s par les arguments
    db = connect_db()
    cursor = db.cursor()
    infos = (code_permanent, nom, prenom, date_naissance, specialite)
    cursor.execute(sql, infos)
    db.commit()

def affichage():
    sql = "SELECT * FROM etudiant"
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(sql)
    i = cursor.fetchall()
    for result in i:
        print(result)




#tester insertion
affichage()
exit()
code_permanent = input(print("Entrer le code permanent :"))
nom = input(print("Entrer le nom :"))
prenom = input(print("Entrer le prenom :"))
date_naissance = input(print("Entrer la date de naissance :"))
specialite = input(print("Entrer la specialite :"))
insertion(code_permanent, nom, prenom, date_naissance, specialite)



"""
connection_db = mysql.connect (
    user = 'root',
    password = '',
    host = 'localhost',
    database = 'personne'
)

cursor = connection_db.cursor()

def  get_all():
    sql = "SELECT * FROM client"
    cursor.execute(sql)
    i = cursor.fetchall()
    for r in i:
        print(r)

def  add_client(nom, prenom):
    sql= "INSERT INTO client VALUES(%s,%s)"
    try :
        cursor.execute(sql,(nom,prenom))
        connection_db.commit()
        print("Client ajouté")
    except :
        print("Erreur d'ajout du client")

get_all()
"""