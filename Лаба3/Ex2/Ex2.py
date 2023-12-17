import numpy as np
import matplotlib.pyplot as plt
k=1
for i in range(3):
    f=open(f'signal0{i+1}.dat')
    num=[]
    new=[]
    for j in f:
        num.append(float(j))
        
    fig, ax = plt.subplots()
    num=np.array(num)
    x = np.linspace(0, len(num),len(num))
    
    plt.subplot(3,2,k)
    plt.plot(x, num)
    plt.grid()
    plt.title("Сырой сигнал " + str(i+1))
    k+=1
    for j in range(len(num)):
        if j<9:
            new.append(np.mean(num[:j+1]))
        else:
            new.append(np.mean(num[j-9:j+1]))
        x = np.linspace(0, len(new),len(new))
    plt.subplot(3,2,k)
    plt.plot(x, new)
    plt.grid()
    plt.title("После фильтра")
    k+=1
plt.savefig('Эпизод 2')
plt.show()
