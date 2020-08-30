import math
A, B, C = [1,4,5,8,10], [6,9,10], [2,3,6,10]
i = j = k = 0
min1 = min(A[i], B[j], C[k])
minimum = abs(max(A[i],B[j],C[k]) - min1)

while (i<len(A)-1 and j<len(B)-1 and k<len(C)-1):
    if min1 == A[i] :
        i += 1
    elif min1 == B[j]:
        j += 1
    elif min1 == C[k]:
        k += 1
    min1 = min(A[i], B[j], C[k])
    m = abs(max(A[i], B[j], C[k]) - min1)
    if m < minimum:
        minimum = m
print(minimum)
