import sqlite3
import os.path


conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()


cursor.execute("""CREATE TABLE users
                    (login text,name text, surname text, email text, password text, is_logged_in integer)
               """)
cursor.execute("""INSERT INTO users
                    VALUES ('banan', 'Ivan', 'Popov', 'ivan@ya.ru', '1234', 0)""")


conn.commit()
conn.close()
