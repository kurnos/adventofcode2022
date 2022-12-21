from typing import NamedTuple

class Materials(NamedTuple):
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    def __add__(self, other):
        return Materials(*(a+b for (a,b) in zip(self, other)))

    def __sub__(self, other):
        return Materials(*(a-b for (a,b) in zip(self, other)))

    def __mul__(self, m):
        return Materials(*(a*m for a in self))

    def __ge__(self, other):
        return all(a >= b for a,b in zip(self, other))

class State(NamedTuple):
    t: int
    mats: Materials
    prod: Materials

def parse(line):
    words = line.split()
    return {
        Materials(geode=1): Materials(ore=int(words[27]), obsidian=int(words[30])),
        Materials(obsidian=1): Materials(ore=int(words[18]), clay=int(words[21])),
        Materials(clay=1): Materials(ore=int(words[12])),
        Materials(ore=1): Materials(ore=int(words[6])),
    }

def run(bp, init:State, N):
    max_c = tuple(max(v[i] for v in bp.values()) for i in range(4))

    visited = set()
    queue = [init]
    while queue:
        s = queue.pop()
        if s.t == N:
            yield s.mats.geode
            continue
        for p, c in bp.items():
            x = s.prod+p
            if x[0] > max_c[0] or x[1] > max_c[1] or x[2] > max_c[2]:
                continue

            new_s = s
            while new_s.t < N:
                if new_s.mats >= c: 
                    new_s = State(new_s.t+1, new_s.mats + new_s.prod - c, new_s.prod + p)

                    if new_s not in visited:
                        visited.add(new_s)
                        queue.append(new_s)
                    break
                new_s = State(new_s.t+1, new_s.mats + new_s.prod, new_s.prod)
    print("visited", len(visited))

data = open("data/day19").read()

blueprints = [parse(line) for line in data.split("\n")]

s = State(0, Materials(), Materials(ore=1))

total = 0
for id, bp in enumerate(blueprints, 1):
    geodes = max(run(bp, s, 24))
    print(id, geodes, "->", geodes*id)
    total += geodes*id
print(x := total, x == 2341)

total = 1
for id, bp in enumerate(blueprints[:3], 1):
    geodes = max(run(bp, s, 32))
    print(id, geodes)
    total *= geodes
print(x := total, x == 3689)