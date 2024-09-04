import matplotlib.pyplot as plt
import numpy as np
a=-5
b=10
c=17
x = np.arange(0, 11)
y=a*x**2+b*x+c
plt.plot(x,y)
X = 6
Y=a*X**2+b*X+c
plt.plot(X,Y,'o')
plt.show() 
print("%d reais"% Y)