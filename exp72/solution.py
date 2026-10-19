from bisect import bisect_right

def job_scheduling(start, end, profit):
    jobs = sorted(zip(end, start, profit))
    ends = [j[0] for j in jobs]
    dp = [0] * (len(jobs) + 1)
    for i, (e, s, p) in enumerate(jobs, 1):
        k = bisect_right(ends, s, 0, i - 1)
        dp[i] = max(dp[i - 1], dp[k] + p)
    return dp[-1]

print("Example 1 ->", job_scheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
print("Example 2 ->", job_scheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]))
