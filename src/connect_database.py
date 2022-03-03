import pymysql


def open_database_mc_skin():
    try:
        db = pymysql.connect(host='localhost', user='root', password='', port=3306, database='mc_skin', autocommit=True)
        print('database "mc_skin" open successfully!!!')
    except pymysql.Error as e:
        print('database "mc_skin" open failed!!!')
        print(e)
        return None
    return db


def close_database(db):
    db.close()


def update_skin_set_model_by_id(db, skin_id, model):
    with db.cursor() as cursor:
        try:
            cursor.execute('UPDATE `skin` SET `model` = %s WHERE `id` = %s', (model, skin_id))
            print((model, skin_id))
        except pymysql.Error as err:
            print(err)


def update_skin_set_passageway_by_id(db, skin_id, passageway):
    with db.cursor() as cursor:
        try:
            cursor.execute('UPDATE `skin` SET `passageway` = %s WHERE `id` = %s', (passageway, skin_id))
            print((passageway, skin_id))
        except pymysql.Error as err:
            print(err)
