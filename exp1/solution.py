def first_palindrome(words):
    for w in words:
        if all(w[i] == w[-1 - i] for i in range(len(w) // 2)):
            return w
    return ""

for words in (["abc", "car", "ada", "racecar", "cool"], ["notapalindrome", "racecar"], ["abc", "def"]):
    print("Input :", words)
    print("Output:", repr(first_palindrome(words)))
