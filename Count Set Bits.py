# Brian Kernighan's Algorithm
def countSetBits(n):
    c = 0
    while n:
        n = n & (n - 1)
        c += 1
    return c


n = int(input())
ct = 0
for i in range(1, n+1):
    ct += countSetBits(i)
print(ct)
