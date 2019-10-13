from src import EntryClass
from src import setup


def encrypt_or_decrypt(password):
    """
    Dialog tha asks if they want to add or view the passwords. This is the event loop that just keeps iterating until
    the program ends

    :param password: str
    :return: None
    """
    while True:  # event loop
        try:
            while True:  # input loop
                choice = input("\nDo you want to [v]iew entries, [e]dit entries, [a]dd one, or [exit]? ").upper()  # takes the input
                if choice in ['V', 'A', 'E', 'EXIT']:  # if it is a valid choice
                    break
            setup.clear()
            if choice == 'A':  # add accounts
                new_entry = setup.get_info(password)  # this creates an Entry
                new_entry.fix().add()

            elif choice == 'V':  # view accounts
                existing_entry = EntryClass.Entry(big_pass=password)
                existing_entry.get_list_of_entries()

            elif choice == 'E':  # editing accounts
                edit_entry = EntryClass.Entry(big_pass=password)  # Entry that contains data about account (pre-edit)
                line = edit_entry.get_list_of_entries(edit=True)
                editee_entry = setup.get_info(password, edit=True)  # Entry that collects information to be printed
                editee_entry.big_pass = password
                editee_entry.edit_line(line, edit_entry)

            elif choice == 'EXIT':  # ends program
                setup.clear()
                quit('Bye')
        except KeyboardInterrupt:
            print('\n\n')
            continue  # allows user to cancel their action by hitting ctrl+c


def generate(password_file):  # Encryption of files
    """
    Wipes the data and then asks user for the password they want, hashes it and writes it to passhash.txt

    :param password_file:
    :return:
    """
    with open('src//tmp//txt.passwords', 'w') as f:  # wipe data file
        f.write('')

    # generates hash
    password = input("What do you want your password to be? ")
    password_file.write(setup.salt_hash(password))

    print('Ok, password set! Now try and login.')
    password_file.close()
    return None
