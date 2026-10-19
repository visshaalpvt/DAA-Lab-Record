from collections import defaultdict

def count_pairs(nums, k):
    pos = defaultdict(list)
    for i, v in enumerate(nums):
        pos[v].append(i)
    cnt = 0
    for idx in pos.values():
        for a in range(len(idx)):
            for b in range(a + 1, len(idx)):
                if (idx[a] * idx[b]) % k == 0:
                    cnt += 1
    return cnt

for nums, k in (([3, 1, 2, 2, 2, 1, 3], 2), ([1, 2, 3, 4], 1)):
    print(f"nums={nums}, k={k} -> {count_pairs(nums, k)}")
