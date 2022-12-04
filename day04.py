import itertools

def parse(line):
    a, b = line.split(",")
    a0, a1 = a.split("-")
    b0, b1 = b.split("-")
    return (int(a0), int(a1)), (int(b0), int(b1))


def contains(a, b):
    return b[0] >= a[0] and b[1] <= a[1]


def overlaps(a, b):
    return a[0] <= b[1] and a[1] >= b[0]


def solve(data):
    print(sum(contains(a, b) or contains(b, a)
          for (a,b) in map(parse, data.split("\n"))))
    print(sum(overlaps(*p) for p in map(parse, data.split("\n"))))


if __name__ == "__main__":
    solve(open("data/day04").read())
