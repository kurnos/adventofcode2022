from itertools import count, chain

def make_board(data):
    result = set({})
    for line in data.split("\n"):
        ps = [(int((x:=list(p.split(",")))[0]), int(x[1])) for p in line.split(" -> ")]
        for i in range(len(ps)-1):
            result.update(
                ((ps[i][0], y) for y in range(min(ps[i][1], ps[i+1][1]), max(ps[i][1], ps[i+1][1])+1))
                if ps[i][0] == ps[i+1][0] else
                ((x, ps[i][1]) for x in range(min(ps[i][0], ps[i+1][0]), max(ps[i][0], ps[i+1][0])+1))
            )
    return result

ddown = lambda board, max_y, x0, y0: next(((x0,y) for y in range(y0, max_y+1) if (x0,y+1) in board), (x0, max_y))
dleft = lambda board, x0, y0: next((x0-n,y0+n) for n in count() if (x0-n,y0+n+1) not in board or (x0-n-1, y0+n+1) in board)
dright = lambda board, x0, y0: next((x0+n,y0+n) for n in count() if (x0+n,y0+n+1) not in board or (x0+n+1, y0+n+1) in board)

def drop_stack(board, stack, max_y):
    if (down := ddown(board, max_y, *stack[-1])) != stack[-1]:
        stack.append(down)
    elif (left := dleft(board, *stack[-1])) != stack[-1]:
        stack.append(left)
    elif (right := dright(board, *stack[-1])) != stack[-1]:
        stack.append(right)
    else:
        board.add(stack.pop())

def drop(board):
    stack, c, max_y = [(500,0)], len(board), max(p[1] for p in board) + 1
    while stack[-1][1] != max_y:
        drop_stack(board, stack, max_y)
    return len(board) - c

def drop2(board):
    stack, c, max_y = [(500,0)], len(board), max(p[1] for p in board) + 1
    while stack:
        if stack[-1][1] == max_y:
            board.add(stack.pop())
        else:
            drop_stack(board, stack, max_y)
    return len(board) - c

board = make_board(open("data/day14").read())
print(x:=drop(set(board)), x==1072)
print(x:=drop2(board), x==24659)
    