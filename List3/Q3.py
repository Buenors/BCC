import matplotlib.pyplot as plt
import numpy as np
a=-17
b=-17
x = np.arange(0, 10)
y=a*x+b
plt.plot(x, y)
X = 5
Y=a*X+b
plt.plot(X,Y,'o')
print("%d reais"% Y)