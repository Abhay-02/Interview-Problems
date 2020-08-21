def compare(p1, p2):
    if p1[0] > p2[0] and p1[1] >= p2[1] and p1[2] >= p2[2]:
        return 1
    elif p1[0] >= p2[0] and p1[1] > p2[1] and p1[2] >= p2[2]:
        return 1
    elif p1[0] >= p2[0] and p1[1] >= p2[1] and p1[2] > p2[2]:
        return 1
    return 0
T = int(input())
while T:
    per1, per2, per3 = 0, 0, 0
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))
    s3 = list(map(int, input().split()))
    if compare(s1, s2):
        max1, min1 = s1, s2
    elif compare(s2, s1):
        max1 = s2
        min1 = s1
    if compare(s1, s3):
        max1 = s1
        min1 = s3
    elif compare(s3, s1):
        max1 = s3
        min1 = s1
    if compare(s1, s2):
        max1 = s1
        min1 = s2
    elif compare(s2, s1):
        max1 = s2
        min1 = s1
    T -= 1