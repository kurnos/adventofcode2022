from itertools import product

blob = eval("{(" + open("data/day18").read().replace("\n", "),(") + ")}")

d6 = lambda c: {(c[0]+dx, c[1]+dy, c[2]+dz) for dx,dy,dz in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]}
d26 = lambda c: {(c[0]+dx, c[1]+dy, c[2]+dz) for dx,dy,dz in product([-1,0,1], repeat=3) if (dx,dy,dz) != (0,0,0)}

queue = [max((x+1, y, z) for (x,y,z) in blob)]
outside = set(queue)

while queue:
    p = queue.pop()
    for n in d6(p):
        if n in blob or n in outside: continue
        if blob & d26(n):
            queue.append(n)
            outside.add(n)

print(x := sum(len(d6(p) - blob) for p in blob), x==3498)
print(x := sum(len(d6(o) & blob) for o in outside), x==2008)