import os
import EntryClass


import setup


def encrypt_or_decrypt(password):
    while True:
        while True:
            choice = input("Do you want to [v]iew passwords or [a]dd one?").upper()
            if choice in ['V', 'A']:
                break
        if choice == 'A':
            new_entry = setup.get_info(password)
            new_entry.fix()
            new_entry.add()
        else:
            EntryClass.Entry.get_list_of_entries(password)
# Encryption of files
