def bubble_sort(v):
    for i in range(len(v) - 1):
        for j in range(len(v) - i - 1):
            if (v[j] > v[j + 1]):
                v[j], v[j + 1] = v[j + 1], v[j]

lista = [42, 7, 91, 15, 63, 28, 4, 77, 36, 59, 12, 84, 23, 68, 95, 31, 50, 9, 71, 18]

bubble_sort(lista)

print(lista)