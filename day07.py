import itertools
import collections

def solve(data):
    cwd = []
    dirs = collections.defaultdict(int)
    for line in data.split("\n"):
        if line == "$ cd ..":
            cwd.pop()
        elif line.startswith("$ cd "):
            cwd.append(line[5:])
        elif line.startswith("$ ls") or line.startswith("dir"):
            pass
        else:
            size, fname = line.split()
            for i in range(1, len(cwd)+1):
                dirs[tuple(cwd[:i])] += int(size)

    print(sum(v for v in dirs.values() if v < 100_000))
    need_to_free = dirs[('/',)] - 40000000
    print(min(v for v in dirs.values() if v > need_to_free))

if __name__ == '__main__':
    solve(open("data/day07").read())