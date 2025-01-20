import re

name = input("What's your name? ").strip()

#find if there is any commas in the name and reduce space between the comma and the first name
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    #if there is a comma, split the name into last and first
    # last, first = matches.groups()
    # name = f"{first} {last}"
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello {name}!")