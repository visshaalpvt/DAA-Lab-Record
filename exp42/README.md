# Exp 42: median_of_medians(arr, k) Function

## Aim
To implement median_of_medians(arr, k) returning the k-th smallest element of an unsorted array.

## Algorithm
1. Divide the array into groups of 5 and sort each group
2. Take the median of every group and recursively find the median of these medians (the pivot)
3. Partition the array into elements smaller than, equal to and greater than the pivot
4. Recurse only into the part that contains the k-th smallest element

## Input
```
arr = [1,2,3,4,5,6,7,8,9,10], k = 6
arr = [23,17,31,44,55,21,20,18,19,27], k = 5
```

## Program
[`solution.py`](solution.py)

```python
def median_of_medians(arr, k):          # k is 1-based
    if len(arr) <= 5:
        return sorted(arr)[k - 1]
    groups = [sorted(arr[i:i + 5]) for i in range(0, len(arr), 5)]
    medians = [g[len(g) // 2] for g in groups]
    pivot = median_of_medians(medians, (len(medians) + 1) // 2)
    low = [x for x in arr if x < pivot]
    eq = [x for x in arr if x == pivot]
    high = [x for x in arr if x > pivot]
    if k <= len(low):
        return median_of_medians(low, k)
    if k <= len(low) + len(eq):
        return pivot
    return median_of_medians(high, k - len(low) - len(eq))

for arr, k in (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6), ([23, 17, 31, 44, 55, 21, 20, 18, 19, 27], 5)):
    print(f"arr={arr}, k={k}")
    print("Output:", median_of_medians(arr, k))
```

## Output
```
arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=6
Output: 6
arr=[23, 17, 31, 44, 55, 21, 20, 18, 19, 27], k=5
Output: 21
```

## Screenshot
![Output screenshot](output.png)

## Result
The program for **median_of_medians(arr, k) Function** was implemented and executed successfully, and the output shown above was obtained for all the given test cases.

## Time and Space Complexity
| | Complexity |
|---|---|
| **Time** | O(n) worst case |
| **Space** | O(n) |
