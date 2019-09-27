import os
import EntryClass
import hashlib


import setup

hasher = hashlib.sha256()


def encrypt_or_decrypt(password):
    while True:
        while True:
            choice = input("Do you want to [v]iew passwords or [a]dd one?").upper()
            if choice in ['V', 'A']:
                break
        if choice == 'A':
            new_entry = setup.get_info(password)
            new_entry.fix().add()
        else:
            get_list = EntryClass.Entry(big_pass=password)
            get_list.get_list_of_entries()

# Encryption of files


def generate(pfile):
    with open('dat//dat.txt', 'w') as f:
        f.write('')
    password = input("What do you want your password to be? ")
    hasher.update(password.encode())
    pfile.write(hasher.hexdigest())
    print('Ok, password set! Now try and login.')
    pfile.close()
    return