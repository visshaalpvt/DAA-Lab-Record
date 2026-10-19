def sum_subarray_mins(arr):
    MOD = 10 ** 9 + 7
    n = len(arr)
    left, right, st = [0] * n, [0] * n, []
    for i in range(n):
        while st and arr[st[-1]] > arr[i]:
            st.pop()
        left[i] = i - (st[-1] if st else -1)
        st.append(i)
    st = []
    for i in range(n - 1, -1, -1):
        while st and arr[st[-1]] >= arr[i]:
            st.pop()
        right[i] = (st[-1] if st else n) - i
        st.append(i)
    return sum(a * l * r for a, l, r in zip(arr, left, right)) % MOD

print("arr=[3,1,2,4] ->", sum_subarray_mins([3, 1, 2, 4]))
print("arr=[11,81,94,43,3] ->", sum_subarray_mins([11, 81, 94, 43, 3]))
