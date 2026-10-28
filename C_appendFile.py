with open("notes.txt","a") as file:
    file.write("\nHii welcome to python world\n")


with open("notes.txt","r") as file:
    data = file.read()

print(data)

