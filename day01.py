def solve():
    elves = [sum(int(f) for f in s.split()) for s in open("data/day01").read().split("\n\n")]
    print("a", max(elves))
    print("b", sum(sorted(elves)[-3:]))


if __name__ == "__main__":
    solve()