# Print the 1 to 100 numbers

def printNumbers():
    for item in range(1,101):
        print("item====>",item)


#printNumbers()

def printTheEvenNumbers():
    for item in range(1,101):
       if (item % 2 == 0):
          print("Event item===>",item)


#printTheEvenNumbers()

def printODDNumbers():
    for item in range(1,101):
       if (item % 2 != 0):
          print("ODD item===>",item)

#printODDNumbers()