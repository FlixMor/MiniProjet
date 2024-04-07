import connectdb as connectdb

db = connectdb.connect_db()
cursor = db.cursor()

def insertion(nom, age):
    sql = "INSERT INTO personnes(nom, age) VALUE(%s, %s)"
    
    infos = (nom, age)
    cursor.execute(sql, infos)
    db.commit()
    print("oui")

def get_all():
    sql = "SELECT * FROM personnes"
    cursor.execute(sql)
    i = cursor.fetchall()
    return i

def  recherche(nom,age):
    sql = "SELECT * FROM personnes WHERE  nom=%s AND age=%s"
    params = (nom,age)
    cursor.execute(sql,params)
    i=cursor.fetchone() 
    if i is None:
        return False
    else:
        return i