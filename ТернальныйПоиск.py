def ternary_search(arr, target):
    """
    Тернарный поиск - делит массив на три части вместо двух
    """
    return ternary_search_recursive(arr, target, 0, len(arr) - 1)

def ternary_search_recursive(arr, target, left, right):
    """
    Рекурсивная реализация тернарного поиска
    """
    if left > right:
        return -1
    
    # Разделяем массив на три части
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3
    
    # Проверяем точки разделения
    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2
    
    # Определяем, в какой части продолжать поиск
    if target < arr[mid1]:
        # Ищем в левой части
        return ternary_search_recursive(arr, target, left, mid1 - 1)
    elif target > arr[mid2]:
        # Ищем в правой части
        return ternary_search_recursive(arr, target, mid2 + 1, right)
    else:
        # Ищем в средней части
        return ternary_search_recursive(arr, target, mid1 + 1, mid2 - 1)

def ternary_search_iterative(arr, target):
    """
    Итеративная реализация тернарного поиска
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    
    return -1

# Пример использования
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
target = 7
print(f"Массив: {arr}")
print(f"Поиск элемента {target}")

result_recursive = ternary_search(arr, target)
result_iterative = ternary_search_iterative(arr, target)

print(f"Рекурсивный поиск: элемент на позиции {result_recursive}")
print(f"Итеративный поиск: элемент на позиции {result_iterative}")
