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
    """
    Login sequence for the user, if it is the right password they can continue, else it will quit the program

    :return: None
    """
    password = input('Password: ')
    hasher.update(password.encode())
    if setup.check_pass(hasher.hexdigest()):
        talk.encrypt_or_decrypt(password)
    else:
        quit('Bad Password!')


def login_or_generate():
    """
    Reads passhash.txt and if it has a hash in it then it assumes that the user want to login, if it doesn't exist or it
    is empty, than it creates a new profile for the user

    :return: None
    """
    if os.path.exists('dat//passhash.txt'):
        file_read_only = open('dat//passhash.txt', 'r')
        if file_read_only.read() == '':
            file_read_only.close()
            new_file = open('dat//passhash.txt', 'w')
            talk.generate(new_file)
        else:
            file_read_only.close()
            login()
    else:
        write_file = open('dat//passhash.txt', 'w')
        talk.generate(write_file)


login_or_generate()
