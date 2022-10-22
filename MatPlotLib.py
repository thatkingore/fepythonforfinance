# Using Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Plotting a line y=mx by using lists

plt.plot([1, 2, 3, 4, 5])
plt.show()

# Plotting (x,y) by using lists, defining axes, colours, and shapes (patterns)

plt.plot([1, 2, 3, 4, 5], [1, 3, 5, 9, 35], 'ro')
plt.axis([0, 6, 0, 40])
plt.show()

# Plotting multiple variations of (t) by defining colours and shapes (patterns)

t = np.arange(100, 300, 10)
plt.plot(t, t, 'g--', t, t**3, 'r^')
plt.show()

# Plotting (x,y,z) by defining x, y, and z

x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]
plt.plot(x,y)
plt.plot(x,z)
plt.title("Test")
plt.xlabel("x-axis")
plt.ylabel("y-axis and z-axis")
plt.legend(["this is y", "this is z"])
plt.show()

# Plotting categorical data by defining 'names' and 'values'

names = ["AMZN", "AAPL", "GOOGL"]
values = [1734.7, 262.1, 1301.4]

plt.figure(figsize=(9,3))
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting (Closing Share Price of Companies)')
plt.show()

# Plotting a box chart

data = pd.read_csv("S_P500Companies.csv")
print(data.head())

data.Day3.plot(kind="box")
plt.show()
