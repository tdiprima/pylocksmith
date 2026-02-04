"""
Initializes HashiCorp Vault client and demonstrates basic properties/ops.
In production, use real token/URL; here shows auth status and readiness.
TODO: Integrate with actual secret read/write operations.
"""

import sys

import hvac

try:
    vault_url = "http://127.0.0.1:8200"  # Local Vault example
    client = hvac.Client(url=vault_url, token="hvs.testtoken123")  # nosec B105 Dummy token for demo

    print(f"Vault URL: {client.url}")
    print(f"Authenticated: {client.is_authenticated()}")
    print(f"Vault sealed: {client.sealed}")
except Exception:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print("\nType:", exc_type)
    print("\nErr:", exc_obj)
    print("\nLine:", exc_tb.tb_lineno)
    sys.exit(1)

# Example secret read (fails gracefully if no Vault)
try:
    response = client.secrets.kv.v2.read_secret_version(path="myapp/db")
    print("Sample secret data:", response.get("data", {}).get("data", "No data"))
except Exception as e:
    print(f"Expected error without Vault server: {e}")
