list = [100,200,600,800,100,20,50,45]

maxValue = max(list)
minValue = min(list)

list.remove(maxValue)   # remove first max value
maxValue = max(list)    # after you will get second max value




print("maxValue value is",maxValue)
