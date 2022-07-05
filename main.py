#Generating a key for the file
from cryptography.fernet import Fernet
key = Fernet.generate_key()

with open('saved_key.key','wb') as file:
    file.write(key)
