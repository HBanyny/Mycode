import pandas as pd

# helper function for pandas to convert all salaries
# into yearly integer salaries
def yearly_wage(row):
    # the last two characters determine if it's yearly, monthly, hourly
    period = row['Salary'][-2:]
    
    # remove all commas and combine all numbers
    number = int(''.join(filter(str.isdigit, row['Salary'])))
    
    # if it's hourly, the average work hours per year in India is
    # approximately 2117.01 (might change in future)
    if period == "hr":
        number = int(number * 2117.01)
    elif period == "mo":
        # months to year
        number = int(number * 12)
    
    # return the yearly salary in integer format
    return number

# read data
ds = pd.read_csv("data_salaries_india.csv")

# most common value in different fields:
job_title = ds['Job Title'].value_counts() #28

companies = ds['Company Name'].value_counts() #2523

location = ds['Location'].value_counts() #5

# based on the distribution the data is not balanced

# combine job titles
def replace(string: str) -> str:
    if 'Associate' in string:
        rv = ''
        for word in string.split():
            rv += ' Machine learning Associate specialist' if 'Associate' in word else ' ' + word
        return rv.strip()
    else:
        return string

print (ds)

#outliners: drop rows where the salary is negative
#ds = ds[ds['Salary'] < 0]

# correlation role-column
label1, unique1 = pd.factorize(ds['Role'], sort=False)
ds['ManagerRole'] = label1

# checking out the correlations
correlations = ds.corr(method="spearman")
# correlation is low