import itertools, operator

def solve(data):
    cwd, dirs = [], {}
    for line in itertools.chain(data.split("\n"), itertools.repeat("$ cd ..")):
        if line == "$ cd ..":
            dirs[tuple(n for n, _ in cwd)] = cwd[-1][1]
            if len(cwd) == 1: break
            _, size = cwd.pop()
            cwd[-1][1] += size

        elif line.startswith("$ cd "):
            cwd.append([line[5:], 0])
        elif not line.startswith("$ ls") and not line.startswith("dir"):
            size, fname = line.split()
            cwd[-1][1] += int(size)

    need_to_free = dirs[('/',)] - 40000000
    return sum(v for v in dirs.values() if v < 100_000), min(v for v in dirs.values() if v > need_to_free)

print(x := solve(open("data/day07").read()), x == (1543140, 1117448))