# Hash passwords securely with Argon2 - strong protection for user accounts!

from passlib.hash import argon2

hashed = argon2.hash("strongpass123")
print(argon2.verify("strongpass123", hashed))  # True
print(argon2.verify("wrongpass", hashed))  # False
