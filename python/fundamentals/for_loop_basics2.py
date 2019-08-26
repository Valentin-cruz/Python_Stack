# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def biggie_size(arr):
    for x in range(len(arr)):
        if arr[x] > 0:
            arr[x] = "Big"
        return arr

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
def count_postive(arr):
    count = 0
    for x in range(len(arr)):
        if arr[x] > 0:
            count = count + 1
    arr[len(arr-1)] = count
    return arr

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
def sum_total(arr):
    sum = 0
    for x in range(len(arr)):
        sum = sum + arr[x]
    return sum

# Average - Create a function that takes a list and returns the average of all the values.
def average(arr):
    sum = 0
    for x in range(len(arr)):
        sum = sum + arr[x]
    return sum/len(arr)

# Length - Create a function that takes a list and returns the length of the list.
def length(arr):
    count = 0
    for x in range(len(arr)):
        count = count + 1
    return count

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def minimum(arr):
    min = 0
    if len(arr) == 0:
        return False
    for x in range(len(arr)):
        if arr[x] < min:
            min = arr[x]
    return min

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
def maximum(arr):
    max = 0
    if len(arr) == 0:
        return False
    for x in range(len(arr)):
        if arr[x] > max:
            max = arr[x]
    return max

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis(arr):
    newdic = {}
    sum = 0
    average = 0
    sumtotal = 0
    min = 0
    max = 0

    for x in range(len(arr)):
        sumtotal = sumtotal + arr[x]
        return sumtotal

    for x in range(len(arr)):
        sum = sum + arr[x]
        average = sum/len(arr)
        return average

    if len(arr) == 0:
        return False
    for x in range(len(arr)):
        if arr[x] < min:
            min = arr[x]
        return min

    if len(arr) == 0:
        return False
    for x in range(len(arr)):
        if arr[x] > max:
            max = arr[x]
        return max
    newdic = {max, min, average, sumtotal}
    return newdic

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
def reverse_list(arr):
    return arr[::-1]
print(reverse_list([37,2,1,-9]))