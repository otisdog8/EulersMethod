import cexprtk
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
import numpy as np

expression = input("Enter your expression: ")

iterations = int(input("How many steps? "))
interval = float(input("How large of an interval? "))
x = float(input("Initial X coord? "))
y = float(input("Initial Y coord? "))
st = cexprtk.Symbol_Table({'x' : x, 'y' : y, "e" : np.e}, add_constants= True)
derivative = cexprtk.Expression(expression, st)
points = []
for i in range(iterations + 1):
    dval = derivative()
    print("X value:", x, "Y value:", y, "derivative", dval)
    points.append((x, y))
    x = x + interval
    y = y + interval * dval
    st.variables['x'] = x
    st.variables['y'] = y

plt.scatter(*zip(*points))
plt.show()
