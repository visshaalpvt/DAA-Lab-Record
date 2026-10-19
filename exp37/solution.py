def binary_search(a, key):
    low, high, comps = 0, len(a) - 1, 0
    while low <= high:
        mid = (low + high) // 2
        comps += 1
        if a[mid] == key:
            return mid + 1, comps
        if a[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comps

for a, key in (([5, 10, 15, 20, 25, 30, 35, 40, 45], 20), ([10, 20, 30, 40, 50, 60], 50), ([21, 32, 40, 54, 65, 76, 87], 32)):
    pos, c = binary_search(a, key)
    print(f"a={a}, key={key}")
    print(f"Output: position = {pos}, comparisons = {c}")
