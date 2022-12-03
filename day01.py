def solve(data):
    elves = [sum(int(f) for f in s.split())
             for s in data.split("\n\n")]
    print("a", max(elves))
    print("b", sum(sorted(elves)[-3:]))


if __name__ == "__main__":
    solve(open("data/day01").read())
