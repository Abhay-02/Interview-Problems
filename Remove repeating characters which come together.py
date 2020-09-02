#  Remove the characters that come together
A = ['a','b','c','c','b','d']
st = []
top, n = 0, len(A)
st.append(A[0])
for i in range(1, n):
    if st[top] == A[i]:
        st.pop()
        i += 1
        top -= 1
    else:
        st.append(A[i])
        top += 1
print(st, top)