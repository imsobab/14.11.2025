def ternary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid1 = left + (right - left) // 3    # Первая точка деления
        mid2 = right - (right - left) // 3   # Вторая точка деления
        if arr[mid1] == target: return mid1
        if arr[mid2] == target: return mid2
        if target < arr[mid1]: right = mid1 - 1       # Ищем в левой трети
        elif target > arr[mid2]: left = mid2 + 1      # Ищем в правой трети
print(ternary_search([1, 3, 5, 7, 9, 11, 13, 15], 9))
