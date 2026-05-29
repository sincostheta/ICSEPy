import matplotlib.pyplot as plt
x = ["Pen", "Eraser", "Sharpener", "Ruler", "Compass"]
y1 = [10, 5, 5, 10, 50]
y2 = [20, 10, 10, 20, 100]
plt.title("Selling Price v. Original Price")
plt.plot(x, y1, linestyle='solid', color='tomato', label='Original Price')
plt.plot(x, y2, linestyle='solid', color='steelblue', label='Selling Price')
plt.legend()
plt.show()