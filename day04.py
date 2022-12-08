import itertools, re

parse = lambda line: list(map(int, re.split("[-,]", line)))

data = open("data/day04").read() 

print(x := sum(x[2] >= x[0] and x[3] <= x[1] or x[0] >= x[2] and x[1] <= x[3] for x in map(parse, data.split("\n"))), x == 448)
print(x := sum(x[0] <= x[3] and x[1] >= x[2] for x in map(parse, data.split("\n"))), x == 794)
