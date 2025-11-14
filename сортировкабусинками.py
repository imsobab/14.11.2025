def bead_sort(arr):
    """
    Сортировка бусинами - визуализирует сортировку как падающие бусины
    на абакусе (счетах)
    """
    if len(arr) == 0:
        return arr
    
    # Находим максимальное значение для определения количества "стержней"
    max_val = max(arr)
    
    # Создаем матрицу бусин (True - бусина есть, False - нет)
    beads = [[False] * len(arr) for _ in range(max_val)]
    
    # Расставляем бусины согласно исходному массиву
    for i, num in enumerate(arr):
        for j in range(num):
            beads[j][i] = True
    
    # "Падаем" бусинами вниз под действием гравитации
    for i in range(max_val):
        # Считаем количество бусин в текущем ряду
        bead_count = sum(1 for bead in beads[i] if bead)
        
        # Опускаем все бусины вниз
        for j in range(len(arr)):
            beads[i][j] = (j < bead_count)
    
    # Преобразуем бусины обратно в числа
    result = [0] * len(arr)
    for j in range(len(arr)):
        # Считаем количество бусин в каждом столбце
        result[j] = sum(1 for i in range(max_val) if beads[i][j])
    
    return result

# Пример использования
arr = [3, 1, 4, 1, 5, 9, 2, 6]
print("Исходный массив:", arr)
print("Отсортированный массив:", bead_sort(arr))
