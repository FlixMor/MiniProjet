import connectdb as connectdb

db = connectdb.connect_db()
cursor = db.cursor()

def insertion(nom):
    sql = "INSERT INTO fileattente (nom) VALUE (%s)"
    infos = (nom, )
    cursor.execute(sql, infos)
    db.commit()

def suppression(nom):
    sql = "DELETE  FROM fileattente WHERE nom=%s"
    infos=(nom, )
    cursor.execute(sql,infos)
    db.commit()