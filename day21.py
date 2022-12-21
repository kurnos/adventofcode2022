def parse(line):
    words = line.replace(":", "").split(" ")
    return (words[0], int(words[1])) if len(words) == 2 else words

def eval_op(lhs, op, rhs):
    match op:
        case "+": return lhs + rhs
        case "-": return lhs - rhs
        case "*": return lhs * rhs
        case "/": return lhs // rhs

def part1(data):
    monkeys = list(map(parse, data.split("\n")))
    values = {}
    while "root" not in values:
        for m in monkeys:
            if m[0] in values:
                continue
            if len(m) == 2:
                values[m[0]] = m[1]
            elif m[1] in values and m[3] in values:
                values[m[0]] = eval_op(values[m[1]], m[2], values[m[3]])
    return values["root"]

def expr(monkeys, name):
    if name == "humn":
        return name
    match monkeys[name]:
        case (n,): return n
        case [lhs, op, rhs]: 
            e = expr(monkeys, lhs), op, expr(monkeys, rhs)
            if type(e[0]) is int and type(e[2]) is int:
                return eval_op(e[0], op, e[2])
            return e

def part2(data):
    expressions = {m[0]: m[1:] for m in map(parse, data.split("\n"))}

    lhs = expr(expressions, expressions["root"][0])
    rhs = expr(expressions, expressions["root"][2])

    assert type(rhs) is int
    while lhs != "humn":
        a, op, b = lhs
        if type(b) is int:
            lhs = a
            match op:
                case "+": rhs = rhs-b # lhs+b = rhs => lhs = rhs-b
                case "-": rhs = rhs+b # lhs-b = rhs => lhs = rhs+b
                case "*": rhs = rhs//b # lhs*b = rhs => lhs = rhs/b
                case "/": rhs = rhs*b # lhs/b = rhs => lhs = rhs*b
        elif type(a) is int:
            lhs = b
            match op:
                case "+": rhs = rhs-a # a + lhs = rhs => lhs = rhs - a
                case "-": rhs = a-rhs # a - lhs = rhs => lhs = a - rhs
                case "*": rhs = rhs//a # a * lhs = rhs => lhs = rhs/a
                case "/": rhs = a//rhs # a / lhs = rhs => lhs = a/rhs
    return rhs


data = open("data/day21").read()
print(x:=part1(data), x == 286698846151845)
print(x:=part2(data), x == 3759566892641)