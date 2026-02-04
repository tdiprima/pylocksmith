# Use PyJWT when implementing secure authentication with JSON Web Tokens, ensuring tokens are signed and validated to prevent forgery.

import datetime

import jwt

SECRET_KEY = "super_secure_key"  # nosec B105


def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def validate_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return "Token has expired!"
    except jwt.InvalidTokenError:
        return "Invalid token provided!"


if __name__ == "__main__":
    token = generate_token(456)
    print("Generated Token:", token)
    result = validate_token(token)
    print("Validation Result:", result)
