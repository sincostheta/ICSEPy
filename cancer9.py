# importing libraries
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
# image link
img = io.imread("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTssX-T1caQ6G8TJ4RWmx6GcqOtwAOPCIq2Jw&s")
l = np.array(img)
# output
print("The dtype of the numpy array is: ", type(l))
print("The shape of the resulting array of the image is: ", l.shape)