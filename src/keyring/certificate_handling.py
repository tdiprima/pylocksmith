"""
Generates a self-signed X.509 certificate, dumps to PEM, reloads and inspects it.
Demonstrates low-level SSL/TLS cert handling with pyOpenSSL.
"""

from OpenSSL import crypto

# Generate private key
private_key = crypto.PKey()
private_key.generate_key(crypto.TYPE_RSA, 2048)

# Create self-signed cert
cert = crypto.X509()
cert.get_subject().CN = "example.secureapp.com"
cert.get_subject().O = "Secure App Inc"
cert.set_serial_number(12345)
cert.gmtime_adj_notBefore(0)
cert.gmtime_adj_notAfter(365 * 24 * 60 * 60)  # 1 year
cert.set_issuer(cert.get_subject())
cert.set_pubkey(private_key)
cert.sign(private_key, "sha256")

# Dump to PEM string
cert_pem = crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode()
key_pem = crypto.dump_privatekey(crypto.FILETYPE_PEM, private_key).decode()

# Load back from PEM
loaded_cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_pem)

print("Certificate Common Name (CN):", loaded_cert.get_subject().CN)
print("Issuer:", loaded_cert.get_issuer().CN)
print("Cert PEM preview:\n", cert_pem[:200], "...")
