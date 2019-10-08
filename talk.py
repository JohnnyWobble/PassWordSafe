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
            choice = input("Do you want to [v]iew entries, [e]dit entries, [a]dd one, or [exit]? ").upper()  # takes the input
            if choice in ['V', 'A', 'E', 'EXIT']:
                break
        if choice == 'A':  # add passwords
            new_entry = setup.get_info(password)  # this creates an Entry
            new_entry.fix().add()
        elif choice == 'V':  # view passwords
            existing_entry = EntryClass.Entry(big_pass=password)
            existing_entry.get_list_of_entries()
        elif choice == 'E':
            edit_entry = EntryClass.Entry(big_pass=password)
            line = edit_entry.get_list_of_entries(edit=True)
            editee_entry = setup.get_info(password, edit=True)
            editee_entry.big_pass = password
            editee_entry.edit_line(line)
        elif choice == 'EXIT':
            setup.clear()
            quit('Bye')


def generate(password_file):  # Encryption of files
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

