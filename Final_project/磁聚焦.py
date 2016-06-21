import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def phase(r):
    x=[0]
    y=[0]
    z=[0]
    dxdt=[100]
    dydt=[0]
    dzdt=[r]
    t=[0]
    dt=0.0001
    for i in range(499999):
        dxdt.append(dxdt[-1])
        dydt.append(dydt[-1]+dzdt[-1]*dt)
        dzdt.append(dzdt[-1]-dydt[-1]*dt)
        x.append(x[-1]+dxdt[-1]*dt)
        y.append(y[-1]+dydt[-1]*dt)
        z.append(z[-1]+dzdt[-1]*dt)
        t.append(t[-1]+dt)
    return x,y,z
ka=phase(1)
ax.plot(ka[0], ka[1], ka[2])
ka=phase(2)
ax.plot(ka[0], ka[1], ka[2])
ka=phase(3)
ax.plot(ka[0], ka[1], ka[2])
ax.set_title('magnetic focusing')
ax.set_xlabel('z')
ax.set_ylabel('x')
ax.set_zlable('y')
plt.show()
