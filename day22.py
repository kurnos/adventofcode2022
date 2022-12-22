import re
from typing import NamedTuple, Tuple
from functools import reduce

up, down, left, right = (0,-1), (0,1), (-1,0), (1,0)

class State(NamedTuple):
    face: Tuple[int, int]
    pos: Tuple[int, int]
    dir: Tuple[int, int]

    def to_score(self):
        x, y = N*self.face[0] + self.pos[0] + 1, N*self.face[1] + self.pos[1] + 1
        return 1000*y + 4*x + {(0,1): 1, (0,-1): 3, (1,0): 0, (-1,0): 2}[self.dir]

def parse(data, n):
    grid, instr = data.split("\n\n")
    lines = grid.split("\n")
    faces = {
        (ci, ri): [row[n*ci:n*ci+n] for row in lines[n*ri:n*ri+n]]
        for ri in range(0, len(lines)//n)
        for ci in range(0, len(lines[n*ri])//n)
        if lines[n*ri][n*ci] in ".#"
    }
    moves = [
        int(m) if i % 2 == 0 else m
        for i, m in enumerate(re.split(r"(L|R)", instr))
    ]
    return faces, moves

N, data = 50, open("data/day22").read()

# for my puzzle input, lovingly hand calculated
# for part 1
A,B,C,D,E,F = (1, 0), (2, 0), (1, 1), (0, 2), (1, 2), (0, 3)
links1 = {
    (A, up): (E, down),
    (A, right): (B, left),
    (A, down): (C, up),
    (A, left): (B, right),
    (B, up): (B, down),
    (C, left): (C, right),
    (C, down): (E, up),
    (D, up): (F, down),
    (D, left): (E, right),
    (D, right): (E, left),
    (D, down): (F, up),
    (F, left): (F, right),
}
for a,b in list(links1.items()): links1[b] = a


links2 = {
    (A, up): (F, left),
    (A, right): (B, left),
    (A, down): (C, up),
    (A, left): (D, left),
    (B, up): (F, down),
    (B, right): (E, right),
    (B, down): (C, right),
    (C, left): (D, up),
    (C, down): (E, up),
    (D, right): (E, left),
    (D, down): (F, up),
    (E, down): (F, right)
}
for a,b in list(links2.items()): links2[b] = a

faces, moves = parse(data, N)

def square_at(s: State) -> str:
    return faces[s.face][s.pos[1]][s.pos[0]]

tr = lambda p: (p[1], p[0])
flipX = lambda p: (N - 1 - p[0], p[1])
flipY = lambda p: (p[0], N - 1 - p[1])

transformations = {
    (up, up): flipX,
    (right,left): flipX,
    (down,down): flipX,

    (up, down): flipY, 
    (right,right): flipY,
    (left,left): flipY,

    (up, left): tr,
    (right,down): tr,

    (up, right): lambda p: flipY(tr(flipY(p))),
    (down,left): lambda p: flipY(tr(flipY(p))),
}
for (a,b) in list(transformations.items()):
    transformations[a[1],a[0]] = b

def advance(links, s: State):
    next_pos = (s.pos[0]+s.dir[0],s.pos[1]+s.dir[1])
    if 0 <= next_pos[0] < N and 0 <= next_pos[1] < N:
        return s._replace(pos=next_pos)
    else:
        next_face, next_dir = links[s.face,s.dir]
        next_pos = transformations[s.dir, next_dir](s.pos)

        return State(face=next_face, pos=next_pos, dir=(-next_dir[0], -next_dir[1]))

def move_cube(links, s: State, m) -> State:
    match m:
        case 'L': return s._replace(dir=(s.dir[1], -s.dir[0]))
        case 'R': return s._replace(dir=(-s.dir[1], s.dir[0]))
        case i:
            for _ in range(i):
                new_state = advance(links, s)
                if square_at(new_state) == '.':
                    s = new_state
                else:
                    break
            return s

start = State(A, (0,0), right)
print(x := reduce(lambda s, m: move_cube(links1, s, m), moves, start).to_score(), x == 149138)
print(x := reduce(lambda s, m: move_cube(links2, s, m), moves, start).to_score(), x == 153203)
