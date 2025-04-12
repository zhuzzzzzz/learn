import math

import  numpy as np

def matrix_rank(matrix):
    M = len(matrix)
    N = len(matrix[0])
    rank = 0
    row_checked = [False] * M

    for col in range(N):
        pivot_row = -1
        for row in range(M):
            if not row_checked[row] and matrix[row][col] != 0:
                pivot_row = row
                break

        if pivot_row == -1:
            continue

        rank += 1
        row_checked[pivot_row] = True

        for row in range(M):
            if row != pivot_row:
                factor = matrix[row][col] / matrix[pivot_row][col]
                for k in range(N):
                    matrix[row][k] -= factor * matrix[pivot_row][k]

    return rank


# 测试示例
a = [[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print("矩阵的秩为:", matrix_rank(a))
rank = np.linalg.matrix_rank(a)
print(rank)

def is_sushu(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


print((is_sushu(18853+978)))