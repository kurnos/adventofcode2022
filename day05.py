def parse_board(board):
    stack_count = (board.index("\n") + 1)//4
    stacks = [[] for _ in range(stack_count)]

    for line in board.split("\n")[:-1]:
        for c in range(stack_count):
            x = line[c*4+1]
            if x != ' ':
                stacks[c].insert(0,x)
    return stacks

def solvea(data):
    board, moves = data.split("\n\n")
    stacks = parse_board(board)

    for move in moves.split("\n"):
        _, count, _, src, _, trg = move.split()
        for _ in range(int(count)):
            stacks[int(trg)-1].append(stacks[int(src)-1].pop())
    return "".join(s[-1] for s in stacks)

def solveb(data):
    board, moves = data.split("\n\n")
    stacks = parse_board(board)

    for move in moves.split("\n"):
        _, count, _, src, _, trg = move.split()
        stacks[int(trg)-1].extend(stacks[int(src)-1][-int(count):])
        del stacks[int(src)-1][-int(count):]

    return "".join(s[-1] for s in stacks)

def solve(data):
    print(solvea(data))
    print(solveb(data))


if __name__ == '__main__':
    solve(open("data/day05").read())