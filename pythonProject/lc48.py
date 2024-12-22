# transpose then reverse
matrix = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(0, len(matrix)):
    for j in range(i, len(matrix[0])):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp

for i in range(0, len(matrix)):
    matrix[i] = matrix[i][::-1]

print(matrix)

# Brute
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
#
# arr = []
# ans = []
# for i in range(len(matrix[0])):
#     for j in range(len(matrix)-1, -1, -1):
#         arr.append(matrix[j][i])
#
#     ans.append(arr)
#     arr = []
#
# print(ans)
