import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))                # Размер прыжка = квадратный корень из n
    prev = 0
    while prev < n and arr[prev] < target:  # Прыгаем по массиву
        prev += step
    start = max(0, prev - step)             # Возвращаемся к началу блока
    for i in range(start, min(prev, n)):    # Линейный поиск в блоке
        if arr[i] == target:
            return i
    return -1
print(jump_search([1, 3, 5, 7, 9, 11, 13], 7))
