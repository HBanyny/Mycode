

import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')

plt.clf()
sns.pairplot(penguins)
plt.figure()

# There is a strong positive correlation between flipper_lenght_mm and body_mass
correlations = penguins.corr()
sns.heatmap(correlations, annot=True)

#huue(island)
plt.clf()
sns.pairplot(penguins, hue='island')
plt.figure()

#value_counts
print(penguins['island'].value_counts())
#visualisation plot
plt.clf()
sns.countplot(x="island", data=penguins)
plt.figure() # Torgersen doesn't belong to the group

# according to the plots, it looks like there is not a remarquable difference 
plt.clf()
sns.pairplot(penguins, hue='species')
plt.figure()

# the sex of the penguins affect the results:
plt.clf()
sns.pairplot(penguins, hue='sex')
plt.figure()


#scatter plot
sns.scatterplot(x='bill_length_mm', y='flipper_length_mm', 
                hue='island', data=penguins)
#sns.scatterplot(x='bill_length_mm', y='flipper_length_mm', 
                #data=penguins, hue='species')
plt.figure()
# I see that the species affect the result more, there is a better distribution


#violinplot
sns.violinplot(x='species', y='flipper_length_mm', 
            data=penguins, hue='island')
#sns.violinplot(x='species', y='bill_length_mm', 
            #data=penguins, hue='island')
#sns.violinplot(x='species', y='body_mass_g', 
            #data=penguins, hue='island')

# the features i see is that the flippers and bills of penguins affect their numbers
# the other features I can notice is that Adelie's species are presentr in all 3 islands
#unlike other species 
