def next_fit(weights, cap):
    bins, cur = 1, 0
    for w in weights:
        if cur + w > cap:
            bins += 1
            cur = 0
        cur += w
    return bins

def first_fit_decreasing(weights, cap):
    bins = []
    for w in sorted(weights, reverse=True):
        for i in range(len(bins)):
            if bins[i] + w <= cap:
                bins[i] += w
                break
        else:
            bins.append(w)
    return len(bins)

for w, c in (([5, 10, 15, 20, 25, 30, 35], 50), ([10, 20, 30, 40, 50, 60, 70, 80], 100)):
    print(f"weights={w}, capacity={c}")
    print(f"  greedy (fill current container first): {next_fit(w, c)} containers")
    print(f"  first-fit decreasing (for comparison): {first_fit_decreasing(w, c)} containers")
