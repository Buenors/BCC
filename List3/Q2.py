import matplotlib.pyplot as plt
import numpy as np
x=int(input("Número de dias "))
a = -1
b = 9
c = 3
y=a*x**2+b*x+c
plt.plot(x, y, 'o')
print(y, "reais")