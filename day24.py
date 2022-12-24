import heapq
from typing import FrozenSet, List, NamedTuple, Tuple


class State(NamedTuple):
    t: int
    stage: int
    pos: Tuple[int, int]
    size: Tuple[int, int]
    rights: FrozenSet[Tuple[int, int]]
    downs: FrozenSet[Tuple[int, int]]
    lefts: FrozenSet[Tuple[int, int]]
    ups: FrozenSet[Tuple[int, int]]

def parse(data):
    blizzards = {">": set(), "<": set(), "^": set(), "v":set()}
    for y, line in enumerate(data.split("\n")):
        for x, c in enumerate(line):
            if c in blizzards:
                blizzards[c].add((x,y))
    return blizzards, (data.index('\n'), len(data.split('\n')))

def display(s: State):
    X,Y = s.size

    def blizzards_at(pos):
        bs = []
        if pos in s.lefts: bs.append("<")
        if pos in s.rights: bs.append(">")
        if pos in s.ups: bs.append("^")
        if pos in s.downs: bs.append("v")
        if len(bs) == 1:
            return bs[0]
        return str(len(bs))
   
    print()
    for y in range(0, Y):
        print("".join(
            "E" if s.pos == (x,y) else
            "#" if x == 0 or y == 0 or x == X-1 or y == Y-1 else
            b if (b := blizzards_at((x,y))) != "0" else
            "."
            for x in range(0,X)
        ))


def rotate(ps, size, d, n, cache={}):
    X,Y = size
    n = n % ((X-2)*(Y-2))
    if (hit := cache.get((ps, size, d, n), None)) is None:
        dx,dy = d
        hit = frozenset(((((x - 1 + dx*n) % (X-2)) + 1), (((y - 1 + dy*n) % (Y-2)) + 1)) for (x,y) in ps)
        cache[ps,size,d,n] = hit
    return hit

def advance(s: State):
    X,Y = s.size
    return s._replace(
        t=s.t + 1,
        stage= (
            1 if s.pos == (X-2, Y-1) and s.stage == 0 else
            2 if s.pos == (1,0) and s.stage == 1 else
            s.stage
        )
    )
      
def choices(s: State):
    (x,y) = s.pos
    (X,Y) = s.size
    if s.pos == (1,1):
        yield (1,0)
    elif s.pos == (1,0):
        yield s.pos
    elif (x,y) == (X-2,Y-2):
        yield (X-2,Y-1)
    elif s.pos == (X-2,Y-1):
        yield s.pos

    rights = rotate(s.rights, s.size, (1,0), s.t)
    lefts = rotate(s.lefts, s.size, (-1,0), s.t)
    ups = rotate(s.ups, s.size, (0,-1), s.t)
    downs = rotate(s.downs, s.size, (0,1), s.t)
    
    for p in [(x+1, y), (x-1,y), (x, y+1), (x, y-1), (x,y)]:
        if 0 < p[0] < X-1 and 0 < p[1] < Y-1 and p not in rights and p not in lefts and p not in ups and p not in downs:
            yield p

def a_star_search(start: State):
    frontier: List[Tuple[int, State]] = [(0, start)]
    cost_so_far: dict[State, int] = {start: 0}
    
    while frontier:
        _, current = heapq.heappop(frontier)

        if current.stage == 2 and current.pos == (current.size[0]-2, current.size[1]-1):
            return current

        advanced = advance(current)
        for pos in choices(advanced):
            next = advanced._replace(pos=pos)
            new_cost = advanced.t
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                heuristic = (
                    abs(next.size[0] - next.pos[0] - 2) + abs(next.size[1] - next.pos[1] - 1) if current.stage % 2 == 0 else
                    abs(next.size[0] - 1) + abs(next.size[1] - next.pos[1])
                ) + (2-next.stage) * (next.size[1] + next.size[0]-2)
                heapq.heappush(frontier, (new_cost + heuristic, next))

data = open("data/day24").read()

blizzards, size = parse(data)
s = State(
    t=0,
    stage=0,
    size=size,
    pos=(1,0),
    rights=frozenset(blizzards[">"]),
    downs=frozenset(blizzards["v"]),
    lefts=frozenset(blizzards["<"]),
    ups=frozenset(blizzards["^"]),
)

print(x := a_star_search(s._replace(stage=2)).t, x == 232)
print(x := a_star_search(s).t, x == 715)