data = open("data/day01").read()

elves = [sum(int(f) for f in s.split()) for s in data.split("\n\n")]
print(x := max(elves), x == 70509)
print(x := sum(sorted(elves)[-3:]), x == 208567)
