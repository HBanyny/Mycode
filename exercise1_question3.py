import numpy as np

value = np.arange(1, 50)

value = value.reshape(7, 7)

print(value)


matrix = []

for i in range(7):
    row = []
    
    for j in range(7):
        row.append(7 * i + j)
        
    
    matrix.append(row)
    
print(matrix)

data1 = np.random.rand(8, 8)
print(data1)

data2 = np.random.randn(3)
data2 = np.random.randn(8, 8)
print(data2)
