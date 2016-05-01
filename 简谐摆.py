import pylab as py

t=[0]
x=[0]
v=[0.2]
dt=0.001
n=100000

for i in range(n):
    t.append(dt+t[-1])
    x.append(x[-1]+v[-1]*dt)
    v.append(v[-1]-(x[-1]**1)*dt)

py.plot(t,x)
py.show()