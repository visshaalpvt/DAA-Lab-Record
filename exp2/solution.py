def find_intersection_values(nums1, nums2):
    s1, s2 = set(nums1), set(nums2)
    return [sum(x in s2 for x in nums1), sum(x in s1 for x in nums2)]

for a, b in (([2, 3, 2], [1, 2]), ([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6])):
    print(f"nums1={a}, nums2={b}")
    print("Output:", find_intersection_values(a, b))
