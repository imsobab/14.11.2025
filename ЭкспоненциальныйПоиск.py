def exponential_search(arr, target):
    """
    Экспоненциальный поиск - работает на отсортированных массивах,
    особенно эффективен для неограниченных/бесконечных массивов
    """
    n = len(arr)
    
    # Если массив пустой
    if n == 0:
        return -1
    
    # Если искомый элемент - первый
    if arr[0] == target:
        return 0
    
    # Находим диапазон для бинарного поиска
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    
    # Выполняем бинарный поиск в найденном диапазоне
    return binary_search(arr, target, i // 2, min(i, n - 1))

def binary_search(arr, target, left, right):
    """
    Вспомогательная функция бинарного поиска
    """
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Пример использования
arr = [2, 3, 4, 10, 15, 18, 20, 22, 25, 30, 40, 45, 50, 60, 70, 80, 90, 100]
target = 25
print(f"Массив: {arr}")
print(f"Поиск элемента {target}")
result = exponential_search(arr, target)
if result != -1:
    print(f"Элемент найден на позиции {result}")
else:
    print("Элемент не найден")
