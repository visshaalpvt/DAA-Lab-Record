def binary_search(a, key, show=True):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if show:
            print(f"  low={low}, high={high}, mid=({low}+{high})//2={mid}, a[mid]={a[mid]}")
        if a[mid] == key:
            return mid + 1
        if a[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

for a, key in (([3, 9, 14, 19, 25, 31, 42, 47, 53], 31), ([13, 19, 24, 29, 35, 41, 42], 42), ([20, 40, 60, 80, 100, 120], 60)):
    print(f"Sorted a={a}, key={key}")
    print("Output (position):", binary_search(a, key), "\n")

u = [53, 9, 14, 19, 25, 3, 42, 47, 31]
print(f"UNSORTED a={u}, key=31 (31 is present at position 9)")
r = binary_search(u, 31)
print("Output:", r if r != -1 else "-1 -> key NOT found although it exists: binary search is incorrect on unsorted data")
