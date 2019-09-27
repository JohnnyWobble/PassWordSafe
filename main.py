import hashlib
from passlib.context import CryptContext

import setup
import talk

hasher = hashlib.sha3_256()

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)



def login():
    password = input('Password: ')
    hasher.update(password.encode())
    if setup.check_pass(hasher.hexdigest()):
        talk.encrypt_or_decrypt(password)
    else:
        quit('Bad Password!')

login()