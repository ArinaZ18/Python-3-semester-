import matplotlib.pyplot as plt
import numpy as np
X=[]
Y=[]
k=1
with open('frames.dat') as file:
    storage = file.readlines()

plt.figure(figsize=(20, 20))

a=0
b=0

for i in range(0,len(storage),2):
    X=[]
    Y=[]
    X=storage[i].split(' ')
    X=list(map(float,X))

    Y = storage[i+1].split(' ')
    Y = list(map(float, Y))

    plt.subplot(3,2,k)
    plt.plot(X,Y)
    plt.title('Frame ' + str(k))
    plt.grid()
    plt.xlim(0,16)
    plt.ylim(-12,12)
    k+=1

plt.savefig('Эпизод 2')
