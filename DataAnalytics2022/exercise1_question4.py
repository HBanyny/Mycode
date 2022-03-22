import numpy as np

data = np.linspace(0, 1, 10)
print(data)

a = np.linspace(0, 5, 100)
print(a)


#without_numpy
matrix = []

for i in range(10):
    
    row = []
    
    for j in range(10):
        row.append(10 * (i + j))
        
    matrix.append(row)
    
print(matrix)
