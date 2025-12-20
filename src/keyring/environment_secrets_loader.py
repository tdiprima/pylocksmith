"""
Loads secrets from .env file using python-dotenv, with override.
Creates demo .env, shows before/after values.
"""

import os

from dotenv import load_dotenv

# Simulate existing env var
os.environ["API_KEY"] = "exposed_in_code_bad_practice"

# Create demo .env
env_content = "API_KEY=sk-prod-securekey2024_xyz\nDATABASE_URL=postgres://secure\n"
with open(".env", "w") as f:
    f.write(env_content)

print("Before load - API_KEY:", os.getenv("API_KEY"))

# Load and override
load_dotenv(override=True)

print("After load - API_KEY:", os.getenv("API_KEY"))
print("DATABASE_URL:", os.getenv("DATABASE_URL"))

# Cleanup
os.unlink(".env")
