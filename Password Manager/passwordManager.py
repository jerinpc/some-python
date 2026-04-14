from cryptography.fernet import Fernet

def key_file():
    with open("key.key",'rb') as file:
        return file.read()
key= key_file()
fer=Fernet(key)
"""def key_gen():
    key = Fernet.generate_key()
    with open('key.key',"wb") as key_file:
        key_file.write(key)
key_gen()"""

def view():
    with open('database','r') as f:
        for data in f.readlines():
            s=data.rstrip()
            user,pwd=s.split("|")
            print(f"username : {user} | password : {fer.decrypt(pwd.encode()).decode()}")
def add():
    userName=input("Username : ")
    pwd = input("password : ")
    with open('database','a') as f:
        f.write(userName+'|'+fer.encrypt(pwd.encode()).decode()+'\n')

while True:
    mode = input("Do you want to add a password or view existing ones? (add/view, q to quit): ").lower()

    if mode=='q':
        break
    elif mode=='add':
        add()
    elif mode =='view':
        view()
