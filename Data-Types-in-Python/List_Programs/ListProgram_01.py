# Author: KEDAR BHARTIYA[appsec-samurai]
# Problem Statement: Python program to interchange first and last elements in a list

# Solution 1:
"""Find the length of the list and simply swap the first element with (n-1)th element."""

def swapElements(inputList):
    size = len(inputList)

    temp = inputList[0]
    inputList[0] = inputList[size-1]
    inputList[size-1] = temp

    return inputList

# Driver code
inputList = [10, 20, 30, 40, 50]
print("List before swapping first & last elements", inputList)
print("List after swapping first & last elements", swapElements(inputList))

# Solution 2:
"""Swap list[0] with list[-1]"""

def swapElements(inputList):
    inputList[0], inputList[-1] = inputList[-1], inputList[0]

    return inputList

# Driver code
inputList = [10, 20, 30, 40, 50]
print("List before swapping first & last elements", inputList)
print("List after swapping first & last elements", swapElements(inputList))

# Solution 3:
"""Swap the first and last element is using tuple variable and unpack those elements with first and last element 
in that list."""

def swapElements(inputList):
    get = inputList[-1], inputList[0]

    # unpacking those elements
    inputList[0], inputList[-1] = get

    return inputList


# Driver code
inputList = [10, 20, 30, 40, 50]
print("List before swapping first & last elements", inputList)
print("List after swapping first & last elements", swapElements(inputList))

# Solution 4:
"""By using pop, insert, append inbuilt functions of list"""


def swapElements(inputList):
    first = inputList.pop(0)
    last = inputList.pop(-1)

    inputList.insert(0, last)
    inputList.append(first)

    return inputList

# Driver code
inputList = [10, 20, 30, 40, 50]
print("List before swapping first & last elements", inputList)
print("List after swapping first & last elements", swapElements(inputList))
