
import pandas as pd 
import seaborn as sns
#import matplotlib.pyplot as plt
#import datetime

food = pd.read_csv('groceries.csv')

#fill nan columns
food['Fish'].fillna((food['Fish'].mean()), inplace=True)
food['Pork'].fillna((food['Pork'].mean()), inplace=True)
food['Sunflower-oil'].fillna((food['Sunflower-oil'].mean()), inplace=True)

#date cleanup
food[['Month','Year']]=food.Month.str.split('-',expand=True)
food['Month'] = pd.to_datetime(food.Month, format='%b').dt.month
food['Year'] = pd.to_datetime(food.Year, format='%y').dt.year
print(food)

#correlation and heatmap
correlations = food.corr()
sns.heatmap(correlations, annot=False)
#the grocery which price doesn't follow other groceries is sunflowe oil


# groceries that seem to coorelate to each other's prices are:
#corn,barley and wheat
#sunflower oil and coconut oil
