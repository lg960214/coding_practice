N, M = map(int, input().split())

matrix_A = []
matrix_B = []

for i in range(N):
    temp_lst = list(map(int, input().split()))
    matrix_A.append(temp_lst)

for i in range(N):
    temp_lst = list(map(int, input().split()))
    matrix_B.append(temp_lst)

for i in range(N):
    for j in range(M):
        matrix_A[i][j] += matrix_B[i][j]
        print(matrix_A[i][j], end=' ')
    print()

