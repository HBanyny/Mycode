import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

 

df = pd.read_csv("netflix_titles.csv")

 

# initial correlations
correlations = df.corr()

 
#replace unmentioned country with the most popular one
df['country'] = df['country'].fillna(df['country'].mode()[0])

# drop cast and director
df = df.drop('cast', axis = 1)
df = df.drop('director', axis = 1)
df = df.drop('description', axis = 1)
df = df.drop('show_id', axis = 1)

#We have 17 nan values left
x = df.isna().sum().sum()
#so we drop the rows that have nan values in them
df.dropna(inplace=True)
#now nan = y = 0
y = df.isna().sum().sum()



#movies or tv-shows
movies_or_tv_shows = df['type'].value_counts().reset_index()
sns.countplot(x="type", data=df)
#there are more Movies on Netflix than TV shows

#Netflix ratings
plt.figure(figsize=(12,10))
sns.countplot(x="rating", data=df, order=df['rating'].value_counts().index[0:15])
# first most rating is mature, then second is 'no less than 14', and third is R rating (17yo)


# top 10 countries
country_count=df['country'].value_counts().sort_values(ascending=False)
country_count=pd.DataFrame(country_count)
topcountries=country_count[0:11]
topcountries # USA INDIA UK JAPAN SOUTH KOREA CANADA ...

#release years
plt.figure(figsize=(12,10))
sns.countplot(y="release_year", data=df, order=df['release_year'].value_counts().index[0:15])
#So, 2018 was the year when most of the content was released.



 