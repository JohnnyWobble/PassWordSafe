import hashlib
import os


from EntryClass import Entry

h = hashlib.sha256()


def check_pass(hashed_password):
    """
    Checks if the password is valid by comparing its hash to the stored one

    :param hashed_password: bytes
    :return: bool
    """
    if os.path.exists('dat//txt.passwords') and os.path.exists('dat//passhash.txt'):
        with open('dat//passhash.txt', 'r') as f:
            pass_hash = f.read()
        return hashed_password == pass_hash
    else:
        tamper_proof()


def add_space(string):
    """
    Adds a space to the string to make comprehension easier

    :param string: str
    :return: str
    """
    if string == '':
        string += ' '
    return string


def get_info(big_pass):
    """
    Has a dialog with the user to get the data that will be stored

    :param big_pass: str
    :return: Entry
    """
    print("Just hit enter if you don't want to fill out the field")
    name = add_space(input('Name of account: '))
    username = add_space(input('Username of account: '))
    email = add_space(input('Email for account: '))
    password = add_space(input('Password for account: '))
    pin = add_space(input('PIN of account: '))
    return Entry(name=name, username=username, email=email, password=password, pin=pin, big_pass=big_pass)


def tamper_proof():
    """
    If the password file is wiped then it deletes all of the data

    :return: None
    """
    with open('dat//passhash.txt', 'w') as f:
        f.write('')
    with open('dat//txt.passwords', 'w') as f:
        f.write('')
    quit('Data wiped! The password was deleted')