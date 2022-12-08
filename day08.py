from itertools import product, chain

def solvea(data):
    trees = data.split("\n")
    def seen(it):
        height = -1
        for x in it:
            if (h := int(trees[x[0]][x[1]])) > height:
                height = h
                yield (x[1], x[0])

    return len(set(chain.from_iterable(
        chain(
            (seen((x, c) for c in range(len(trees)))),
            (seen((x, c) for c in reversed(range(len(trees))))),
            (seen((r, x) for r in range(len(trees)))),
            (seen((r, x) for r in reversed(range(len(trees))))),
        )
        for x in range(len(trees))
    )))

def solveb(data):
    trees = data.split("\n")
    def score(row, col):
        h = int(trees[row][col])
        return (
            next((i-col for i in range(col+1, len(trees[0])) if int(trees[row][i]) >= h), len(trees[0]) - col - 1)
            * next((col-i for i in reversed(range(col)) if int(trees[row][i]) >= h), col)
            * next((i-row for i in range(row+1, len(trees)) if int(trees[i][col]) >= h), len(trees) - row - 1)
            * next((row-i for i in reversed(range(row)) if int(trees[i][col]) >= h), row)
        )
    
    return max(score(row, col) for row in range(len(trees)) for col in range(len(trees[0])))

print(x := solvea(open("data/day08").read()), x == 1859)
print(x := solveb(open("data/day08").read()), x == 332640)