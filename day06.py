solve = lambda data, d: next(i+d for i in range(len(data)-d) if len(set(data[i:i+d])) == d)

print(x := solve(open("data/day06").read(), 4), x == 1566)
print(x := solve(open("data/day06").read(), 14), x == 2265)