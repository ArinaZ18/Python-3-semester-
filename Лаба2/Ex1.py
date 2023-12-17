import pandas as pd

wine_reviews = pd.read_csv("pandas1.csv")
# wine_reviews.shape #1000 строк 5 столбца 
wine_reviews
# wine_reviews.head()

sol1=(wine_reviews[wine_reviews['STATUS']=="OK"].sort_values(by='SUM', ascending=False)).iloc[0:3]

sol2=(wine_reviews[(wine_reviews['STATUS']=="OK") & (wine_reviews['CONTRACTOR']=="Umbrella, Inc")]).sum()

print('Ex1:\n')
print(sol1['SUM'],'\n')
print('Ex2: ', sol2['SUM'])
