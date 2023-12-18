import pandas as pd

data_html = pd.read_html("results_ejudge.html")[0]
data_excel = pd.read_excel("students_info.xlsx")


data = data_excel.merge(data_html, left_on='login', right_on='User')
plt.figure(figsize=(16, 8))
plt.subplot(121)
data.groupby('group_faculty')['Solved'].mean().plot.bar(xlabel='',grid=True,title="по факультетским группам")
plt.subplot(122)
data.groupby('group_out')['Solved'].mean().plot.bar(xlabel='',grid=True,title="по группам по информатике")
plt.suptitle("Среднее количество решённых задач")
plt.savefig('ex3_1.png')


plt.figure(figsize=(16, 8))
sol2=(data[(data['H']>=10) | (data['G']>=10)])
plt.subplot(121)
sol2['group_faculty'].value_counts().plot.pie(ylabel='', title='Факультетские группы из которых пришли студенты')
plt.subplot(122)
sol2['group_out'].value_counts().plot.pie(ylabel='',title='Группы по информатике, в которые они попали')
plt.savefig('ex3_2.png')
