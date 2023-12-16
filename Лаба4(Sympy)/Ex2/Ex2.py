import scipy as sci
import numpy as np
import matplotlib.pyplot as plt

f=open("ex2.dat")
N=int(f.readline())

A=[]
for i in range(N):
    A.append(f.readline().split( ))

A=np.array(A, dtype=np.float64)
b=np.array(f.readline().split(),dtype=np.float64)

x = linalg.solve(A, b)
y=np.linspace(1,len(b),len(b))

plt.bar(y,x)
plt.grid()
plt.savefig('Эпизод2_2.png')
