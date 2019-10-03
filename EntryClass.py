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
        self.decrypt_list = []

    def fix(self):
        self.vars = '::~~::~~::'.join([self.name, self.username, self.email, self.password, self.pin])
        return self

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

        f = Fernet(self.get_key(self.big_pass))

        with open('dat//txt.passwords', 'ab') as file:
            file.write(f.encrypt(secret))
            file.write(b'\n')
        return self

    def get_list_of_entries(self):
        file = open('dat//txt.passwords', 'rb')
        encrypted = file.readlines()
        for num, write in enumerate(encrypted):
            f = Fernet(Entry.get_key(self.big_pass))
            decrypt = f.decrypt(write).decode('utf-8')
            decrypt = decrypt.split('::~~::~~::')
            self.decrypt_list.append(decrypt)
            print(f"{num}) {decrypt[0]}")
        choice = input('Which account would you like to view? ')
        while not choice.isdigit():
            choice = input('Which account would you like to view? ')
        choice = int(choice)
        account = self.decrypt_list[choice]
        print(f'\n\nName of account:      {account[0]}')
        print(f'Username of account:  {account[1]}')
        print(f'Email for account:    {account[2]}')
        print(f'Password of account:  {account[3]}')
        print(f'PIN for account:      {account[4]}\n\n')


