from cryptography.fernet import Fernet
def keyGen():
    key=Fernet.generate_key()
    with open('data.key','wb') as fileGen:
        return fileGen.write(key)

def keyFile():
    with open('data.key','rb') as data:
        return data.read()
try:
    key= keyFile()
except FileNotFoundError:
    print('Key not found... generating new one 🗝️')
    keyGen()
    key=keyFile()

fer=Fernet(key)
def view():
    with open('password','r') as file:
        for data in file:
            m=data.rstrip()
            user,pwd=m.rsplit("|")
            print(f'Username : {user} | Password : {fer.decrypt(pwd.encode()).decode()}')
        
def add():
    userName=input("Username : ")
    pwd=input('Password : ')
    with open('password','a') as f:
        f.write(userName+"|"+fer.encrypt(pwd.encode()).decode()+'\n')
while True:
    mode = input("Do you want to add a password or view existing ones? (add/view, q to quit): ").lower()
    if mode=='q':
        break
    elif mode=='add':
        add()
    elif mode=='view':
        view()