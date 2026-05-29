# importing numpy
import numpy as np
# intializing lits
l1 = np.arange(1, 17)
l2 = np.arange(1, 12)
# concatenating and splitting + output
l3 = np.concatenate([l1, l2])
print(l3)
print(np.split(l3, 3))