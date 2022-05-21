import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

 

df = pd.read_csv("supermarket_sales.csv")

x = df.shape #number of rows and columns 1000,17

#drops
df = df.drop('Invoice ID', axis = 1)
df = df.drop('Time', axis = 1)


y = df.dtypes
#since date is object, we will convert it to datetime
df['Date'] = pd.to_datetime(df['Date'])
#let's check date type now
z = df.dtypes #they are not object anymore

#calculation avg unit price
avg_unit_price = df["Unit price"].astype("float").mean(axis=0)
df["Unit price"].replace(np.nan, avg_unit_price, inplace=True)

#drop nan values
df.dropna(inplace=True)

null = df.isnull().sum() #we have no null values


# initial correlations
df.describe()
correlations = df.corr()
np.round(df.corr(),2)
#after some searching I figured out that since some variables did not vary, 
#then the respective standard deviation will be zero and so will the denominator of the fraction. 
#Thus, the correlation at 'gross margin percentage"  will be NaN.

#plots
plt.figure(dpi=125)
sns.heatmap(np.round(df.corr(),2),annot=True)
plt.show()
#The best correlated are Tax 5%, Total, Gross Income and cogs i.e Cost of Goods sold with a correlation of 1.

plt.figure(figsize=(12,6),dpi=100)
sns.regplot(x='Tax 5%',y='gross income',data=df,color='Blue')
plt.xlabel('Tax 5%')
plt.ylabel('Gross Income')
plt.show()


#there is a 71% correlation between the (Tax 5%, Total, Gross Income cogs) and quantity
plt.figure
sns.regplot(x='Quantity',y='Total',data=df,color='Red')
plt.xlabel('Quantity')
plt.ylabel('Cost of Goods Sale')
plt.title('Quantity and Cost of Goods Sale correlatrion',fontsize=15)
plt.show()

## To see the distribution of different ratings and the average rating
plt.figure(dpi=125)
sns.distplot(df['Rating'],kde=False)
plt.axvline(x=np.mean(df['Rating']),c='purple',label='Mean Rating')
plt.legend()
plt.show()
#the mean rating is 7

# Plotting Histogram for all
df.hist(figsize=(12,12))
plt.show()


#wich branch has more popularity
# Branch Count
plt.figure(dpi=125)
sns.countplot(df['Branch'])
plt.xlabel('Branch Name')
plt.ylabel('Count')
plt.title('Which Branch is the most popular?')
A,B,C =df.Branch.value_counts()
print('Branch A -',A)
print('Branch B -',C)
print('Branch C -',B)
plt.show()
#the answer is A!

#Which Payment Method is most used?
plt.figure(dpi=125)
sns.countplot(df['Payment'])
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.title('Which Payment Method is most used?')
A,B,C =df.Payment.value_counts()
print('E-wallet -',A)
print('Cash -',B)
print('Credit Card -',C)
plt.show()
# the answer is e-wallet


#Which City is most busy?
plt.figure(dpi=125)
sns.countplot(df['City'])
plt.xlabel('City')
plt.ylabel('Count')
plt.title('Which City is most busy?')
A,B,C =df.City.value_counts()
print('Yangon -',A)
print('Naypyitow -',C)
print('Mandalay -',B)
plt.show()
#the answer is Yangon


#gender count
plt.figure(dpi=125)
sns.countplot(df['Gender'])
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Count of Gender')
A,B =df.Gender.value_counts()
print('Male-',B)
print('Female -',A)
plt.show()
#Male- 499
#Female - 501

#Visualizing a Gender based comparison related to Product Type
sns.catplot(x='Product line',y='Unit price',hue='Gender',data=df,aspect=2)
plt.xlabel('Product Type')
plt.ylabel('Unit Price')
plt.show()

#a better way to look at the distribution between males and females
plt.figure(dpi=125)
sns.countplot(y ='Product line', hue = "Gender", data = df) 
plt.xlabel('Count')
plt.ylabel('Product Type')
plt.show()
#Well, In Health & Beauty, Males are much more than Females 
#whereas in Fashion accessories , Food & beverages and Sports & Travel Females are more


#which city leads by product type?
plt.figure(dpi=125)
sns.countplot(y ='Product line', hue = "City", data = df) 
plt.xlabel('Count')
plt.ylabel('Product Type')
plt.show()
#Well, Yangon leads at Home & Lifestyle and Electronic accessories.
#Naypyitaw leads at Food & Bevaerages and Fashion accessories.
#Mandalay leads at Sports & Travel and Health & Beauty.


#Finding Which Branch has better sale for a particular product type
plt.figure(dpi=125)
sns.countplot(y ='Product line', hue = "Branch", data = df) 
plt.xlabel('Count')
plt.ylabel('Product Type')
plt.show()
#Well, branch A leads at Home & Lifestyle and Electronic accessories.
#Branch C leads at Food & Bevaerages and Fashion accessories.
#Branch B leads at Sports & Travel and Health & Beauty.


