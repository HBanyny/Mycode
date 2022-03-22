import numpy as np

dataset = np.arange(1, 50).reshape(7, 7)

add = dataset + 50

total = np.sum(dataset)

odd = dataset[dataset % 2 != 0]

sum_odd = np.sum(odd)

deviation = np.std(dataset)

total_row = np.sum(dataset, axis = 1)

total_column = np.sum(dataset, axis = 0)


#without_numpy
total1 = 0

for i in range(50):
    
    total1 = total1 + i
    print(total1)
    
rows = len(dataset)
column = len(dataset[0])

for i in range(0, 7):
    sumRow = 0
    for j in range(0, 7):
        sumRow = sumRow + dataset[i][j]
        
    print(sumRow)
    
for i in range(0, 7):
    sumCol = 0
    for j in range(0, 7):
        sumCol = sumCol + dataset[j][i]
        
    print(sumCol)