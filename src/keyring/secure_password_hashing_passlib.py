"""
Shows proper password hashing with passlib using bcrypt.
Hashes a password and verifies it (and a wrong one).
Requires: pip install passlib[bcrypt]
TODO: In production, use proper error handling and secure password input.
"""

import sys

from passlib.context import CryptContext

try:
    pwd_hasher = CryptContext(schemes=["bcrypt"], deprecated="auto")

    password = "MySecurePass2024!@#"

    # Hash
    hashed_password = pwd_hasher.hash(password)

    # Verify correct
    is_valid = pwd_hasher.verify(password, hashed_password)
    print(f"Valid password matches: {is_valid}")

    # Verify incorrect
    is_invalid = pwd_hasher.verify("wrongpass", hashed_password)
    print(f"Invalid password rejected: {is_invalid}")
except Exception:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print("\nType:", exc_type)
    print("\nErr:", exc_obj)
    print("\nLine:", exc_tb.tb_lineno)
    sys.exit(1)
