import os

user = os.environ.get("SECRET_USER")
password = os.environ.get("SECRET_PASS")

print ([user, password])