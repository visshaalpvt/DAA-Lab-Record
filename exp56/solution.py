def full_justify(words, W):
    res, i = [], 0
    while i < len(words):
        j, length = i, 0
        while j < len(words) and length + len(words[j]) + (j - i) <= W:
            length += len(words[j])
            j += 1
        line, gaps = words[i:j], j - i - 1
        if j == len(words) or gaps == 0:
            s = " ".join(line)
            s += " " * (W - len(s))
        else:
            q, r = divmod(W - length, gaps)
            s = "".join(w + " " * (q + (1 if g < r else 0)) for g, w in enumerate(line[:-1])) + line[-1]
        res.append(s)
        i = j
    return res

for words in (["This", "is", "an", "example", "of", "text", "justification."],
              ["What", "must", "be", "acknowledgment", "shall", "be"]):
    print("Input:", words, "maxWidth=16")
    for line in full_justify(words, 16):
        print(f'  "{line}"')
