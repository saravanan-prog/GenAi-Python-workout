# A dictionary in Python stores data in key-value pairs.

student = {
    "name": "Ravi",
    "age": 20,
    "mark": 85
}

print("student name ====>", student['name'])
print("student age ====>",  student['age'])
print("student mark ====>", student['mark'])

student["name"]     = "Sunil"                             # update
student["address"]  = "2nd cross st, maharashtra"         # create
del student["age"]                                        # delete

print("student  ====>", student)
