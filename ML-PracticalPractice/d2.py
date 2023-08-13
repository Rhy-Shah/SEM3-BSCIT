import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10)
y = np.arange(11,21)

a = np.arange(40,50)
b = np.arange(50,60)
y=x*x
plt.scatter(x,y,c='red')

plt.plot(x,y,'r--')
plt.show() 

x = np.arange(0,5*np.pi,0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.subplot(2,1,1)
plt.plot(x,y_sin)
plt.title('Sine')
plt.subplot(2,1,2)
plt.plot(x,y_cos)
plt.title('Cos')
plt.show()