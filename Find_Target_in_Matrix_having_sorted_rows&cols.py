def findPos(A, target):
    i = 0
    j = len(A) - 1
    p1, p2 = -1, -1
    while i < len(A) and j >= 0:
        if A[i][j] == target:
            p1 = i
            p2 = j
            return p1, p2
        elif target < A[i][j]:
            j -= 1
        elif target > A[i][j]:
            i += 1
    return -1, -1



A = []
for i in range(5):
    A.append(list(map(int, input().split())))
target = 35
pos1, pos2 = findPos(A, target)
print(pos1, pos2)

#10 20 30 40 50
#15 25 35 45 55
#16 26 36 46 56
#17 27 37 47 57
#18 28 38 48 58