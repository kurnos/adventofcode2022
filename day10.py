from itertools import islice, accumulate, chain


def run(cmds): return chain.from_iterable(accumulate(
    cmds,
    lambda b, cmd: [(b[-1][0]+1, b[-1][1])] if cmd == "noop"
    else [(b[-1][0]+1, b[-1][1]), (b[-1][0]+2, b[-1][1] + int(cmd[4:]))],
    initial=[(1, 1)]))


data = open("data/day10").read()
print(sum(s*r for s, r in islice(run(data.split("\n")), 19, 220, 40)))
print("\n".join("".join('#' if abs(r - (s-1) % 40) <= 1 else '.' for s, r in line)
      for line in zip(*[run(data.split("\n"))]*40)))
