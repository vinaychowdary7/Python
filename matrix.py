matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix)
# firstly transpose
for i in range(n):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix[i][j],matrix[j][i])
print(matrix)
# secondly invert by vertical
for i in range(n):
    for j in range(n // 2):
        matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
print(matrix)
print([1,2,3]*3)