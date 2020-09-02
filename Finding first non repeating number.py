#  Finding first non repeating number
A = [2,6,3,2,5,3,6,3]
d = {}
for i in A:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in d.keys():
    if d[i] == 1:
        ans = i
        break
print(ans)