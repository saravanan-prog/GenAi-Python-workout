def filterOddNumber(number):
   
    oddNumber = [
        item
        for item in range(number)
        if(item %2 == 0)
    ]

    return  oddNumber

print(filterOddNumber(100))
