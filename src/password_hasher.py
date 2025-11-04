# Hash passwords securely with Argon2 - strong protection for user accounts!

from icecream import ic
from passlib.hash import argon2

hashed = argon2.hash("strongpass123")

ic(argon2.verify("strongpass123", hashed))  # True
ic(argon2.verify("wrongpass", hashed))  # False
