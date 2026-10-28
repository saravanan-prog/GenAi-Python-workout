def getEvenNumbers(inputRange):
    list = [
        item
        for item in range(1,inputRange)
        if(item %2 == 0)
    ]

    return list
    