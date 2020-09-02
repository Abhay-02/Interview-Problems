#A = ['cat', 'dog', 'god','tca']
A = ['rat', 'tar', 'art']
a, k = {}, 1
for i in A:
    j = str(sorted(i))
    if j in a:
        a[j] += [k]
    else:
        a[j] = [k]
    k += 1
l = list(i for i in a.values())
print(l)