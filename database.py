import mysql.connector as mysql

connection_params = {
    'user' : "root",
    'password' : "",
    'host' : "localhost",
    'database' : "personne" 
}

def cree_pers(nom, age):
    with mysql.connect(**connection_params) as db:
        with db.cursor() as cursor:
            #Insertion
            sql_insert = "INSERT INTO client (nom, age) VALUE (%s, %s)"
            cursor.execute(sql_insert, (nom, age))
            db.commit()

def afficher_pers():
    with mysql.connect(**connection_params) as db:
        with db.cursor() as cursor:
            #sql = "SELECT * FROM personne"
            #i = cursor.execute(sql)
            #cursor.fetchall()
            #for i in mysql:
            #    print(i)