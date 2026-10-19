def word_break(s, words):
    words = set(words)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[-1]

for s, w in (("leetcode", ["leet", "code"]), ("applepenapple", ["apple", "pen"]),
             ("catsandog", ["cats", "dog", "sand", "and", "cat"])):
    print(f's="{s}", wordDict={w} -> {word_break(s, w)}')
