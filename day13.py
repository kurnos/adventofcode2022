from itertools import chain
from functools import cmp_to_key
from operator import lt

parse = lambda d: eval("[" + d.replace("\n\n", "],[").replace("\n", ",") + "]")
class Types:
    int = int
    list = list

def coerce(a, b):
    match (type(a), type(b)):
        case [Types.int, Types.int]: return a,b
        case [Types.list, Types.list]: 
            a,b = a[:],b[:]
            for i, (A, B) in enumerate(zip(a, b)):
                a[i], b[i] = coerce(A, B)
            return a,b
        case [Types.list, Types.int]: return coerce(a, [b])
        case [Types.int, Types.list]: return coerce([a], b)

cmp = lambda a,b: 1 - 2*lt(*coerce(a,b))

data = open("data/day13").read()

print(x:=sum(n for n, (a,b) in enumerate(parse(data), 1) if lt(*coerce(a,b))), x==4894)

packets = sorted(chain(chain.from_iterable(parse(data)), [[[2]], [[6]]]), key=cmp_to_key(cmp))
print(x:=(packets.index([[2]])+1)*(packets.index([[6]])+1), x==24180)