def exponential_search(arr, target):
    if not arr: return -1
    i = 1
    while i < len(arr) and arr[i] < target:  # Экспоненциально увеличиваем границу
        i *= 2
    left, right = i//2, min(i, len(arr)-1)   # Определяем диапазон для поиска
    while left <= right:                      # Бинарный поиск в диапазоне
        mid = (left + right) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1
print(exponential_search([2, 4, 6, 8, 10, 12, 14, 16], 10))
