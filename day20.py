from collections import deque
from typing import Tuple

def parse(data):
    return eval("[" + data.replace("\n", ",") + "]")

def mix(cs: deque[Tuple[int,int]], i):
    cs.rotate(-cs.index(i))
    cs.popleft()
    cs.rotate(-i[1])
    cs.append(i)

def part1(numbers: list[int]):
    cs = deque(enumerate(numbers))
    for i in enumerate(numbers):
        mix(cs, i)

    z = cs.index((numbers.index(0), 0))
    return cs[(z+1000)%len(cs)][1] + cs[(z+2000)%len(cs)][1] + cs[(z+3000)%len(cs)][1]

def part2(numbers):
    cs = deque(enumerate(numbers))
    for i in range(10):
        for i in enumerate(numbers):
            mix(cs, i)

    z = cs.index((numbers.index(0), 0))
    return (cs[(z+1000)%len(cs)][1] + cs[(z+2000)%len(cs)][1] + cs[(z+3000)%len(cs)][1])
    
data = open("data/day20").read()
numbers: list[int] = parse(data)
print(x := part1(numbers), x == 27726)
print(x := part2([n*811589153 for n in numbers]), x == 4275451658004)