def solve(data):
    scoresA = {
        "A X": 1 + 3,
        "B X": 1 + 0,
        "C X": 1 + 6,

        "A Y": 2 + 6,
        "B Y": 2 + 3,
        "C Y": 2 + 0,

        "A Z": 3 + 0,
        "B Z": 3 + 6,
        "C Z": 3 + 3,
    }

    scoresB = {
        "A X": 3 + 0,
        "A Y": 1 + 3,
        "A Z": 2 + 6,

        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,

        "C X": 2 + 0,
        "C Y": 3 + 3,
        "C Z": 1 + 6,
    }
    print("a", sum(scoresA[d] for d in data.split("\n")))
    print("b", sum(scoresB[d] for d in data.split("\n")))

if __name__ == '__main__':
    solve(open("data/day02").read())