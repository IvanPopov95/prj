import os
import sys
os.chdir("C:\\Users\\popov\\Desktop\\python")
log = input('login: ')
password = input('password: ')
def login(login, password):
    with open ('users.txt') as f, open('users2.txt','w') as g: 
        for line in f:
            line = line.split()
            if line[0] == login:
                if line[2] == '1':
                    g.close()
                    os.remove('users2.txt')
                    print('mistake')
                    break
                else:
                    line[2] = '1'                  
                    g.write('   '.join(line)+ '\n')
            else:
                g.write('   '.join(line) + '\n')
        if os.path.isfile('users2.txt'):
            g.close()
            f.close()
            os.remove('users.txt')
            os.rename('users2.txt', 'users.txt')
def logout(login, password):
    with open ('users.txt') as f, open('users2.txt','w') as g: 
        for line in f:
            line = line.split()
            if line[0] == login:
                if line[2] == '0':
                    g.close()
                    os.remove('users2.txt')
                    print('mistake')
                    break
                else:
                    line[2] = '0'                  
                    g.write('   '.join(line)+ '\n')
            else:
                g.write('   '.join(line) + '\n')
        if os.path.isfile('users2.txt'):
            g.close()
            f.close()
            os.remove('users.txt')
            os.rename('users2.txt', 'users.txt')
def main():
    if sys.argv[1] == 'login':
        login(log, password)
    if sys.argv[1] == 'logout':
        logout(log, password)
if __name__ == '__main__':
    main()

