import base64
from cryptography.fernet import Fernet


def generate_key(keystring) -> bytes:
    key = bytes(keystring, "UTF-8", )
    
    if len(key) < 32:
        key += b'\x00' * (32 - len(key))
    elif len(key) > 32:
        key = key[:32]

    return base64.urlsafe_b64encode(key)


def encrypt(key, filepath):
    '''
    Encrypts text file.
    '''
    key = generate_key(key)
    fernet = Fernet(key)
    with open(filepath, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    
    with open(filepath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt(key, filepath):
    '''
    Decrypts text file.
    '''
    key = generate_key(key)
    fernet = Fernet(key)
    with open(filepath, 'rb') as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    
    with open(filepath, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)


def decp(key, filepath):
    '''
    Decrypts text file and print it to teminal
    '''
    key = generate_key(key)
    fernet = Fernet(key)
    with open(filepath, 'rb') as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    
    with open(filepath, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    
    print(decrypted.decode("utf-8"))


