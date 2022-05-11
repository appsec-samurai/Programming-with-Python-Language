# Author: KEDAR BHARTIYA[appsec-samurai]
# Problem Statement: Ways to find length of list

# Solution 1:
"""Naive Method"""

inputList = [1, 4, 5, 7, 8]

# Printing the list
print("The list is : " + str(inputList))

# Finding length of list using loop
# Initializing counter
counter = 0
for i in inputList:
    # incrementing counter
    counter = counter + 1

# Printing length of list
print("Length of list using naive method is : " + str(counter))

# Solution 2:
"""Using len() Method"""

inputList = []
inputList.append("Hello")
inputList.append("I")
inputList.append("Am")
inputList.append("Kedar")
print("The length of list is: ", len(inputList))

# Solution 3:
"""Using length_hint() Method"""

from operator import length_hint

# Initializing list
inputList = [1, 4, 5, 7, 8]

# Printing test_list
print("The list is : " + str(inputList))

# Finding length of list using length_hint()
list_len_hint = length_hint(inputList)

# Printing length of list
print("Length of list using length_hint() is : " + str(list_len_hint))
