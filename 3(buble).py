f=open('input3')
n, k=map(int, f.readline().split())
A=[int(i) for i in f.readline().split()]

for i in range(len(A)):
    for j in range(len(A) - i - k):
        if A[j] > A[j + k]:
            A[j], A[j + k] = A[j + k], A[j]

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