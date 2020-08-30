def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

A = [1,2,2,3,4,5,5]
i, j, pairs = 0, 1, 0
k = 2
while j < len(A):
    if A[j]-A[i] < k:
        j += 1
    elif A[j] - A[i] > k:
        i += 1
    else:
        if A[i] == A[j]:
            c = j-i+1
            f = factorial(c) // (factorial(2)*factorial(c-2))
            j = c + 1
            pairs += f * 2
        else:
            n1, n2 = A[i], A[j]
            c1 = c2 = 0
            while A[i] == n1:
                c1 += 1
                i += 1
            if A[j] == A[-1]:
                j = len(A)-1
                while A[j] == n2:
                    c2 += 1
                    j -= 1
            else:
                while A[j] == n2:
                    c2 += 1
                    j += 1
        pairs += (c1 * c2)
print(pairs)

