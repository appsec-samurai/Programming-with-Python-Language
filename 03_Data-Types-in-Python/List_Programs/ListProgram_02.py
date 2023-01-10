# Author: KEDAR BHARTIYA[appsec-samurai]
# Problem Statement: Python program to swap two elements as per given positions

# Solution 1:
"""Simple swap, using comma assignment"""

def swapElements(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]

    return list

# Driver code
inputList = [10, 20, 30, 40, 50]
pos1, pos2 = 1, 3
print("List before swapping first & last elements", inputList)
print("List after swapping first & last elements", swapElements(inputList, pos1-1, pos2-1))

# Solution 1:
"""Using tuple variable"""


def swapElements(list, pos1, pos2):
    get = list[pos1], list[pos2]

    # unpacking those elements
    list[pos2], list[pos1] = get

    return list


# Driver Code
inputList = [23, 65, 19, 90]
pos1, pos2 = 2, 4
print("List before swapping first & last elements", inputList)
print("List after swapping first & last elements", swapElements(inputList, pos1-1, pos2-1))