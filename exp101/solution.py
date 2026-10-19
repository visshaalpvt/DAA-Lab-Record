import time

def first_fit(items, cap):
    bins = []
    for w in items:
        for b in bins:
            if sum(b) + w <= cap:
                b.append(w)
                break
        else:
            bins.append([w])
    return bins

def best_fit(items, cap):
    bins = []
    for w in items:
        fits = [b for b in bins if sum(b) + w <= cap]
        if fits:
            min(fits, key=lambda b: cap - sum(b) - w).append(w)
        else:
            bins.append([w])
    return bins

items, cap = [4, 8, 1, 4, 2, 1], 10
for name, fn, data in (("First-Fit", first_fit, items), ("Best-Fit", best_fit, items),
                       ("First-Fit Decreasing", first_fit, sorted(items, reverse=True))):
    t0 = time.perf_counter()
    bins = fn(data, cap)
    dt = (time.perf_counter() - t0) * 1e6
    print(f"{name}: Number of Bins Used: {len(bins)}  ->  " + ", ".join(f"Bin {i + 1}: {b}" for i, b in enumerate(bins)) + f"   (time {dt:.1f} microseconds)")
print("Lower bound = ceil(total weight / capacity) =", -(-sum(items) // cap))
