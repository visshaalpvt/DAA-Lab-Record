from collections import Counter

def four_sum_count(A, B, C, D):
    ab = Counter(a + b for a in A for b in B)
    return sum(ab[-(c + d)] for c in C for d in D)

print("A=[1,2], B=[-2,-1], C=[-1,2], D=[0,2] ->", four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2]))
print("A=[0], B=[0], C=[0], D=[0] ->", four_sum_count([0], [0], [0], [0]))
