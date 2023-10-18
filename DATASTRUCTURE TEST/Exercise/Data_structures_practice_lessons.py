
# NUMBER ONE
import math
# Allowing the user input their own degree value
degrees = float(input('Enter value in degrees: '))

# printing out the results of the degrees input
print(math.radians(degrees))


# NUMBER TWO
# CALCULATING AREA OF A PARALLELOGRAM
# Creating the empty list so ican add the numbers the user input
numbers = []

# allowing the user input the values
user_input = float(input("Please input the height of the parallelogram: "))
user_input2 = float(input("please input the length of the base: "))

# adding the userinput to the list
numbers.append(user_input)
numbers.append(user_input2)

print("The area of the parallelogram is ", math.prod(numbers))

# NUMBER THREE
n = int(input("please input any values so you can get its smallest multiple:"))
factors = list(range(1, n+1))
smallest_multiple = math.prod(factors)

print(factors)
print(f"The smallest multiple of {n} values",smallest_multiple)

# NUMBER FOUR

import numpy as np

arr = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
num = 3.1

print("Original array:")
print(arr)
print("Checking for complex number:")
print(np.iscomplex(arr))
print("Checking for real number:")
print(np.isreal(arr))
print("Checking for scalar type:")
print(np.isscalar(num))

# NUMBER FIVE


arr = np.array([1, 7, 13, 105])
print("Original array:")
print(arr)
print("Size of the memory occupied by the said array:")
print(f"{arr.size * arr.itemsize} bytes")









