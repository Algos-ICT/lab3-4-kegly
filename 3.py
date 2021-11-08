f=open('input3')
n, k= map(int, f.readline().split())
A= [int(i) for i in f.readline().split()]
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