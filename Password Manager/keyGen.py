from cryptography.fernet import Fernet

def key_gen():
    key = Fernet.generate_key()
    with open('key.key',"wb") as key_file:
        key_file.write(key)
key_gen()
