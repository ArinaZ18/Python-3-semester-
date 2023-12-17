import pandas as pd

data_html = pd.read_html("results_ejudge.html")[0]
data_excel = pd.read_excel("students_info.xlsx")


data = data_excel.merge(data_html, left_on='login', right_on='User')
plt.figure(figsize=(16, 8))
plt.subplot(121)
data.groupby('group_faculty')['Solved'].mean().plot.bar(grid=True,title="по факультетским группам")
plt.subplot(122)
data.groupby('group_out')['Solved'].mean().plot.bar(grid=True,title="по группам по информатике")
plt.suptitle("Среднее количество решённых задач")
plt.savefig('ex3_1.png')
