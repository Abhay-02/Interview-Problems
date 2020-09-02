A = [14,10,3,2,9,12]
n = len(A)
st = []
st.append(0)
top = 0
for i in range(1,n):
    if A[i] > A[st[top]]:
        while A[i] > A[st[top]]:
            A[st[top]] = A[i]
            st.pop()
            top -= 1
            if top == -1:
                break
    else:
        top += 1
        st.append(i)
while top != -1:
    A[st[top]] = -1
    top -= 1
A[n-1] = -1
print(A)