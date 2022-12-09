def move_rope(rope, move, visited):
    for _ in range(int(move[2:])):
        rope[0] = move_head(rope[0], move[0])
        for i in range(1, len(rope)):
            prev = rope[i]
            rope[i] = move_tail(rope[i], rope[i-1])
            assert max((abs(prev[0] - rope[i][0]), abs(prev[1] - rope[i][1]))) <= 1, (prev, rope[i-1])
        visited.add(rope[-1])

def move_head(head, dir):
    if dir == 'L': return (head[0]-1, head[1])
    if dir == 'R': return (head[0]+1, head[1])
    if dir == 'U': return (head[0], head[1]-1)
    if dir == 'D': return (head[0], head[1]+1)

def move_tail(tail, head):
    d = (tail[0]-head[0], tail[1]-head[1])
    if abs(d[0]) > 1 or abs(d[1]) > 1:
        if d[0] == 0 or d[1] == 0:
            return (tail[0] - d[0]//2, tail[1]-d[1]//2)
        if abs(d[0]) == 2 and abs(d[1]) == 2:
            return (tail[0] - d[0]//2, tail[1] - d[1]//2)
        if abs(d[1]) == 2:
            return (tail[0] - d[0], tail[1]-d[1]//2)
        if abs(d[0]) == 2:
            return (tail[0] - d[0]//2, tail[1]-d[1])
    return tail

data = open("data/day09").read()

r = [(0,0)]*2
visited = set()
for move in data.split("\n"):
    move_rope(r, move, visited)
print(len(visited))

r = [(0,0)]*10
visited = set()
for move in data.split("\n"):
    move_rope(r, move, visited)
print(len(visited))
