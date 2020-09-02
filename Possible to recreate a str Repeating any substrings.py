A = 'abab'
a = A
A += A
n = len(A)
A2 = A[1: n-1]
if a in A2:
    print("possible")
else:
    print("not possible")