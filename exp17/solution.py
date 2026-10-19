def champagne_tower(poured, query_row, query_glass):
    row = [float(poured)]
    for _ in range(query_row):
        nxt = [0.0] * (len(row) + 1)
        for k, v in enumerate(row):
            if v > 1:
                extra = (v - 1) / 2
                nxt[k] += extra
                nxt[k + 1] += extra
        row = nxt
    return min(1.0, row[query_glass])

for p, r, g in ((1, 1, 1), (2, 1, 1), (4, 2, 1)):
    print(f"poured={p}, query_row={r}, query_glass={g} -> {champagne_tower(p, r, g):.5f}")
