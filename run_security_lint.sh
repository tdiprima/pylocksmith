# This script installs bandit and runs it to lint your Python project for security issues,
# such as weak hashing or potential injection vulnerabilities.

pip install bandit
bandit -r path/to/your_project/