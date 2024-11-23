# O(log n)
def binary_search(arr, target):
    left = 0
    right =  len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 0
result = binary_search(arr, target)
if result != -1:
    print(f"Элемент найден на индексе {result}")
else:
    print("Элемент не найден")
