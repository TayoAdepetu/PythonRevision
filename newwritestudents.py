import csv

# method 2
name = input("Write a name: ")
home = input("Write a home: ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

# method 3
name = input("Write a name: ")
home = input("Write a home: ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name":name, "home": home})
