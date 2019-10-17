import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Entry:
    def __init__(self, name: str = None, username: str = None, email: str = None, password: str = None, pin: str = None, big_pass: str = None):
        """
        init method for Entry (duh), it gets called without params when you just need to access some of the unrelated
        methods (e.i. static methods) for viewing the accounts

        :param name: str
        :param username: str
        :param email: str
        :param password: str
        :param pin: str
        :param big_pass: str
        """
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.pin = pin
        self.big_pass = big_pass  # User's password to the safe
        self.decrypt_list = []
        self.data_list = [self.name, self.username, self.email, self.password, self.pin]

    def ready_for_write(self):
        """
        Joins data with an identifier (::~~::~~::) to separate later

        :return: self
        """
        self.vars = '::~~::~~::'.join(self.data_list)
        return self

    @staticmethod
    def get_key(password):
        """
        Gets the key needed to decrypt the stored data

        :param password: str
        :return: bytes
        """
        password = password.encode()
        salt = b'*\x1e\xd5\\-\x99x\xc9\xc5{\xaa\xfa\xaa\n\x19\xf3'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
        return key

    def add(self):
        """
        Writes newline to the txt.passwords file so it can differentiate between entries

        :return: self
        """
        secret = self.vars.encode()

        f = Fernet(self.get_key(self.big_pass))

        with open('src//tmp//txt.passwords', 'ab') as file:
            file.write(f.encrypt(secret))
            file.write(b'\n')
        return self

    def print_entries(self, edit: bool = False, delete: bool = False) -> int:
        """
        Asks the user which entry they want to print, and prints it, for editing it returns the index of the account
        they wanted so it can be edited later

        :return: self
        """
        word = 'view'
        if edit:  # makes sure to use the correct word where necessary
            word = 'edit'
        elif delete:
            word = 'delete'
        choice = input(f'Which account would you like to {word} (ctrl+c to cancel)? ')

        while not choice.isdigit():  # only allow valid inputs (int)
            choice = input(f'Which account would you like to {word} (ctrl+c to cancel)? ')
        choice = int(choice)
        account = self.decrypt_list[choice]
        print('\n')
        print(f'Name of account:      {account[0]}')
        print(f'Username of account:  {account[1]}')
        print(f'Email for account:    {account[2]}')
        print(f'Password of account:  {account[3]}')
        print(f'PIN for account:      {account[4]}')
        print('\n')
        return choice

    def get_list_of_entries(self, edit: bool = False, delete: bool = False) -> int:
        """
        Accesses the data stored on txt.passwords, and sorts it to be printed, then asks the user which one they want to
        see

        :return: self
        """
        f = Fernet(Entry.get_key(self.big_pass))

        with open('src//tmp//txt.passwords', 'rb') as file:
            encrypted = file.readlines()

        for num, write in enumerate(encrypted):  # iterates through data to sort it

            decrypt = f.decrypt(write).decode('utf-8')
            decrypt = decrypt.split('::~~::~~::')  # splits data by type

            self.decrypt_list.append(decrypt)
            print(f"{num}) {decrypt[0]}")  # print the different accounts
        pick_line = self.print_entries(edit=edit, delete=delete)  # prints data for the account, and asks user which one they want

        return pick_line  # pick_line is the index of the account they want

    def edit_line(self, line: int, info_entry):
        """
        Encrypts the data that the user wants to edit, then over-writes the existing data in the appropriate location on
        to txt.passwords

        :param line: int
        :param info_entry: Entry
        :return: Entry
        """
        self.ready_for_write()  # organizes data from self.vars
        for num, data in enumerate(info_entry.decrypt_list[line]):
            if self.data_list[num].isspace() or self.data_list[num] == "":
                self.data_list[num] = data
            elif self.data_list[num] == ".":  # clear the entry if it is just a period
                self.data_list[num] = " "
        self.ready_for_write()

        f = Fernet(self.get_key(self.big_pass))  # generates encryption key

        # Gets the current data on txt.passwords
        with open('src//tmp/txt.passwords', 'rb') as file:
            file_lines = file.readlines()

        # encrypts and adds the line to the list of lines going to be written
        line_to_write = f.encrypt(self.vars.encode())
        file_lines[line] = line_to_write + b'\n'

        with open('src//tmp/txt.passwords', 'wb') as file:  # Writes lines
            file.writelines(file_lines)
        return self

    def delete_entry(self, entry_line: int):
        """
        It will write back the data but without the entry that was specified to be deleted

        :param entry_line: int
        :return: None
        """
        while True:  # takes only valid input
            y_n = input("Are you absolutely sure [Y/N]? ").upper()
            if y_n == "N":
                raise KeyboardInterrupt  # goes back to main menu
            elif y_n == "Y":
                break

        with open("src//tmp//txt.passwords", "w") as f:  # clears data so the new stuff can be appended with .add()
            f.write("")

        self.decrypt_list.pop(entry_line)
        for entry in self.decrypt_list:
            self.data_list = entry
            self.ready_for_write()
            self.add()
