import pandas as pd

ds = pd.read_csv("purchases.csv")

# the total price of a purchase order
total_price = ds[ds["Purchase Order Number"] == "018H2015"]

# name and description of a purchased item
name_description_item = ds[ds["Purchase Order Number"] == "3176273"]
name = name_description_item['Item Name']
description = name_description_item['Item Description']

# ammount of accasions during 2013
year_2013 = ds[ds['Purchase Date'].str.find('2013') >= 0] # 34024 occasions

# five common departments
b=5
most_department = ds['Department Name'].value_counts().index.tolist()[:b]


# three departments using most money

most_money =  ds.nlargest(3, 'Total Price')
most_money_department = most_money['Department Name']

# sorting
sort_department = ds['Department Name'].unique()

# IT goods more than 50000 dollars
it_goods = ds[(ds['Total Price'] >= 50000) & (ds['Acquisition Type']== 'IT Goods')]  # 702 It goods 

# IT related purchases:
it1 = ds[ds['Acquisition Type'] == 'IT Goods'] #7811
it2 = ds[ds['Acquisition Type'] == 'IT Services'] #1741
it3 =  ds[ds['Acquisition Type'] == 'IT Telecommunications'] #6
# 7811 + 1741 + 6 = 9558 IT  realted purchases