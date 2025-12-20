# pylocksmith 🔐 🐍
## Security Libraries We Love

### 1. `python-decouple` 🌿

**What it does:** Keeps secrets *outta your code*.  
Instead of hard-coding API keys or passwords, you toss them in a `.env` file, and `decouple` cleanly loads them.  
→ Think: ".env whisperer" — super useful for keeping your repo squeaky clean & not leaking creds.

### 2. `itsdangerous` 💥

**What it does:** Signs data so you can tell if it's been tampered with.  
You give it a value (like a token), it gives you back a signed version. Later, you can check if that value's still legit.  
→ Flask uses this under the hood for secure cookies 👀.

### 3. `bandit` 🕵️‍♂️

**What it does:** Scans your code for common security oopsies.  
Like "hey, you accidentally left `eval()` here," or "this password handling looks sus."  
→ Basically a static analysis security guard that never sleeps.

### 4. `secure` 🛡️

**What it does:** Makes security headers easy-peasy for web apps.  
You can quickly set things like `Content-Security-Policy`, `X-Frame-Options`, etc. without memorizing the RFC jungle.  
→ Think of it as "best practice headers on autopilot."

### 5. `pycryptodome` 🔐

**What it does:** Gives you all the low-level crypto building blocks.  
AES, RSA, hashing, random number generation — all the classics.  
→ Kinda like the Swiss Army knife of cryptography if you wanna build secure systems yourself.

### 6. `pynacl` 🧂

**What it does:** Wraps the **NaCl (salt)** crypto library for Python.  
Gives you high-level, modern cryptography — like public-key encryption, digital signatures, secure messaging — without needing a PhD to use it.  
→ More "modern crypto toolkit" than `pycryptodome`, and it's battle-tested.

### 7. `passlib` 🔑

**What it does:** Makes password hashing stupid simple.  
You can hash, verify, and upgrade password storage securely. Supports bcrypt, scrypt, argon2, etc.  
→ Basically "don't roll your own password system," this library's got you.

### 8. `python-gnupg` ✉️

**What it does:** Lets you use **GPG/PGP encryption** from Python.  
Encrypt files, sign messages, manage keys — all using the GnuPG backend.  
→ Think: "old school, super-trusty email/file encryption but automated through Python."

---

## More Scripts
- `secure_message_encryption.py`: Fernet symmetric encryption/decryption.
- `secure_password_hashing_passlib.py`: Bcrypt password hashing/verification.
- `generate_secure_token.py`: Cryptographically secure URL-safe tokens.
- `argon2_password_hashing.py`: Argon2 password hashing/verification.
- `create_expiring_tokens.py`: Signed, time-limited tokens.
- `jwt_token_handling.py`: JWT creation and verification.
- `security_code_scan_bandit.py`: Static analysis scan with vuln demo.
- `certificate_handling.py`: Generate and parse self-signed cert.
- `vault_secrets_client.py`: HashiCorp Vault client initialization.
- `environment_secrets_loader.py`: Load/override secrets from .env.

<br>
