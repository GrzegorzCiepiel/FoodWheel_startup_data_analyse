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
plt.title('Different types of cuisines available on FoodWheel')
plt.savefig('pie.png')
plt.show()
plt.clf()

orders = pd.read_csv('orders.csv')
# print(orders.head())
# Group the orders data by month.
orders['month'] = orders.date.apply(lambda x: x.split('-')[0])
print(orders.head())
print('\n')
print(orders.groupby('month').price.sum().reset_index())
mean_orders = orders.groupby('month').price.mean().reset_index()
std_order = orders.groupby('month').price.std().reset_index()
print(std_order)

plt.figure()
ax = plt.subplot()
plt.bar(range(len(mean_orders)), mean_orders.price,
        yerr=std_order.price,
        capsize=5,
        color='purple'
        )
ax.set_xticks(range(len(mean_orders)))
ax.set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September'])
plt.ylabel('Average Order Amount')
plt.title('Average Order Amount Over Time')
plt.savefig('bar1.png')
plt.show()
plt.clf()

customer_amount = orders.groupby('customer_id').price.sum().reset_index()

print(customer_amount)
plt.figure()
plt.hist(customer_amount.price, bins=40, range=(0, 200))
plt.xlabel('Total Spent')
plt.ylabel('Number of Customers')
plt.title("Each client's expenses")
plt.savefig('hist.png')
plt.show()
plt.clf()

#Create a visualization to display the restaurant count for each neighborhood.

restaurant_count = restaurants.groupby('neighborhood').name.count().reset_index()
print(restaurant_count)


plt.figure()
ax = plt.subplot()
plt.bar(restaurant_count.neighborhood, restaurant_count.name)
ax.set_xticks(range(7))
ax.set_xticklabels(restaurant_count.neighborhood, rotation=30)
plt.ylabel('Restaurant Count', fontsize=10)
plt.title('Neighborhood by Restaurant Count', fontsize=12)
plt.savefig('bar2.png')
plt.show()
plt.clf()