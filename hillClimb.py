
import random

tsp = [
    [0, 400, 500, 300],
    [400, 0, 300, 500],
    [500, 300, 0, 400],
    [300, 500, 400, 0]
]

def distance(route):
    total = 0
    for i in range(len(route)):
        total += tsp[route[i - 1]][route[i]]
    return total

def neighbours(route):
    result = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            r = route.copy()
            r[i], r[j] = r[j], r[i]
            result.append(r)
    return result

def hillClimbing():
    route = list(range(len(tsp)))
    random.shuffle(route)
    cost = distance(route)

    while True:
        near = neighbours(route)
        best = min(near, key=distance)

        if distance(best) >= cost:
            return route, cost

        route = best
        cost = distance(route)

print(hillClimbing())
