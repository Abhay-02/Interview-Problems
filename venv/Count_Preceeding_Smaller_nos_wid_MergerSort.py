def merge(A, l, m, r):
    global s
    n1 = m - l + 1
    n2 = r - m
    L = [0]*(n1)
    R = [0]*(n2)
    for i in range(n1):
        L[i] = A[l + i]

    for j in range(n2):
        R[j] = A[m + 1 + j]

    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            s += len(L) - i
            j += 1
        k += 1
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

def merge_sort(A, beg, end):
    if beg < end:
        mid = (beg + (end-1)) // 2
        merge_sort(A, beg, mid)
        merge_sort(A, mid+1, end)
        merge(A, beg, mid, end)

s = 0
A = list(map(int, input().split()))
n = (len(A)-1)
merge_sort(A, 0, n)
print(A)
for i in range(0, len(A)):
    print (A[i])
print(s)