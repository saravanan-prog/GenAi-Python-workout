import json

student = '{"studentName":"saravanan", "studentAge":28, "course":"Angular"}'  # json


print("Json data ====>",student)

student = json.loads(student)     # convert json to dictionary

print("student name ====>",student['studentName'])
print("student Age ====>",student['studentAge'])
print("student Course ====>",student['course'])