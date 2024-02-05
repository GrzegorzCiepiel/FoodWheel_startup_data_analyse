import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
import matplotlib.pyplot as pt

restaurants = pd.read_csv('restaurants.csv')
print(restaurants.head())

#How many different types of cuisine FoodWheel offers
# and how many different restaurants serve that type of cuisine.

rest_unique = restaurants.cuisine.unique( )
cuisine_counts = restaurants.groupby('cuisine').name.count()
print(cuisine_counts)

#Create a pie chart that shows the different types of cuisines available on FoodWheel.

plt.figure()
plt.pie(cuisine_counts,
        colors=sns.color_palette('Set2'),
        explode=[0.03, 0.03, 0.03, 0.09, 0.09, 0.09, 0.09],
        autopct='%1.2f%%',
        labels = rest_unique)
plt.axis('equal')
plt.show()
plt.clf()

orders = pd.read_csv('orders.csv')
# print(orders.head())
# Group the orders data by month.
orders['month'] = orders.date.apply(lambda x: x.split('-')[0])
print(orders.head())
print('\n')
print(orders.groupby('month').price.sum())
print(orders.groupby('month').price.mean())
std_order = orders.groupby('month').price.std()
print(std_order)