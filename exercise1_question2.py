import numpy as np

data = np.zeros(15)
print(data)

data1 = np.ones(15)
print(data1)

data2 = np.ones(15) * 7
print(data2)

data3 = np.arange(100, 150)
print(data3)

data4 = np.arange(1900, 2021)
print(data4)

data5 = np.arange(0, 100, 2)
print(data5)

data6 = np.arange(1950, 2020)
y = (data6 % 4 == 0)
z = data6[y]

print(z)