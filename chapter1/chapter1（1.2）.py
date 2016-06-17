import pylab as py

t=[0]
x=[0]
v=40
dt=0.1
n=100

for i in range(n):
    t.append(dt+t[-1])
    x.append(x[-1]+v*dt)
    

py.plot(t,x)
py.show()