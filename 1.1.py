# быстрая сортировка
import random
def f(a):
    def quick_sort(a,l,r):
        if l<r:
            k=random.randint(l,r) # индекс опорного элемента
            a[l], a[k] = a[k], a[l]
            m = partition(a, l, r)
            quick_sort(a, l, m)
            quick_sort(a,m+1,r)
    quick_sort(a,0,len(a)-1)

def partition(a, l, r):
    x = a[l]
    j=l
    m=j
    for i in range(l+1, r+1):
        if a[i]<x:
            j+=1
            m+=1
            a[m], a[i] = a[i], a[m]
            a[j], a[m] = a[j], a[m]

    a[l], a[j] = a[j], a[l]
    return j
f=open('input1')
A=list(map(int, f.readline().split()))
f(A)
file=open('output1', 'w')
for i in range(len(A)):
    file.write(str(i)+' ')
