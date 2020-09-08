# IF SUM OF ANY SUB ARRAY EQUALS 0
# USING PREFIX ARRAY
A, P, d = [4,2,3,-5,8], [], {}
P.append(A[0])
d[P[0]] = 1
for i in range(1, len(A)):
    P.append(P[i-1] + A[i])
    if P[i] in d or P[i] == 0:      # for case A = [-1,1]
        index = i
    else:
        d[P[i]] = 1
print(P)
print(index)