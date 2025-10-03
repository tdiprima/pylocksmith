# Load secrets from .env files - keep your API keys safe!

from decouple import config

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)

# Example usage: Print the loaded values
print(f"Secret Key: {SECRET_KEY}")
print(f"Debug Mode: {DEBUG}")
