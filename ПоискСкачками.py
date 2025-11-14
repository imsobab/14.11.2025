import math

def jump_search(arr, target):
    """
    Поиск скачками - улучшенная версия линейного поиска для отсортированных массивов
    """
    n = len(arr)
    
    # Определяем размер прыжка (оптимально - квадратный корень из n)
    step = int(math.sqrt(n))
    
    # Находим блок, где может находиться элемент
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # Элемент не найден
    
    # Линейный поиск в найденном блоке
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1  # Элемент не найден
    
    # Проверяем, найден ли элемент
    if arr[prev] == target:
        return prev
    else:
        return -1

# Пример использования
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
target = 55
print(f"Массив: {arr}")
print(f"Поиск элемента {target}")
result = jump_search(arr, target)
if result != -1:
    print(f"Элемент найден на позиции {result}")
else:
    print("Элемент не найден")
