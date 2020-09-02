# Isomorphic means should have only one corresponding character for each character of the two strings
s1 = 'abb'
s2 = 'cac'
n = len(s1)
d1, d2 = {}, {}
for i in range(n):
    if s1[i] in d1:
        print("not-isomorphic")
        break
    else:
        d1[s1[i]] = s2[i]
    if s2[i] in d2:
        print("not-isomorphic")
        break
    else:
        d2[s2[i]] = s1[i]
print(d1, d2)
