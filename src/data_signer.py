# Sign your data to prevent tampering - like secure tokens but simpler!

from itsdangerous import URLSafeSerializer

s = URLSafeSerializer("app-secure-key")
token = s.dumps({"user": "dany"})
print(token)  # Outputs a signed token like eyJ1c2VyIjoiY2hhcmxpZSJ9...

# Verify and load the data
loaded_data = s.loads(token)
print(loaded_data)  # {'user': 'dany'}
