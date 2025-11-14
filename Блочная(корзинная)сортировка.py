def bucket_sort(arr):
    if not arr: return arr                    # Если массив пустой - возвращаем
    buckets = [[] for _ in range(len(arr))]   # Создаем пустые корзины
    for num in arr:                           # Распределяем числа по корзинам
        buckets[int(num * len(arr))].append(num)
    return [num for bucket in buckets for num in sorted(bucket)]  # Сортируем корзины и объединяем
print(bucket_sort([0.42, 0.32, 0.33, 0.52, 0.37]))
