# importing numpy
import numpy as np
# initialising list and asking user for element
l = np.array([21, 19, 67, 42, 12, 14, 15, 63, 71, 31])
print(l)
a = int(input("Enter the element whose index number you want to find: "))
# finding the index number + printing
f = np.where(l == a)
print(f"Index of {a} is: ", f[0][0])