import matplotlib.pyplot as plt
arr = ['001.dat','002.dat','003.dat','004.dat','005.dat']

for i in range(len(arr)):
    f=open(arr[i])
    X=[]
    Y=[]
    for j in range(int(f.readline())):
        x,y = f.readline().split()
        X.append(float(x))
        Y.append(float(y))
    
    w1=sorted(X)
    w2=sorted(Y)
  
    q1=[]
    q2=[]
    for s in range(len(X)-1):
      #print(w1[s], w1[s+1], abs(w1[s]-w1[s+1]))
      if (abs(w1[s]-w1[s+1])!=0):
        q1.append(abs(w1[s]-w1[s+1]))
      if (abs(w2[s]-w2[s+1])!=0):
        q2.append(abs(w2[s]-w2[s+1]))
  
    m1=min(q1)
    m2=min(q2)
    m=min(m1,m2) * 2

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.scatter(X,Y,s=m)
    plt.title('Number of points: ' + str(len(X)))
    plt.axis('scaled')
    plt.show()
    plt.savefig('Эпизод 1'+ 'Number of points: ' + str(len(X)))


