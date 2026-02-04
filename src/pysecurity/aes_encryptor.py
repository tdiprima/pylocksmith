# Simple AES encryption example - keeps your messages safe and secure!

import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from icecream import ic

key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)
nonce = os.urandom(12)
ciphertext = aesgcm.encrypt(nonce, b"Confidential report", None)

# For completeness: Decrypt to verify
plaintext = aesgcm.decrypt(nonce, ciphertext, None)
ic(plaintext.decode())  # Outputs: Confidential report
