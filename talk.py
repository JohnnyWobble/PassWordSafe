import os
import EntryClass
import hashlib

import setup


hasher = hashlib.sha256()


def encrypt_or_decrypt(password):
    """
    Dialog tha asks if they want to add or view the passwords. This is the event loop that just keeps iterating until
    the program ends

    :param password: str
    :return: None
    """
    while True:  # event loop
        while True:
            choice = input("Do you want to [v]iew passwords or [a]dd one?").upper()  # takes the input
            if choice in ['V', 'A']:
                break
        if choice == 'A':  # add passwords
            new_entry = setup.get_info(password)
            new_entry.fix().add()
        elif choice == 'V':  # view passwords
            get_list = EntryClass.Entry(big_pass=password)
            get_list.get_list_of_entries()

# Encryption of files


def generate(password_file):
    """
    Wipes the data and then asks user for the password they want, hashes it and writes it to passhash.txt

    :param password_file:
    :return:
    """
    with open('dat//txt.passwords', 'w') as f:  # wipe data file
        f.write('')

    # generates hash
    password = input("What do you want your password to be? ")
    hasher.update(password.encode())
    password_file.write(hasher.hexdigest())

    print('Ok, password set! Now try and login.')
    password_file.close()
    return None

