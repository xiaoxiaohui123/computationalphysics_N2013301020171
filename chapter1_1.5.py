import pylab as py

t=[0]
N_A=[100]
N_B=[0]
dt=0.001
n=10000

for i in range(n):
    t.append(dt+t[-1])
    N_A.append(N_A[-1]+(N_B[-1]-N_A[-1])*dt)
    N_B.append(N_B[-1]+(N_A[-1]-N_B[-1])*dt)

py.plot(t,N_A)
py.plot(t,N_B)
py.show()