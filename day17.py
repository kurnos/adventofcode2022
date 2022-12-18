from itertools import count
from typing import Dict, FrozenSet, List, Tuple

rocks: List[List[Tuple[int, int]]] = [
    [(0,0), (1,0), (2,0), (3,0)],
    [(1,2), (0,1), (1,1), (2,1), (1,0)],
    [(2,2), (2,1), (0,0), (1,0), (2,0)],
    [(0,3), (0,2), (0,1), (0,0)],
    [(0,1), (0,0), (1,1), (1,0)],
]

rock_at = lambda ri, p: {(x+p[0], y+p[1]) for x,y in rocks[ri]}

State = Tuple[FrozenSet[Tuple[int,int]], int, int] # normalized chute, rock_index, jet_index

init: State = (frozenset((x,-1) for x in range(7)), 0, 0)

class Volcano(object):
    jets:str
    truncate:0

    def __init__(self, jets, truncate):
        self.jets = jets
        self.truncate = truncate

    def rocks_height(self, N) -> int:
        s, height = init, 0
        cache: Dict[State, Tuple[State, int]] = {}
        # make cache
        for n in range(N):
            if s not in cache:
                new_s, g = v.drop_rock(s)
                cache[s], s = (new_s, g), new_s
            else:
                break
            height += g

        # find cycle length
        s0, sx, cycle_height = s, s, 0
        for cycle_length in count(1):
            sx, h = cache[sx]
            cycle_height += h
            if sx == s0:
                break

        # fast forward cycles
        T = (N-n)//cycle_length
        n += T * cycle_length
        height += T * cycle_height

        # run the last part normally
        for n in range(n, N):
            s, h = cache[s]
            height += h

        return height

    def drop_rock(self, state: State) -> Tuple[State, int]: # state, growth
        chute, rock_index, jet_index = state
        top = max(y for _, y in chute)
        p = [2, top+4]

        while True:
            dx = -1 if self.jets[jet_index] == '<' else 1
            jet_index = (jet_index + 1) % len(self.jets)
            new_p = (p[0] + dx, p[1])
            if all(0 <= x < 7 for x,_ in rock_at(rock_index, new_p)) and not chute & rock_at(rock_index, new_p):
                p = new_p
            new_p = (p[0], p[1]-1)
            if not chute & rock_at(rock_index, new_p):
                p = new_p
            else:
                new_chute = chute | rock_at(rock_index, p)
                return ((self.normalize_chute(new_chute), (rock_index+1) % len(rocks), jet_index), max(y for _, y in new_chute) - top)

    def normalize_chute(self, chute) -> State:
        highpoint = max(y for _, y in chute)
        return frozenset((x,y - highpoint + self.truncate) for x,y in chute if highpoint - self.truncate <= y)

v = Volcano(open("data/day17").read(), 64)
print(x := v.rocks_height(2022), x == 3168)
print(x := v.rocks_height(1000000000000), x == 1554117647070)
