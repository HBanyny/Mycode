import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


 
# our helper function to create the price difference
# between selling price and present price (ex-showroom price)
def percentage_difference(row):
    selling = row['selling_price']
    road = row['ex_showroom_price']

    # the difference in decimal format
    result = 1 - round(selling / road, 2)
    return result
 
 
# load the csv dataset
df = pd.read_csv('BIKE.csv')

 
#we gonna replace nan values in the ex showrrom price columns to actual values
df['ex_showroom_price'].fillna((df['ex_showroom_price'].mean()), inplace=True)

# let's use our helper function to make the price difference column!
df['price_difference'] = df.apply(percentage_difference, axis=1)

#counts of owners
owner_counts = df['owner'].value_counts()
#most owners are 1st owners
#drop owner
df = df.drop('owner', axis=1)

# counts of seller type
seller_type_counts = df['seller_type'].value_counts()
#looks like most of seller_type is individual
#drop seller_type
df = df.drop('seller_type', axis=1)

# let's reorder the columns for easier reading in the variable explorer
column_names = ['name', 'Year', 'selling_price', 'ex_showroom_price', 'Price_Difference', 'km_driven']
#df = df.reindex(columns = column_names)
 
top_bike_company = df['name'].value_counts().head(10)
plt.figure(figsize=(10, 8))
sns.barplot(x = top_bike_company, y = top_bike_company.index)
plt.ylabel('Name of bike')
plt.title('Top 10 bike company')
plt.xlabel('Count')
# Bajaj pulsar 150 is the most popular
 
# correlations
correlations = df.corr()
#there is a big correlation between the price_difference and km_driven
# as well as the selling price and the ex showroom price which makes sense
 
#year plot
sns.displot(df['year'])

#we see from the year plot that there has been a peak between 2010 - 2020
#let's check it
highest_bike_purchased_year = df['year'].value_counts().head(10)
highest_bike_purchased_year
#it was 2017



sns.pairplot(df)









