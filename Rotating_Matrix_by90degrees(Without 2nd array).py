def transpose_matrix(mat):
    for i in range(len(mat)):
        for j in range(i, len(mat)):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

def reverse_rows(mat):
    for i in range(len(mat)):
        k = len(mat) - 1
        for j in range(0, k):
            mat[i][j], mat[i][k] = mat[i][k], mat[i][j]
            k -= 1

mat = []
r, c = map(int, input().split())
for i in range(r):
    mat.append(list(map(int, input().split())))
transpose_matrix(mat)
reverse_rows(mat)
print(mat)
