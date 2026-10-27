def printName(candidatename):
    print("Hello " + candidatename)

# printName("Saravanan")


def arithmeticOperation(firstnumber,secondNumber):
    return firstnumber + secondNumber

#arithmeticResult = arithmeticOperation(100,100)
#print("Arithmetic Result ===>",arithmeticResult)


def printEventNumbers(rangeNumber):
    eventList = []
    for item in range(1,rangeNumber):
        if(item % 2 == 0):
            eventList.append(item)
    return eventList


#evenListResult = printEventNumbers(101)
#print("Event lsit ===>",evenListResult)


def findOddNumbers(rangeNumber):
    oddNumberList = []
    for item in range(1,rangeNumber):
        if(item % 2 != 0):
            oddNumberList.append(item)
    return oddNumberList

#result = findOddNumbers(101)
#print("ODD Result ====>",result)

        
