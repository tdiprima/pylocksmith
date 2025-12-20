"""
Creates and verifies time-limited, signed tokens without database storage.
Uses URLSafeTimedSerializer for stateless sessions/verification.
"""

from itsdangerous import URLSafeTimedSerializer

secret_key = "my_app_secret_key_change_in_prod_2024"

serializer = URLSafeTimedSerializer(secret_key)

user_session = "user:100:session_active"

# Create token (expires in 30 min)
token = serializer.dumps(user_session)

# Verify (valid)
decoded_data = serializer.loads(token, max_age=1800)
print("Decoded session data:", decoded_data)

# TODO: Simulate expired (will raise SignatureExpired after time)
# serializer.loads(token, max_age=0)  # Uncomment to test expiry
