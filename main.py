#!/usr/bin/env python3
import hashlib
import os
from passlib.context import CryptContext

import setup
import talk

hasher = hashlib.sha256()

# pwd_context = CryptContext(
#         schemes=["pbkdf2_sha256"],
#         default="pbkdf2_sha256",
#         pbkdf2_sha256__default_rounds=30000
# )


def login():
    password = input('Password: ')
    hasher.update(password.encode())
    if setup.check_pass(hasher.hexdigest()):
        talk.encrypt_or_decrypt(password)
    else:
        quit('Bad Password!')


def login_or_generate():

    if os.path.exists('dat//passhash.txt'):
        ofile = open('dat//passhash.txt', 'r')
        if ofile.read() == '':
            ofile.close()
            new_file = open('dat//passhash.txt', 'w')
            talk.generate(new_file)
        else:
            ofile.close()
            login()
    else:
        file = open('dat//passhash.txt', 'w')
        talk.generate(file)


login_or_generate()
