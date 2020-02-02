import sys
import sqlite3


def password_check(log, password):
    cursor.execute("""SELECT password FROM users WHERE login = ?""", (log,))
    res = cursor.fetchone()
    return res[0] == password
    

def log_in(log):
    res = (cursor.execute("""UPDATE users SET is_logged_in = 1
WHERE login = ? AND is_logged_in = 0""", (log,)).rowcount)
    conn.commit()
    return res > 0
    

def log_out(log):
    res = (cursor.execute("""UPDATE users SET is_logged_in = 0
WHERE login = ? AND is_logged_in = 1""", (log,)).rowcount)
    conn.commit()
    return res > 0


def login_internal(log, password):
    if password_check(log, password):
        if not log_in(log):
            return 'You already login'
    else:
        return 'Wrong Password'
            

def login():
    log = input('login: ')
    password = input('password: ')
    if login_internal(log, password) is not None:
        print(login_internal(log, password))


def logout():
    log = input('login: ')
    if not log_out(log):
        print('You are not in system')


if __name__ == '__main__':
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor() 
    if sys.argv[1] == 'login':
        login()
    if sys.argv[1] == 'logout':
        logout()
    conn.close()
