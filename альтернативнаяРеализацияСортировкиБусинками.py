def bead_sort_simple(arr):
    for i in range(len(arr)):                           # Первый проход слева направо
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:                         # Если левый столбец выше
                arr[i] -= 1                             # Бусина падает вниз
                arr[j] += 1                             # Бусина поднимается вверх
    for i in range(len(arr)-1, -1, -1):                # Второй проход справа налево
        for j in range(i-1, -1, -1):
            if arr[i] < arr[j]:                         # Если правый столбец ниже
                arr[i] += 1
                arr[j] -= 1
    return arr
print(bead_sort_simple([2, 4, 1, 3]))
