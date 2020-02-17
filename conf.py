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
            return 1
    elif not password_check(log, password):
        return 0


def login():
    log = input('login: ')
    password = input('password: ')
    if login_internal(log, password):
        print('You are already in system') 
    elif not login_internal(log, password):
        print('Wrong password try one more time')
        login()


def logout():
    log = input('login: ')
    if not log_out(log):
        print('You are not in system')


def email_check(email):
    return '@' in email


def registration():
    log = input('login: ')
    name = input('name: ')
    if len(name) == 0:
        name = ''
    surname = input('surname: ')
    if len(surname) == 0:
        surname = ''
    email = input('Email: ')
    while not email_check(email):
        print('Email is not correct')
        email = input('Email: ')
    password = input('password: ')
    cursor.execute("""INSERT INTO users(login, name, surname, email, password, is_logged_in)
VALUES(?, ?, ?, ?, ?, ?)""", (log, name, surname, email, password, 1))
    conn.commit()


def name_surname_change():
    log = input('login: ')
    name = input('new name: ')
    surname = input('new surname: ')
    cursor.execute("""UPDATE users SET name = ?, surname = ? 
                   WHERE login = ?""", (name, surname, log))
    conn.commit()

if __name__ == '__main__':
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor() 
    if sys.argv[1] == 'login':
        login()
    if sys.argv[1] == 'logout':
        logout()
    if sys.argv[1] == 'reg':
        registration()
    if sys.argv[1] == 'change':
        name_surname_change()
    conn.close()
