import csv

students = []

# method 2
with open("newstudents.csv") as file:
    # return each line as a dictionary
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})


for student in students:
    print(f"{student['name']} is from {student['home']}.")
