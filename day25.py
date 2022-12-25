def conv(snafu):
    res = 0
    for c in snafu:
        res *= 5
        match c:
            case "1": res += 1
            case "2": res += 2
            case "-": res -= 1
            case "=": res -= 2
    return res

def inv(n):
    res = []
    while n > 0:
        match n % 5:
            case 0: res.append("0")
            case 1: res.append("1"); n -= 1
            case 2: res.append("2"); n -= 2
            case 3: res.append("="); n += 2
            case 4: res.append("-"); n += 1
        n //= 5
    return "".join(reversed(res))

data = open("data/day25").read()

print(inv(sum(conv(line) for line in data.split("\n"))))