import hashlib
from os import system, name, path

from EntryClass import Entry


h = hashlib.sha256()


def salt(password):
    """
    Adds a salt to the beginning and end of the password to deter dehashing it with a brute force method or with a hash
    library

    :param password: str
    :return: str
    """
    pass


def check_pass(hashed_password: str) -> bool:
    """
    Checks if the password is valid by comparing its hash to the stored one

    :param hashed_password: bytes
    :return: bool
    """
    if path.exists('dat//txt.passwords') and path.exists('dat//passhash.txt'):
        with open('dat//passhash.txt', 'r') as f:
            pass_hash = f.read()
        return hashed_password == pass_hash
    else:
        tamper_proof()


def add_space(string: str) -> str:
    """
    Adds a space to the string to make comprehension easier

    :param string: str
    :return: str
    """
    if string == '':
        string += ' '
    return string


def get_info(big_pass: str, edit: bool = False) -> Entry:
    """
    Has a dialog with the user to get the data that will be stored

    :param big_pass: str
    :param edit: bool
    :return: Entry
    """
    if edit:
        print("Leave the field blank if you don't want to edit it")
    else:
        print("Just hit enter if you don't want to fill out the field")
    name = add_space(input('Name of account: '))
    username = add_space(input('Username of account: '))
    email = add_space(input('Email for account: '))
    password = add_space(input('Password for account: '))
    pin = add_space(input('PIN of account: '))
    return Entry(name=name, username=username, email=email, password=password, pin=pin, big_pass=big_pass)


def tamper_proof():
    """
    Called if the password file is wiped then it deletes all of the stored data

    :return: None
    """
    with open('dat//passhash.txt', 'w') as f:
        f.write('')
    with open('dat//txt.passwords', 'w') as f:
        f.write('')
    quit('Data wiped! The password was deleted')


def clear():  # clear output function
    """
    Clears the terminal windows, note: does not work on the PyCharm run windows it just prints a weird character

    :return: None
    """
    # for windows
    if name == 'nt':
        system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')