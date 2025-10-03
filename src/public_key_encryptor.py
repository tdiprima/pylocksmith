# Easy public-key encryption - send secret messages that only the right person can read!

from nacl.public import Box, PrivateKey

# Generate keys for sender
sender_sk = PrivateKey.generate()
sender_pk = sender_sk.public_key

# Generate keys for recipient
recipient_sk = PrivateKey.generate()
recipient_pk = recipient_sk.public_key

# Create a Box for encryption (sender's private + recipient's public)
box = Box(sender_sk, recipient_pk)
encrypted = box.encrypt(b"Secret greeting")

# Decrypt using recipient's Box (recipient's private + sender's public)
recipient_box = Box(recipient_sk, sender_pk)
decrypted = recipient_box.decrypt(encrypted)
print(decrypted.decode())  # Outputs: Secret greeting
