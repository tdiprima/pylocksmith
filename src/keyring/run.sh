#!/bin/bash

echo "argon2_password_hashing"
uv run argon2_password_hashing.py
echo

echo "certificate_handling"
uv run certificate_handling.py
echo

echo "create_expiring_tokens"
uv run create_expiring_tokens.py
echo

echo "environment_secrets_loader"
uv run environment_secrets_loader.py
echo

echo "generate_secure_token"
uv run generate_secure_token.py
echo

echo "jwt_token_handling"
uv run jwt_token_handling.py
echo

echo "secure_message_encryption"
uv run secure_message_encryption.py
echo

echo "secure_password_hashing_passlib"
uv run secure_password_hashing_passlib.py
echo

echo "security_code_scan_bandit"
uv run security_code_scan_bandit.py
echo

echo "vault_secrets_client"
uv run vault_secrets_client.py
echo
