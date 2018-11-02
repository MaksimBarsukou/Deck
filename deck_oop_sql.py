import sqlite3
import datetime


# тестовый заполнитель
def aggregate():
    time = "{:%B %d, %Y}".format(datetime.datetime.now())
    x = [x for x in range(5)]
    tes_date = []
    for i in x:
        if i % 2 == 0:
            tes_date.append(('True', time))
        else:
            tes_date.append(('False', time))
    return tes_date


conn = sqlite3.connect('deck.db')
cursor = conn.cursor()
# sql_crate = """CREATE TABLE tournament ('is_player_win','date')"""
# cursor.execute(sql_crate)  # создание БД с указанными таблицами
# commit
# ----------------------------------------------------------------------------
# поплонение данными
# for i in db_test_code.s:
#     cursor.execute('INSERT INTO tournament (is_player_win, date) VALUES (?, ?)', (i))
#     conn.commit()
# ----------------------------------------------------------------------------
# удаление из таблицы
# del_db = """DELETE FROM tournament WHERE is_player_win ==1 and date == 123"""
# cursor.execute(del_db)
# commit
# ----------------------------------------------------------------------------
# обновление данных
# update_db = """UPDATE tournament set date = 'October 31, 2018' WHERE OID = 4"""
# cursor.execute(update_db)
# commit
# ----------------------------------------------------------------------------
# выборка строк из столбца и вывод в консоль
# x = cursor.execute("""SELECT * FROM tournament WHERE is_player_win == 'True'""")
# row = cursor.fetchone()
# while row is not None:
#     print(row)
#     row = cursor.fetchone()
# cursor.close()
# conn.close()
