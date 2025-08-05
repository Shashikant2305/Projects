# --- logic.py ---
# Cryptographic functions: key generation, encryption, decryption

import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32,
        salt=salt, iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(file_path: str, password: str) -> None:
    salt = os.urandom(16)
    key = generate_key(password, salt)
    fernet = Fernet(key)

    with open(file_path, 'rb') as f:
        data = f.read()

    encrypted = fernet.encrypt(data)
    with open(file_path, 'wb') as f:
        f.write(salt + encrypted)

def decrypt_file(file_path: str, password: str) -> bool:
    with open(file_path, 'rb') as f:
        data = f.read()

    salt = data[:16]
    encrypted = data[16:]
    key = generate_key(password, salt)

    try:
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted)
        with open(file_path, 'wb') as f:
            f.write(decrypted)
        return True
    except:
        return False
