import math
f = open('input8')
n, k = map(int, f.readline().split())  # количество всех и искомых точек
points = dict()  # словарь вида : расстояние - координаты точки [x, y]
for i in range(n):
    x, y = map(int, f.readline().split())
    d = math.sqrt(x**2 + y**2)
    points[d] = [x, y]
# словарь не изменяемый так что отсортировать нельзя
# создадим список из ключей и отсортируем а потом будем через них
# обащаться к значениям в словаре
list_keys = list(points.keys())
list_keys.sort()    # любая сортировка( например quicksort )
file = open('output8', 'w')
for i in range(k):
    file.write(str(points[list_keys[i]])+',')
f.close()