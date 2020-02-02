import sys
import sqlite3


def password_check(log, password):
    cursor.execute("""SELECT password FROM users WHERE login = ?""", (log,))
    res = cursor.fetchone()
    return res[0] == password
    

def change_islogin(log):
    islogin = islogin_select(log)
    if islogin == 0:
        cursor.execute("""UPDATE users SET islogin = 1 WHERE login = ?""", (log,))
    else:
        cursor.execute("""UPDATE users SET islogin = 0 WHERE login = ?""", (log,))
    conn.commit()


def islogin_select(log):
    cursor.execute("""SELECT islogin FROM users WHERE login = ?""", (log,))
    res = cursor.fetchone()
    return res[0]


def login():
    log = input('login: ')
    password = input('password: ')
    if password_check(log, password):
        islogin = islogin_select(log)
        if islogin == 0:
            change_islogin(log)
        else:
            print('You already login')
    else:
        print('Wrong Password')


def logout():
    log = input('login: ')
    islogin = islogin_select(log)
    if islogin == 1:
        change_islogin(log)
    else:
        print('You are not in system')

  
if __name__ == '__main__':
    cursor = conn.cursor() 
    conn = sqlite3.connect("mydatabase.db")

    if sys.argv[1] == 'login':
        login()
    if sys.argv[1] == 'logout':
        logout()
    conn.close()     
