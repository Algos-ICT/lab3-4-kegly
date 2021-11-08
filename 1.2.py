import random

def quick_sort(A, left, right):
    if left < right:
        x = A[left]
        j = left
        k = random.randint(left, right - 1)
        A[left], A[k] = A[left], A[k]
        for i in range(left + 1, right):
            if A[i] <= x:
                j += 1
                A[j], A[i] = A[i], A[j]
        A[left], A[j] = A[j], A[left]
        quick_sort(A, left, j)
        quick_sort(A, j + 1, right)

A=[1,6,3,2,1,5]
quick_sort(A, 0, len(A))
print(A)