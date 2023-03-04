import os
from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a secure random key for encryption and decryption.
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the previously generated key for encryption and decryption.
    """
    return open("key.key", "rb").read()

def encrypt_message(message):
    """
    Encrypts a message using the Fernet encryption algorithm.
    """
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message using the Fernet encryption algorithm.
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Test
generate_key()

# Get user input for the message to encrypt
message = input("Enter a message to encrypt (by Kiki#4469): ")

encrypted_message = encrypt_message(message)
print(f"Encrypted message: {encrypted_message}")
decrypted_message = decrypt_message(encrypted_message)
print(f"Decrypted message: {decrypted_message}")
