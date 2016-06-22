from __future__ import division
from pylab import *

# define the positions of z, r is variable
def phase(r):
    x=[1]
    y=[0]
    z=[0]
    dxdt=[100]
    dydt=[0]
    dzdt=[r]
    t=[0]
    dt=0.0001
#   qBm=1
    for i in range(499999):
        dxdt.append(dxdt[-1])
        dydt.append(dydt[-1]+dzdt[-1]*dt)
        dzdt.append(dzdt[-1]-dydt[-1]*dt)
        x.append(x[-1]+dxdt[-1]*dt)
        y.append(y[-1]+dydt[-1]*dt)
        z.append(z[-1]+dzdt[-1]*dt)
        t.append(t[-1]+dt)
    return x,y,z

figure()
plot(phase(1)[0],phase(1)[2])
plot(phase(2)[0],phase(2)[2])
plot(phase(3)[0],phase(3)[2])
title('Phase space plot: magnetic focusing in x-z plane')
xlabel('z')
ylabel('x')

show()