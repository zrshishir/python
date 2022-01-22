matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]

print('matrix: ',matrix)
transpose = [[row[i] for row in matrix] for i in range(4)]
print('transpose of the matrix: ', transpose)

transposed = []
for i in range(4):
     transposed.append([row[i] for row in matrix])
     
print(transposed)
     