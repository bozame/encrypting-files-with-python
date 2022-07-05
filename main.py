#Generating a key for the file
from cryptography.fernet import Fernet
key = Fernet.generate_key()

with open('saved_key.key','wb') as file:
    file.write(key)

#Encrypting
key =''
with open('saved_key.key', 'rb') as file:
    key = file.read()

data =''
with open('text.txt', 'rb') as file:
    data = file.read()

f = Fernet(key)

encryptedfile = f.encrypt(data)

with open ('encryptedfile.txt', 'wb') as file:
    file.write(encryptedfile)