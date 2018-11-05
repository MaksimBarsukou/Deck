import sqlite3
import datetime


def log_winner(who_winner):
    date = "{:%B %d, %Y}".format(datetime.datetime.now())
    conn = sqlite3.connect('deck.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tournament (is_player_win, date) VALUES (?, ?)', (who_winner, date))
    conn.commit()
    conn.close()

# sql_crate = """CREATE TABLE tournament ('is_player_win','date','remained card')"""
# cursor.execute(sql_crate)  # создание БД с указанными таблицами
# conn.commit()
# conn.close()
# ----------------------------------------------------------------------------
# поплонение данными
# for i in db_test_code:
#     cursor.execute('INSERT INTO tournament (is_player_win, date) VALUES (?, ?)', (i))
#     conn.commit()
#     conn.close()

# ----------------------------------------------------------------------------
# удаление из таблицы
# del_db = """DELETE FROM tournament WHERE is_player_win ==1 and date == 123"""
# cursor.execute(del_db)
# conn.commit()
# conn.close()
# ----------------------------------------------------------------------------
# обновление данных
# update_db = """UPDATE tournament set date = 'October 31, 2018' WHERE OID = 4"""
# cursor.execute(update_db)
# conn.commit()
# conn.close()
# ----------------------------------------------------------------------------
# выборка строк из столбца и вывод в консоль
# x = cursor.execute("""SELECT * FROM tournament WHERE is_player_win == 'True'""")
# row = cursor.fetchone()
# while row is not None:
#     print(row)
#     row = cursor.fetchone()
# cursor.close()
# conn.close()
