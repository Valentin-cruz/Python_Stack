# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(num):
    for x in range(num, 0,-1):
        print (x)

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return(arr):
    print (arr[0])
    return arr[1]

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first_plus_length(arr):
    return arr[0] + len(arr)

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def values_greater_than_second(arr):
    newarr = []
    if len(arr) < 2:
        return False
    for x in arr:
        if arr[x] > arr[1]:
            newarr.append(arr[x])
    print(newarr)
    print(len(newarr))

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def length_value(a,b):
    newarr = []
    for x in range(0,a):
        newarr.append(b)
    return newarr
