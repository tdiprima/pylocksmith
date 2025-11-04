# Use Hashids when you need to obscure integer IDs in URLs or public-facing data to prevent enumeration attacks, without full encryption.

from hashids import Hashids

hashids_instance = Hashids(salt="secret_salt_value", min_length=6)
hashed_id = hashids_instance.encode(456)
unhashed_id = hashids_instance.decode(hashed_id)
print(hashed_id)  # e.g., 'aBcD3eF'
print(unhashed_id)  # (456,)
