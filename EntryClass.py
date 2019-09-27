import random
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Entry:
    def __init__(self, name=None, username=None, email=None, password=None, pin=None, big_pass=None):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.pin = pin
        self.big_pass = big_pass

    def fix(self):
        list_vars = []
        for letter, var in [['n', self.name], ['u', self.username], ['e', self.email], ['p', self.password], ['i', self.pin]]:
            if var is not None:
                list_vars.append(''.join([letter, var]))
        # random.shuffle(list_vars)
        self.vars = '\n'.join(list_vars)
        print('fix done')

    @staticmethod
    def start():
        """
        Gets the hash for the user's password

        :return: str
        """
        password = bytes(input("What do you want you password to be? "))
        return password

    @staticmethod
    def get_key(password):
        password = password.encode()
        salt = b'*\x1e\xd5\\-\x99x\xc9\xc5{\xaa\xfa\xaa\n\x19\xf3'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
        return key

    def add(self):
        secret = self.vars.encode()

        print(self.get_key(self.big_pass))
        f = Fernet(self.get_key(self.big_pass))

        with open('dat//dat.txt', 'ab') as file:
            file.write(f.encrypt(secret))
            file.write(b'\n')

    @staticmethod
    def get_list_of_entries(password):
        file = open('dat//dat.txt', 'rb')
        encrypted = file.readlines()
        for write in encrypted:
            f = Fernet(Entry.get_key(password))
            decrypt = f.decrypt(write).decode('utf-8')
            decrypt.split('\n')
            print(decrypt[0][1:])


