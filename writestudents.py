

name = input("Write a name: ")
home = input("Write a home: ")

name_and_home = f"{name},{home}\n"

with open("students.csv", "a") as file:
    file.write(name_and_home)
    print(f"Added {name} from {home}.")

    