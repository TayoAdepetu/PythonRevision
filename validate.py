import re

email = input("What's your email? ").strip()

# username, domain = email.split("@")

# if username.isalnum() and domain.isalnum():
#     print("Valid email")

# if username and "." in domain and domain.endswith(".com"):
#     print("Valid email")


# if re.search(r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$", email):
#     print("Valid email")

if re.search(r"^\w+@(\w\.)?\w+\.(edu|com|ng|net)$", email):
    print("Valid email")

else:
    print("Invalid email")
