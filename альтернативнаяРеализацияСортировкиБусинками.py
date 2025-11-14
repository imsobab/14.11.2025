def bead_sort_optimized(arr):
    """
    Оптимизированная версия сортировки бусинами
    """
    if not arr:
        return []
    
    # Создаем копию массива для работы
    beads = [0] * max(arr)
    
    # Распределяем бусины по уровням
    for num in arr:
        for i in range(num):
            beads[i] += 1
    
    # Собираем результат
    result = []
    for i in range(len(arr)):
        level = 0
        while level < len(beads) and beads[level] > 0:
            level += 1
        result.append(level)
        # Убираем одну бусину с каждого уровня
        for j in range(level):
            beads[j] -= 1
    
    return result

# Пример использования
arr = [5, 3, 1, 7, 4, 1, 1, 20]
print("Исходный массив:", arr)
print("Отсортированный массив:", bead_sort_optimized(arr))
