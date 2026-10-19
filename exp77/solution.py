def load(weights, cap):
    total, chosen = 0, []
    for w in sorted(weights, reverse=True):
        if total + w <= cap:
            total += w
            chosen.append(w)
    return total, chosen

for w, c in (([10, 20, 30, 40, 50], 60), ([5, 10, 15, 20, 25, 30], 50)):
    t, ch = load(w, c)
    print(f"weights={w}, capacity={c} -> maximum weight loaded = {t} (items {ch})")
