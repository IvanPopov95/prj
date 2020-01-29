import sys
import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor() 


log = input('login: ')
password = input('password: ')


def password_check(log, password):
    cursor.execute("""SELECT password FROM users WHERE login = ?""", log.split())
    res = cursor.fetchone()
    i = res[0]
    return i == int(password)
        

def change_id(id):
    if id == 0:
        cursor.execute("""UPDATE users SET id = 1 WHERE login = ?""", log.split())
    else:
        cursor.execute("""UPDATE users SET id = 0 WHERE login = ?""", log.split())
    conn.commit()


def dict_of_data(log, password):
    cursor.execute("""SELECT id FROM users WHERE login = ?""", log.split())
    res = cursor.fetchone()
    d = {'login': log, 'password': password, 'id': res[0]}
    return d


def login(log, password):
    if password_check(log, password):
        a = dict_of_data(log, password)
        if a['id'] == 0:
            change_id(0)
        else:
            print ('mistake')
    else:
        print ('Wrong Password')


def logout(log, password):
    if password_check(log, password):
        a = dict_of_data(log, password)
        if a['id'] == 1:
            change_id(1)
        else:
            print ('mistake')
    else:
        print ('Wrong Password')


def main():
    if sys.argv[1] == 'login':
        login(log, password)
    if sys.argv[1] == 'logout':
        logout(log, password)
    
if __name__ == '__main__':
    main()       
