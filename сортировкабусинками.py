def bead_sort(arr):
    max_val = max(arr)                                  # Находим максимальное число
    beads = [[1] * num + [0] * (max_val - num) for num in arr]  # Создаем матрицу бусин
    beads_fallen = [sorted(col, reverse=True) for col in zip(*beads)]  # Бусины "падают"
    return [sum(col) for col in zip(*beads_fallen)]     # Считаем бусины в столбцах
print(bead_sort([3, 1, 4, 2]))
