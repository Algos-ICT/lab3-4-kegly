f=open('input3')
n, k=map(int, f.readline().split())
A=[int(i) for i in f.readline().split()]
if k==1:
    for i in range(len(A)):
        for k in range(len(A) - i - 1):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]

else:
    for i in range(len(A)-k):
        if A[i]>A[i+k]:
            A[i], A[i+k], = A[i+k], A[i]

# check :
file= open('output3', 'w')
flag=True
for i in range(len(A)-1):
    if A[i]>A[i+1]:
        flag=False
        break
if flag:
    file.write('YES')
else:
    file.write('NO')

file.close()