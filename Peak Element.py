A = [1,1000000000,1000000000]
n = len(A)
low, high = 0, n-1
while low <= high:
    mid = low + (high - low)//2
    if mid > 0 and mid < n - 1:
        if A[mid + 1] >= A[mid] and A[mid - 1] <= A[mid]:
            low = mid + 1
        elif A[mid - 1] >= A[mid] and A[mid + 1] <= A[mid]:
            high = mid - 1
        elif A[mid - 1] < A[mid] and A[mid + 1] < A[mid]:
            print(A[mid])
    else:
        break
if A[0] > A[n - 1]:
    print(A[0])
print(A[n - 1])