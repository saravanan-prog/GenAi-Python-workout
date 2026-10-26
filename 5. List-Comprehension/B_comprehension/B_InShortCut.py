list = [ 10,20,40,22,55,885,96,5]

newList = [ 
    number + 100 
    for number in list
]

evenNumbers = [
    number
    for number in list
    if  number % 2 == 0
]

oddNumberlist = [
    number
    for number in list
    if number % 2 != 0
]


print("Original List ====>",list) 
print("New List ====>",newList) 
print("Even Numbers List ====>",evenNumbers) 
print("ODD Numbers List ====>",oddNumberlist) 