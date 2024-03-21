import mysql.connector as mysql

connection_params = {
    'user' : "root",
    'password' : "",
    'host' : "localhost",
    'database' : "ecole" 
}

with mysql.connect(**connection_params) as db:
    with db.cursor() as cursor:
        sql = "SELECT * FROM ETUDIANT WHERE nom='Parent' or prenom='Felix'"
        cursor.execute(sql)
        etudiant = cursor.fetchall()

        #Insertion
        sql_insert = "INSERT INTO ETUDIANT ('code_permanent', 'nom', 'prenom', 'specialite') VALUE ('SL4353', 'Labrie', 'Stephane', 'securite inf')"
        cursor.execute(sql_insert)
        db.commit()
