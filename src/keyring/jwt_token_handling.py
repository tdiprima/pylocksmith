"""
Creates and verifies JSON Web Tokens (JWTs) with expiration.
Enforces HS256 algorithm and expiry validation.
"""

from datetime import datetime, timedelta, timezone

import jwt

jwt_secret = "my_jwt_secret_key_2025_change_me"

payload = {
    "user_id": 100,
    "role": "admin",
    # "exp": datetime.utcnow() + timedelta(minutes=30)
    "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
}

# Encode
token = jwt.encode(payload, jwt_secret, algorithm="HS256")

# Decode/verify
decoded_payload = jwt.decode(token, jwt_secret, algorithms=["HS256"])

print("Decoded payload:", decoded_payload)
print("Token valid and expired check passed.")
