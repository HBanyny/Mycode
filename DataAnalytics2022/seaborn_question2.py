
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('mpg')

df['liters_per_100km'] = 235.215 / df['mpg']

df = df.drop('mpg', axis=1)

df = df.drop('name', axis=1)

correlations = df.corr()

# model_year and acceleration don't correlate
df = df.drop('model_year', axis=1)
df = df.drop('acceleration', axis=1)

#☻ keeping the strongest correlation
corr1 = df['horsepower'].corr(df['liters_per_100km'])
corr2 = df['displacement'].corr(df['liters_per_100km'])
corr3 = df['cylinders'].corr(df['liters_per_100km'])
#drop horsepower and cylinders
df = df.drop('horsepower', axis=1)
df = df.drop('cylinders', axis=1)


# USA has bigger fuel consumption
plt.clf()
sns.pairplot(df, hue='origin')
plt.figure()

# Japan consume least fuel
sns.boxplot(x='origin', y='liters_per_100km', data=df)

# from the first plot weight seems to be another feature
