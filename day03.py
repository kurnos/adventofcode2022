from collections import Counter

data = open("data/day03").read()

sacks = data.split('\n')
prio = lambda c: ord(c) - 96 if c >= 'a' else ord(c)-38

print(x := sum(
    prio((set(sack[:len(sack)//2]) & set(sack[len(sack)//2:])).pop())
    for sack in sacks
), x == 8185)
print(x := sum(
    prio((set(sacks[i]) & set(sacks[i+1]) & set(sacks[i+2])).pop())
    for i in range(0, len(sacks), 3)
), x == 2817)
