# Simple AES encryption example - keeps your messages safe and secure!

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)
cipher = AES.new(key, AES.MODE_GCM)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(b"Confidential report")

# For completeness: Decrypt to verify
decrypt_cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
plaintext = decrypt_cipher.decrypt_and_verify(ciphertext, tag)
print(plaintext.decode())  # Outputs: Confidential report
