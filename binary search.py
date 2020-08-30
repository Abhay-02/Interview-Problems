def binarySearch(A, t):
    low, high = 0, len(A) - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if t < A[mid]:
            high = mid - 1
        elif t > A[mid]:
            low = mid + 1
        else:
            return mid
    return low


A, t = [2, 5, 7, 9, 11, 15, 20], 17
pos = binarySearch(A, t)
if A[pos] == t:
    print("pos=", pos)
else:
    print("Pos to be inserted=", pos)
