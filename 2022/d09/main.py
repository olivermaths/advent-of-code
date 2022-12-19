## hello you there!!
import sys

def solvePuzzle():
    if len(sys.argv) < 2:
        print("you should pass a file path here")
        return
    visited = set([(0,0)])
    head = [0,0]
    tail = [0,0]
    direction, moves = [0,0]
    file = open(sys.argv[1])
    lines = file.readlines()
    file.close()
    for line in lines:
        direction, moves = line.split()
        moves = int(moves)
        for _ in range(moves):
            dx = 1 if direction == "R" else -1 if direction == "L" else 0
            dy = 1 if direction == "U" else -1 if direction == "D" else 0
            head[0] += dx         
            head[1] += dy

            x = head[0] - tail[0]
            y = head[1] - tail[1]
            if abs(x) > 1 or abs(y) > 1:
                if x == 0:
                    tail[1] += y // 2
                elif y == 0:
                    tail[0] += x // 2
                else:
                    tail[0]  += 1 if x > 0 else -1
                    tail[1]  += 1 if y > 0 else -1
            visited.add(tuple(tail))
    print(len(visited))
    puzzleTwo(lines)


def puzzleTwo(lines):
    visited = set([(0,0)])
    rope = [[0,0] for _ in range(10)]

    direction, moves = [0,0]

    for line in lines:
        direction, moves = line.split()
        moves = int(moves)
        for _ in range(moves):
            dx = 1 if direction == "R" else -1 if direction == "L" else 0
            dy = 1 if direction == "U" else -1 if direction == "D" else 0
            rope[0][0] += dx         
            rope[0][1] += dy
            for i in range(9):
                head = rope[i]
                tail = rope[i + 1]
                x = head[0] - tail[0]
                y = head[1] - tail[1]
                if abs(x) > 1 or abs(y) > 1:
                    if x == 0:
                        tail[1] += y // 2
                    elif y == 0:
                        tail[0] += x // 2
                    else:
                        tail[0]  += 1 if x > 0 else -1
                        tail[1]  += 1 if y > 0 else -1
            visited.add(tuple(rope[-1]))
    print(len(visited))

solvePuzzle()