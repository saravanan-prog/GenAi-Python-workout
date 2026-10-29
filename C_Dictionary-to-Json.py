import json

# dictionary 

teacherRecord = {
    "name" : "Mahit",
    "age" : 28,
    "specification" : "Python instructor"
}

print("Teacher Name ====>",teacherRecord['name'])
print("Teacher Age ====>",teacherRecord['age'])
print("Teacher specify area ====>",teacherRecord['specification'])

# convert dictionary to Json

teacherRecord = json.dumps(teacherRecord)

print("2 Teacher Name ====>",teacherRecord['name'])
print("2 Teacher Age ====>",teacherRecord['age'])
print("2 Teacher specify area ====>",teacherRecord['specification'])



