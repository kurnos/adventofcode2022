x = lambda c: ord(c) % 23 - 19 # maps ABC and XYZ to 012
def scoreA(line):
    elf, me = x(line[0]), x(line[2])
    return 1 + me + ((me - elf + 1) % 3)*3

def scoreB(line):
    elf, result = x(line[0]), x(line[2])
    return 1 + (2 + elf + result) % 3 + result * 3

def solve(data):
    print("a", sum(scoreA(d) for d in data.split("\n")))
    print("b", sum(scoreB(d) for d in data.split("\n")))

if __name__ == '__main__':
    solve(open("data/day02").read())
