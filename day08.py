from itertools import product

example = '''\
30373
25512
65332
33549
35390'''

def solvea(data):
    trees = data.split("\n")
    def seen(it):
        height = -1
        for x in it:
            if (h := int(trees[x[0]][x[1]])) > height:
                height = h
                yield (x[1], x[0])
            elif h == 9:
                break

    visible = set()

    for row in range(len(trees)):
        visible.update(seen((row, c) for c in range(len(trees[0]))))
        visible.update(seen((row, c) for c in reversed(range(len(trees[0])))))

    for col in range(len(trees[0])):
        visible.update(seen((r, col) for r in range(len(trees))))
        visible.update(seen((r, col) for r in reversed(range(len(trees)))))

    return len(visible)


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


if __name__ == "__main__":
    # solve(example)
    print(x := solvea(open("data/day08").read()), x == 1859)
    print(x := solveb(open("data/day08").read()), x == 332640)