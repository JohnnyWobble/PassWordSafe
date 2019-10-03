from cryptography.fernet import Fernet

import EntryClass



file = open('dat//txt.passwords', 'rb')
encrypted = file.readlines()[0]
print([encrypted])
print(EntryClass.Entry.get_key('cool'))
f = Fernet(EntryClass.Entry.get_key('cool'))
decrypted = f.decrypt(encrypted)
print(decrypted)
print(decrypted.decode('utf-8'))