class WordFilter:
    def __init__(self, words):
        self.d = {}
        for idx, w in enumerate(words):
            for i in range(len(w) + 1):
                for j in range(len(w) + 1):
                    self.d[(w[:i], w[j:])] = idx

    def f(self, pref, suff):
        return self.d.get((pref, suff), -1)

wf = WordFilter(["apple"])
print('WordFilter(["apple"]).f("a", "e") ->', wf.f("a", "e"))
wf2 = WordFilter(["apple", "ape", "apple"])
print('WordFilter(["apple","ape","apple"]).f("ap", "e") ->', wf2.f("ap", "e"), "(largest valid index)")
print('wf.f("b", "e") ->', wf.f("b", "e"))
