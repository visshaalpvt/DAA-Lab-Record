def str_str(haystack, needle):
    n, m = len(haystack), len(needle)
    for i in range(n - m + 1):
        j = 0
        while j < m and haystack[i + j] == needle[j]:
            j += 1
        if j == m:
            return i
    return -1

for h, nd in (("sadbutsad", "sad"), ("leetcode", "leeto")):
    print(f'haystack="{h}", needle="{nd}" -> {str_str(h, nd)}')
