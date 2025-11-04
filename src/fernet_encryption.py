# Use Fernet when you need to securely encrypt and decrypt sensitive data like API tokens or user information using symmetric encryption.

from cryptography.fernet import Fernet
from icecream import ic

# Generate a secure key (keep this safe, perhaps in an env variable)
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

# Encrypt confidential information
encrypted_data = cipher_suite.encrypt(b"Confidential message here")
ic(encrypted_data)

# Decrypt the information
decrypted_data = cipher_suite.decrypt(encrypted_data)
ic(decrypted_data)
