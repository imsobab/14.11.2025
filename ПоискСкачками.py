import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while prev < n and arr[prev] < target:
        prev += step
    start = max(0, prev - step)
    for i in range(start, min(prev, n)):
        if arr[i] == target:
            return i
    return -1
print(jump_search([1, 3, 5, 7, 9, 11, 13], 7))
