parse = lambda c: ord(c) % 23 - 19  # maps ABC and XYZ to 012
scoreA = lambda elf, me: 1 + me + ((me - elf + 1) % 3)*3
scoreB = lambda elf, result: 1 + (2 + elf + result) % 3 + result * 3

data = open("data/day02").read()
print(x := sum(scoreA(parse(d[0]), parse(d[2])) for d in data.split("\n")), x == 13221)
print(x := sum(scoreB(parse(d[0]), parse(d[2])) for d in data.split("\n")), x == 13131)