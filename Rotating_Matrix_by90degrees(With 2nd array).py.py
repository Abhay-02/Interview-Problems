#IMPORTANT

r = int(input())
c = int(input())
A = [[2,3,4], [5, 6, 7]]
B = [[0 for i in range(r)] for i in range(c)]
print(B)
for i in range(c):
    k = r - 1
    for j in range(r):
        B[i][j] = A[k][i]
        k -= 1
print(B)