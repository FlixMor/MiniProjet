import mysql.connector as mysql

connection_params = {
    'user' : "root",
    'password' : "",
    'host' : "localhost",
    'database' : "personne" 
}

with mysql.connect(**connection_params) as db:
    with db.cursor() as cursor:
        pass
        #Insertion
        #sql_insert = "INSERT INTO PERSONNE ('nom', 'age') VALUE ('Labrie','22')"
        #cursor.execute(sql_insert)
        #db.commit()
