"""
Demonstrates Bandit static security scanner.
Creates a sample vulnerable file with eval(), runs scan, prints issues.
"""

import os
import subprocess
import tempfile

# Create temp vulnerable code
vuln_code = """
def risky_func(user_input):
    return eval(user_input)  # B101: Very insecure!

print(risky_func('2+2'))
"""

with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
    f.write(vuln_code)
    vuln_file = f.name

try:
    # Run bandit on the vuln file
    result = subprocess.run(
        ["bandit", "-r", os.path.dirname(vuln_file)],
        capture_output=True,
        text=True,
        timeout=10,
    )
    print("Bandit scan results:")
    print(result.stdout)
    if result.stderr:
        print("Warnings:", result.stderr)
finally:
    os.unlink(vuln_file)
