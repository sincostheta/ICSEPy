# importing libs
import numpy as np
from scipy import stats
# initialising list
l = np.array([89, 91, 62, 95, 93, 72, 86, 67, 82, 73])
# output: mean, median and mode
print("The mean of the marks are: ", np.mean(l))
print("The median of the marks are: ", np.median(l))
print("The mode of the marks are: ", stats.mode(l))