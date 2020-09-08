A = [34,35,27,42,5,28,39,20,28]
st = []
n, top = len(A), 0
st.append(n-1)
for i in range(n-2, -1, -1):
    if A[i] < A[st[top]]:
        while A[i] < A[st[top]]:
            A[st[top]] = A[i]
            top -= 1
            st.pop()
            if top == -1:
                break
        st.append(i)
        top += 1
    else:
        st.append(i)
        top += 1
while top != -1:
    A[st[top]] = -1
    top -= 1
A[0] = -1
print(A)