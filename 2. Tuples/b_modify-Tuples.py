# A tuple in Python is used to store multiple values in a single variable.
# A tuple is similar to a list, but a tuple cannot be modified after it is created.

fruits = ("Apple", "Banana", "Mango")
list = list(fruits)
list.append("lichi")
list.append("grapes")
fruits = tuple(list)

print("fruits   ===>",fruits)