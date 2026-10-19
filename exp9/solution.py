def binary_search(arr, key):
    data = sorted((v, i + 1) for i, v in enumerate(arr))   # (value, original position)
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid][0] == key:
            return data[mid][1]
        if data[mid][0] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

X = [3, 4, 6, -9, 10, 8, 9, 30]
for key in (10, 100):
    pos = binary_search(X, key)
    print(f"Element {key} is found at position {pos}" if pos != -1 else f"Element {key} is not found")
