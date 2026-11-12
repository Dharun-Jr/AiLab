graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [], 'E': [('D', 6)], 'D': [('G', 1)], 'G': []
}

h = {'A': 1, 'B': 6, 'C': 0, 'D': 1, 'E': 0, 'G': 0}

def astar(start, goal):
    open_set = {start}
    closed = set()
    g = {start: 0}
    parent = {start: start}

    while open_set:
        n = min(open_set, key=lambda v: g[v] + h[v])

        if n == goal:
            path = []
            while parent[n] != n:
                path.append(n)
                n = parent[n]
            path.append(start)
            print("Path found:", path[::-1])
            return

        open_set.remove(n)
        closed.add(n)

        for m, w in graph[n]:
            cost = g[n] + w
            if m not in g or cost < g[m]:
                g[m] = cost
                parent[m] = n
                closed.discard(m)
                open_set.add(m)

    print("Path does not exist!")

astar('A', 'G')