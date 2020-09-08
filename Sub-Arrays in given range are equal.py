A = [1,7,11,8,11,7,1]
B = [
    [0,2,4,6]
    ]

a1, a2 = {}, {}
for j in range(len(B)):
    l1, r1, l2, r2 = B[j][0], B[j][1], B[j][2], B[j][3]
    for i in range(l1, r1+1):
        if A[i] in a1:
            a1[A[i]] += 1
        else:
            a1[A[i]] = 1
    for i in range(l2, r2+1):
        if A[i] in a2:
            a2[A[i]] += 1
        else:
            a2[A[i]] = 1
    print(a1 == a2)