greeting = "hello world!"
age = "Twenty One"
newage = 23
newgreeting = greeting.strip()
newgreeting = greeting.capitalize()
newgreeting = greeting.title()
print(f"Another way for variables, {newgreeting} {age} {newage}")
firstname, lastname = newgreeting.split(" ")

print(f"First Name: {firstname} Last Name: {lastname}")

for i in [0,1,2,3,4]:
    print(f"Count {i}")

for i in range(5):
    print(f"Range Count {i}")

for _ in range(5):
    print(f"Unknown Range Count {_}")

print("meow\n"*3)

print("meow\n"*3, end="")

