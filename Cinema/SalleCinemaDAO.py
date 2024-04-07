import connectdb as connectdb

db = connectdb.connect_db()
cursor = db.cursor()

def insertion(nom, place):
    sql = "INSERT INTO cinema (nom, place) VALUE (%s, %s)"
    infos = (nom, place)
    cursor.execute(sql, infos)
    db.commit()
    print("oui")


def get_all():
    sql = "SELECT * FROM cinema"
    cursor.execute(sql)
    i = cursor.fetchall()
    return i

def get_by_name(nom):
    sql = "SELECT * FROM cinema WHERE nom=%s"
    infos = (nom, )
    cursor.execute(sql,infos)
    i = cursor.fetchall()
    return i

def remove(nom):
    sql = "DELETE FROM cinema WHERE nom=%s"
    infos = (nom, )
    cursor.execute(sql,infos)
    db.commit()
    return 