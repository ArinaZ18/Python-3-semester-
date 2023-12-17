import pandas as pd

data = pd.read_csv("pandas2.csv")

data['COUNT'] = 1
data = data.drop(['Unnamed: 0'], axis=1)

data.groupby('CARGO').sum().plot.bar(subplots=True, figsize=(20, 20), grid=True)
plt.savefig('ex2_bar.png')
data.groupby('CARGO').sum().plot.pie(subplots=True, figsize=(20, 20))
plt.savefig('ex2_pie.png')
