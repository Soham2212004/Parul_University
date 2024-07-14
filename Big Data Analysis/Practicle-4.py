students_list = [
{"roll_number": 1, "name": "Soham", "date_of_birth": "22-01-2004","address":"Vadodara"},
{"roll_number": 2, "name": "Dev", "date_of_birth": "14-10-2002","address":"Dubai"},
{"roll_number": 3, "name": "Raju", "date_of_birth": "22-10-2050","address":"Gujarat"}
]

print(students_list[1]["name"])

students_set = {
"Soham",
"Dev",
"Raju"
}
if "Dev" in students_set:
    print("Dev is in the set")

students_dict = {
    1: {"name": "Soham", "date_of_birth": "22-01-2004", "address": "Vadodara"},
    2: {"name": "Dev", "date_of_birth": "14-10-2003", "address": "Dubai"},
    3: {"name": "Raju", "date_of_birth": "22-10-2050", "address": "Gujarat"}
}

print(students_dict[1]["address"]) 


# task-2
students = [
 {"name": "Soham", "age": 21},
 {"name": "Dev", "age": 20},
 {"name": "Raju", "age": 23},
]
# Create a set of unique student names
student_names = set([student["name"] for student in students])
# Create a map of student names to their ages
student_ages = {student["name"]: student["age"] for student in students}
# Print the student list
print("Student List:")
for student in students:
    print(student)
# Print the set of student names
print("\nStudent Names:")
for name in student_names:
    print(name)
# Print the map of student names to their ages
print("\nStudent Ages:")
for name, age in student_ages.items():
    print(f"{name}: {age}")



