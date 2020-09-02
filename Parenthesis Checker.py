def checker(A):
    n = len(A)
    st = []
    st.append(A[0])
    top = 0
    for i in range(1, n):
        if (st[top] == '[' and A[i] == ']') or (st[top] == '{' and A[i] == '}') or (st[top] == '(' and A[i] == ')'):
            st.pop()
            top -= 1
        elif st[top] == ']' or st[top] == '}' or st[top] == ')':
            return -1
        else:
            top += 1
            st.append(A[i])
    if st == []:
        return 1
    else:
        return -1


# A = '{[(])}'
# A = '{[()][]}'
A = '{{{{{'
ans = checker(A)
if ans == 1:
    print("Valid")
else:
    print("Invalid")