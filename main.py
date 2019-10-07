#!/usr/bin/env python3
import hashlib
from os import system, name, path

import setup
import talk


hasher = hashlib.sha256()


# clear output function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def login():
    """
    Login sequence for the user, if it is the right password they can continue, else it will quit the program

    :return: None
    """
    password = input('Password: ')
    clear()
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
    if path.exists('dat//passhash.txt'):
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
