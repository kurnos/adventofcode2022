from itertools import product

def parse(line: str) -> tuple[str, tuple[int, list[str]]]:
    valve = line[6:8]
    left, right = line.split("; ")
    rate = int(left[23:])
    targets = right.split(" ", 4)[-1].split(", ")
    return valve, (rate, targets)

def shortest_paths(tunnels):
    result = {}
    for t in tunnels:
        best, stack = {}, [(0, t)]
        while stack:
            i, c = stack.pop(0)
            for tt in tunnels[c][1]:
                if tt in best: continue
                best[tt] = i+1
                stack.append((i+1, tt))
        if t == "AA" or tunnels[t][0] > 0:
            result[t] = {x: d for x,d in best.items() if tunnels[x][0] > 0}
    return result

data = open("data/day16").read()

tunnels = dict(map(parse, data.split("\n")))
paths = shortest_paths(tunnels)

def best_sets(t, visited, current, results):
    f, v = current
    fvisited = frozenset(visited)
    if results.get(fvisited, 0) < f:
        results[fvisited] = f

    for new_v, dist in paths[v].items():
        new_t = t + dist + 1
        if new_v in visited or new_t >= 30: continue
        new_f = f + tunnels[new_v][0] * (30-new_t)
        visited.add(new_v)
        best_sets(new_t, visited, (new_f, new_v), results)
        visited.remove(new_v)

results = {}
best_sets(0, {"AA"}, (0, "AA"), results)
print("part1: ", x:=max(results.values()), x==1701)

results = {}
best_sets(4, {"AA"}, (0, "AA"), results)
print("part2: ", x:=max(af + bf for ((a, af), (b, bf)) in product(results.items(), repeat=2) if len(a&b)==1), x==2455)

