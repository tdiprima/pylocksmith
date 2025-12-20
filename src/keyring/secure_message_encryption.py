"""
Demonstrates secure symmetric encryption and decryption using Fernet (AES + HMAC).
Generates key, encrypts/decrypts sensitive data, prints results.
"""

from cryptography.fernet import Fernet

# Generate a new key (in practice, store securely)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Sample sensitive data
original_message = b"Sensitive user credentials: abc123@secure.app"

# Encrypt
encrypted_data = cipher_suite.encrypt(original_message)

# Decrypt
decrypted_data = cipher_suite.decrypt(encrypted_data)

print("Original:", original_message.decode())
print("Decrypted:", decrypted_data.decode())
print("Encryption successful:", original_message == decrypted_data)
