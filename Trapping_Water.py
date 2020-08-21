ht = [3, 2, 1, 3, 4]
n = len(ht)
leftMax, rightMax = [0 for i in range(n)], [0 for i in range(n)]

leftMax[0] = ht[0]
for i in range(1, n):
    leftMax[i] = max(leftMax[i-1], ht[i])

rightMax[n-1] = ht[n-1]
for i in range(n-2, -1, -1):
    rightMax[i] = max(rightMax[i+1], ht[i])

water = 0
for i in range(0, n):
    water += min(leftMax[i], rightMax[i]) - ht[i]

print(water)

