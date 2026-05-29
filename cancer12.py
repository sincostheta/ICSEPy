# importing libraries
import matplotlib.pyplot as plt
# x and y arrays
x = [1.5, 2.6, 3.5, 4, 9]
y = [3.25, 6.3, 4.23, 1.35, 3]
# plotting + output
plt.plot(x, y, linestyle='--', marker='*')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()