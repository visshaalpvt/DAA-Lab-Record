def string_matching(words):
    res = []
    for i, w in enumerate(words):
        for j, v in enumerate(words):
            if i != j and w in v:
                res.append(w)
                break
    return res

for words in (["mass", "as", "hero", "superhero"], ["leetcode", "et", "code"], ["blue", "green", "bu"]):
    print(words, "->", string_matching(words))
