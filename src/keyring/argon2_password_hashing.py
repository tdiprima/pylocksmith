"""
Implements state-of-the-art Argon2 password hashing and verification.
Memory-hard for resistance to GPU attacks.
"""

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

hasher = PasswordHasher()

passphrase = "CorrectHorseBatteryStaple2024"

# Hash
hash_value = hasher.hash(passphrase)

# Verify correct
valid = hasher.verify(hash_value, passphrase)
print(f"Correct passphrase verified: {valid}")

# Verify wrong
try:
    invalid = hasher.verify(hash_value, "wrongphrase")
except VerifyMismatchError as e:
    print("Wrong passphrase rejected.")
    print(e)
