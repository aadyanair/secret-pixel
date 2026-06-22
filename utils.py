import base64
import hashlib
from cryptography.fernet import Fernet


def text_to_binary(message):
    binary = ''.join(format(ord(char), '08b') for char in message)
    return binary


def binary_to_text(binary_data):
    chars = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))
    return ''.join(chars)


def generate_key_from_password(password):
    hashed_password = hashlib.sha256(password.encode()).digest()
    key = base64.urlsafe_b64encode(hashed_password)
    return key


def encrypt_message(message, password):
    key = generate_key_from_password(password)
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message.decode()


def decrypt_message(encrypted_message, password):
    try:
        key = generate_key_from_password(password)
        fernet = Fernet(key)
        decrypted_message = fernet.decrypt(encrypted_message.encode())
        return decrypted_message.decode()
    except Exception:
        return None