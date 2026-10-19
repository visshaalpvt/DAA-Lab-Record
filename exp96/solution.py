from collections import Counter

def word_subsets(words1, words2):
    need = Counter()
    for b in words2:
        for ch, c in Counter(b).items():
            need[ch] = max(need[ch], c)
    return [a for a in words1 if all(Counter(a)[ch] >= c for ch, c in need.items())]

w1 = ["amazon", "apple", "facebook", "google", "leetcode"]
print('words2=["e","o"] ->', word_subsets(w1, ["e", "o"]))
print('words2=["l","e"] ->', word_subsets(w1, ["l", "e"]))
