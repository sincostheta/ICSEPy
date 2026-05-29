# initialising numpy
import numpy as np
# initialising list
l = np.arange(1, 13)
# printing shape, reshaping + printing
print("Size of the matrix is: ", l.shape)
l = l.reshape(3, 4)
for i in l:
    print(i)