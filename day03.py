from collections import Counter


def solve(data):
    sacks = data.split('\n')
    def prio(c): return ord(c) - 96 if c >= 'a' else ord(c)-38

    print(sum(
        prio((set(sack[:len(sack)//2]) & set(sack[len(sack)//2:])).pop())
        for sack in sacks
    ))
    print(sum(
        prio((set(sacks[i]) & set(sacks[i+1]) & set(sacks[i+2])).pop())
        for i in range(0, len(sacks), 3)
    ))


if __name__ == '__main__':
    solve(open("data/day03").read())
