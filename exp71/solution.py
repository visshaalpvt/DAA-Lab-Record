def min_time(jobs, k):
    jobs = sorted(jobs, reverse=True)
    best = [sum(jobs)]
    loads = [0] * k

    def dfs(i, cur_max):
        if cur_max >= best[0]:
            return
        if i == len(jobs):
            best[0] = cur_max
            return
        seen = set()
        for w in range(k):
            if loads[w] in seen:
                continue
            seen.add(loads[w])
            loads[w] += jobs[i]
            dfs(i + 1, max(cur_max, loads[w]))
            loads[w] -= jobs[i]

    dfs(0, 0)
    return best[0]

for jobs, k in (([3, 2, 3], 3), ([1, 2, 4, 7, 8], 2)):
    print(f"jobs={jobs}, k={k} -> {min_time(jobs, k)}")
