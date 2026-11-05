import numpy as np


number = np.array(
    [
        [2,5,4],
        [5,6,8],
        [10,20,50],
        [65,75,85]
    ]
)
additionMatrix = number + 5
subractionMatrix =  number - 3

print("Original Matrix====>",number)
print("Additon Matrix====>",additionMatrix)
print("Subraction Matrix====>",subractionMatrix)

