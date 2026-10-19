# Exp 92: Hamiltonian Cycle (5 vertices)

## Aim
To determine whether an undirected graph has a Hamiltonian cycle using backtracking.

## Algorithm
1. Start the path at vertex 0
2. Extend the path with an unused vertex adjacent to the last vertex
3. When all n vertices are in the path, check that the last vertex is adjacent to vertex 0 (cycle closes)
4. If no extension works, remove the last vertex (backtrack)
5. Return the cycle or False

## Input
```
n = 5
edges = [(0,1),(1,2),(2,3),(3,0),(0,2),(2,4),(4,0)]
```

## Program
[`solution.py`](solution.py)

```python
def hamiltonian_cycle(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    path, used = [0], [False] * n
    used[0] = True
    def bt():
        if len(path) == n:
            return 0 in adj[path[-1]]
        for v in sorted(adj[path[-1]]):
            if not used[v]:
                used[v] = True
                path.append(v)
                if bt():
                    return True
                path.pop()
                used[v] = False
        return False
    return path + [0] if bt() else None

n, edges = 5, [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (2, 4), (4, 0)]
cyc = hamiltonian_cycle(n, edges)
print("Hamiltonian Cycle Exists:", cyc is not None, "" if cyc is None else f"(Example cycle: {' -> '.join(map(str, cyc))})")
```

## Output
```
Hamiltonian Cycle Exists: False
```

## Screenshot
![Output screenshot](output.png)

## Result
The program for **Hamiltonian Cycle (5 vertices)** was implemented and executed successfully, and the output shown above was obtained for all the given test cases.

> **Note:** In this graph vertices 1, 3 and 4 each have only the neighbours 0 and 2, so a cycle through all three would need vertices 0 and 2 to have degree 3. No Hamiltonian cycle exists, so the correct output is False (the sheet's cycle uses the non-existent edge 4-3).

## Time and Space Complexity
| | Complexity |
|---|---|
| **Time** | O(n!) |
| **Space** | O(n) |
