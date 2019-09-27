import hashlib
import os


from EntryClass import Entry

h = hashlib.sha3_256()


def check_pass(hashp):
    if os.path.exists('dat//test.txt'):
        with open('dat//passhash.txt', 'r') as f:
            pass_hash = f.read()
        return hashp == pass_hash
    else:
        tamper_proof()



def get_info(big_pass):
    print("Just hit enter if you don't want to fill out the field")
    name = input('Name of account: ')
    if name is '':
        name = None

    username = input('Username of account: ')
    if username is '':
        username = None

    email = input('Email for account: ')
    if email is '':
        email = None

    password = input('Password for account: ')
    if password is '':
        password = None

    pin = input('PIN of account: ')
    if pin is '':
        pin = None
    return Entry(name=name, username=username, email=email, password=password, pin=pin, )


def tamper_proof():
    if os.path.exists('dat//test.txt'):
        with open('dat//passhash.txt', 'w') as f:
            f.write('')
    if os.path.exists('dat//dat.txt'):
        with open('dat//dat.txt', 'w') as f:
            f.write('')
    quit('Data wiped! The password was deleted')