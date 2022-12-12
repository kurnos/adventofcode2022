import heapq as hq

def parse(data):
    heights, start, end  = {}, None, None
    for y, row in enumerate(data.split("\n")):
        for x, c in enumerate(row):
            if c == "S":
                start,c = (x,y),'a'
            elif c == "E":
                end,c = (x,y), 'z'            
            heights[(x,y)] = ord(c) - ord('a')
    return heights, start, end

def dijkstra(s, traversable):
    visited, weights, path, queue = set(), {s:0}, dict(), [(0,s)]
    while queue:
        g, u = hq.heappop(queue)
        visited.add(u)
        for v in [(u[0]-1,u[1]), (u[0]+1,u[1]), (u[0],u[1]-1), (u[0],u[1]+1)]:
            if traversable(u, v) and not v in visited:
                if v not in weights or g+1 < weights[v]:
                    weights[v] = g+1
                    path[v] = u
                    hq.heappush(queue, (g+1, v))
    return path, weights

    

data = open("data/day12").read()
heights, start, end = parse(data)
traversable = lambda a,b: a in heights and b in heights and heights[a] + 1 >= heights[b]

path, _ = dijkstra(start, traversable)
pos, i = end, 0
while pos in path:
    i += 1
    pos = path[pos]
print(x := i, x == 330)

_, weights = dijkstra(end, lambda a,b: traversable(b,a))
print(x := min(w for (p,w) in weights.items() if heights[p] == 0), x == 321)