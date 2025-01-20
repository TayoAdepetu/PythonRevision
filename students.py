import csv

students = []

# method 1

with open("students.csv") as file:
    reader = csv.reader(file)
    for name,home in reader:
        students.append({"name": name, "home": home})


for student in students:
    print(f"{student['name']} is from {student['home']}.")


