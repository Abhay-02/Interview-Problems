A = [1,8,6,2,5,4,8,3,7]
i, j = 0, len(A)-1
max_water = 0
while i < j:
    max_water = max(max_water, min(A[i], A[j]) * (j-i))
    if A[i] < A[j]:
        i += 1
    else:
        j -= 1
print(max_water)