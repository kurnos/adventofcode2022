
from itertools import chain
from collections import Counter, deque
from typing import Set, Tuple


def parse(data):
    return {(x,y) for y,row in enumerate(data.split("\n")) for x in range(len(row)) if row[x] == '#'}

def evolve(t, elves: Set[Tuple[int,int]]):
    proposals = {}
    for (x,y) in elves:
        if sum((u,v) in elves for u in range(x-1,x+2) for v in range(y-1,y+2)) == 1:
            continue
        p = deque([
            (x, y-1) if not {(x-1,y-1), (x,y-1), (x+1,y-1)} & elves else None, # North
            (x, y+1) if not {(x-1,y+1), (x,y+1), (x+1,y+1)} & elves else None, # South
            (x-1, y) if not {(x-1,y+1), (x-1,y), (x-1,y-1)} & elves else None, # West
            (x+1, y) if not {(x+1,y+1), (x+1,y), (x+1,y-1)} & elves else None, # East
        ])
        p.rotate(-t)
        p = list(filter(None, p))
        if p:
            proposals[x,y] = p[0]

    prop_count = Counter(proposals.values())

    if any(c == 1 for c in prop_count.values()):
        return {
            proposals[e] if e in proposals and prop_count[proposals[e]] == 1 else e
            for e in elves
        }

def empty_ground(elves):
    return sum(not (x,y) in elves 
        for x in range(min(x for (x,_) in elves), max(x for (x,_) in elves) + 1) 
        for y in range(min(y for (_,y) in elves), max(y for (_,y) in elves) + 1)
    )

data = open("data/day23").read()

elves = parse(data)
for t in range(0, 10):
    elves = evolve(t, elves)
print(x:=empty_ground(elves), x == 3940)

elves, t = parse(data), 0
while elves:
    elves,t = evolve(t, elves), t+1
print(t, t == 990)
