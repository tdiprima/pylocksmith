# GPG encryption made easy - protect your messages!
# Note: You'll need GPG installed and the recipient's key.

import gnupg

gpg = gnupg.GPG()
encrypted_data = gpg.encrypt("Private note", "teamlead@example.com")
print(str(encrypted_data))
