import pandas as pd

ds = pd.read_csv("loans.csv")
                 
# deleting the customer id column
dsDel = ds.drop('Customer ID', axis=1)

#printing the head 
head = ds.head()

#removing large_loan rows
rowKeep = ds[ds['Current Loan Amount'] < 9999999]


#removing nan rows
filt = ds.dropna(subset=['Annual Income'])

# extra: replace the nan with average income 
ds['Annual Income'].fillna((ds['Annual Income'].mean()), inplace=True)

# finding average
average = ds['Current Loan Amount'].mean()

maxds = ds['Annual Income'].max()

minds = ds['Annual Income'].min()


# ownership
home_ownership= ds[ds['Loan ID'] =="bbf87a87-22cd-4d10-bd9b-7a9cc1b6e59d"]

# actual annual income
ds['Actual Annual Income']= ds['Annual Income'] - 12 * ds['Monthly Debt']
actual_annual_income = ds[ds['Loan ID'] == "76fa89b9-e6a8-49af-afa1-8151315aba8e"]

# finding the Loan ID with min AAI
loan_id = ds.loc[ds['Actual Annual Income'].idxmin()]['Loan ID']

# finding long loan terms
long_term_loan = ds[ds['Term'] == 'Long Term']

# more than 1 bankruptcy
loaner_bankruptcy = ds[ds['Bankruptcies'] > 1]

# short term loans for Home Improvements
short_term_loan = ds[ds['Term'] == 'Short Term']
#home improvements
home_improvement = short_term_loan[short_term_loan['Purpose'] == 'Home Improvements']

# unique purposes
unique_loan = ds['Purpose'].unique()

# 3 common loan purposes 
three_most_common = ds['Purpose'].value_counts()[:3]

# correlation between annual Income and Number of Open Accounts
corr1 = ds['Annual Income'].corr(ds['Number of Open Accounts']) #0.13193586215335376
# correlation between Number of Credit Problems and Bankruptcies
corr2 = ds['Number of Credit Problems'].corr(ds['Bankruptcies'])#0.7529419405195407
#corr2 > corr1
#there is more correlation between Number of Credit Problems and Bankruptcies!
