import matplotlib.pyplot as plt
stud_prep=[]
stud_group=[]
stud_grade=[]
with open('students.csv') as file:
    stud_info = file.readlines()
for i in range(len(stud_info)):


  a=stud_info[i].find(';')
  stud_prep.append(str(stud_info[i][:a]))
  stud_info[i]=stud_info[i][a+1:]

  b=stud_info[i].find(';')
  stud_group.append(str(stud_info[i][:b]))
  stud_info[i]=stud_info[i][b+1:]

  stud_grade.append(int(stud_info[i]))


# Marks per prep
k=1
prep=sorted(set(stud_prep))

plt.figure(figsize=(10, 6))
plt.suptitle("Marks per prep")
grades=sorted(set(stud_grade))
for i in range(len(prep)):
  grades_new=[]
  counter=[]
  sizes=[]
  for j in range(len(stud_grade)):
    if stud_prep[j]==prep[i]:
      counter.append(stud_grade[j])
  for p in range(len(grades)):
    if (counter.count(grades[p])!=0):
      sizes.append((counter.count(grades[p])/len(counter))*100)
      grades_new.append(grades[p])
  ax=plt.subplot(len(prep)//2,len(prep)//2 + len(prep)%2,k)
  ax=plt.pie(sizes, labels = grades_new)
  k+=1
plt.show()
plt.savefig('Эпизод 3 Marks per prep')

# Marks per group
k=1
group=sorted(set(stud_group))

plt.figure(figsize=(10, 5))
plt.suptitle("Marks per group")
grades=sorted(set(stud_grade))
for i in range(len(group)):
  grades_new=[]
  counter=[]
  sizes=[]
  for j in range(len(stud_grade)):
    if stud_group[j]==group[i]:
      counter.append(stud_grade[j])
  for p in range(len(grades)):
    if (counter.count(grades[p])!=0):
      sizes.append((counter.count(grades[p])/len(counter))*100)
      grades_new.append(grades[p])
  ax=plt.subplot(len(prep)//2,len(prep)//2 + len(prep)%2,k)
  ax=plt.pie(sizes, labels = grades_new)
  k+=1
plt.show()
plt.savefig('Эпизод 3 Marks per group')
