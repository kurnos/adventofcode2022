def solve(data, d):
    for i in range(len(data)-d):
        if len(set(data[i:i+d])) == d:
            return i+d

assert solve("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4) == 7
assert solve("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
assert solve("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
assert solve("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
assert solve("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11


assert solve("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
assert solve("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
assert solve("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
assert solve("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
assert solve("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26

if __name__ == '__main__':
    print(solve(open("data/day06").read(), 4))
    print(solve(open("data/day06").read(), 14))