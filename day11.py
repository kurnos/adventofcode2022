from collections import namedtuple, Counter
from operator import add, mul
from math import lcm

Monkey = namedtuple("Monkey", "items op arg test true_n false_n")


def parse_monkey(m):
    lines = list(m.split("\n"))
    return Monkey(
        items=[int(i) for i in lines[1][18:].split(', ')],
        op={"+": add, "*": mul}[lines[2][23]],
        arg=lines[2][25:],
        test=int(lines[3][21:]),
        true_n=int(lines[4][29:]),
        false_n=int(lines[5][30:])
    )


def throw(monkeys, n, div, mod):
    m, throws = monkeys[n], len(monkeys[n].items)
    for i in m.items:
        i = (m.op(i, i if m.arg == "old" else int(m.arg)) // div) % mod
        monkeys[m.true_n if i % m.test == 0 else m.false_n].items.append(i)
    m.items.clear()
    return throws


def solve(monkeys, div, N):
    mod = lcm(*(m.test for m in monkeys))
    return mul(*sorted(sum((Counter({i: throw(monkeys, i, div, mod) for i in range(len(monkeys))})
                            for _ in range(N)), Counter()).values())[-2:])


data = open("data/day11").read()
print(x:= solve(list(map(parse_monkey, data.split("\n\n"))), 3, 20), x == 57348)
monkeys = list(map(parse_monkey, data.split("\n\n")))
print(x:= solve(list(map(parse_monkey, data.split("\n\n"))), 1, 10000), x == 14106266886)
