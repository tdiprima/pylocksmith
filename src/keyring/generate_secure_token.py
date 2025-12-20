"""
Generates cryptographically secure, URL-safe random tokens using secrets module.
Suitable for API keys, session IDs, reset tokens.
"""

import secrets

# Generate 32-byte URL-safe token
secure_token = secrets.token_urlsafe(32)

print("Generated secure token:", secure_token)
print("Length:", len(secure_token))
