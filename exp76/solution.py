import heapq

class Node:
    def __init__(self, f, ch=None, l=None, r=None):
        self.f, self.ch, self.l, self.r = f, ch, l, r

def build(chars, freqs):
    pq = [(f, i, Node(f, c)) for i, (c, f) in enumerate(zip(chars, freqs))]
    heapq.heapify(pq)
    cnt = len(pq)
    while len(pq) > 1:
        f1, _, a = heapq.heappop(pq)
        f2, _, b = heapq.heappop(pq)
        heapq.heappush(pq, (f1 + f2, cnt, Node(f1 + f2, None, a, b)))
        cnt += 1
    return pq[0][2]

def codes(node, pre="", out=None):
    if out is None:
        out = {}
    if node.ch is not None:
        out[node.ch] = pre or "0"
    else:
        codes(node.l, pre + "0", out)
        codes(node.r, pre + "1", out)
    return out

def decode(root, bits):
    out, cur = [], root
    for b in bits:
        cur = cur.l if b == "0" else cur.r
        if cur.ch is not None:
            out.append(cur.ch)
            cur = root
    return "".join(out)

for t, (ch, fr, msg) in enumerate(((list("abcd"), [5, 9, 12, 13], "abacd"),
                                     (list("fedcba"), [5, 9, 12, 13, 16, 45], "fcbade")), 1):
    root = build(ch, fr)
    cd = codes(root)
    enc = "".join(cd[c] for c in msg)
    print(f"Test Case {t}:")
    print("  codes   :", sorted(cd.items()))
    print("  encoded :", enc)
    print("  decoded :", decode(root, enc))
