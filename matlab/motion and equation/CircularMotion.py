from matplotlib import pyplot as plt
import numpy as np
import math


# p: Center of an object position
# r: Radius
# T: Frequency

gAngle = 0.0

def getCircularMotionX(p, r, T):
    x = np.arange(0.01, 10.0, 0.01)
    Angles = gAngle + T * x;
    y = p + r * np.cos(Angles)

    return x, y

def getCircularMotionZ(p, r, T):
    x = np.arange(0.01, 10.0, 0.01)
    Angles = gAngle + T * x;
    y = p + r * np.sin(Angles)

    return x, y

x,y = getCircularMotionX(10.0, 15.0, 2.0)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('X Motion')
plt.show()

x,y = getCircularMotionZ(0.0, 15.0, 2.0)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Z Motion')
plt.show()
