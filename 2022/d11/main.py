import sys

def solvePuzzle():
    if len(sys.argv) < 2:
        print("you may pass a file path here")
        return
    file = open(sys.argv[1])
    groups = file.read().strip().split("\n\n")
    file.close()
    monkeys = []

    for group in groups:
        lines = group.splitlines()
        monkey = []
        items = list(map(int, lines[1].split(": ")[1].split(", ")))
        operation = eval("lambda old:" + lines[2].split(" = ")[1])
        monkey.append(items)
        monkey.append(operation)
        for line in lines[3:]:
            test = int(line.split()[-1])
            monkey.append(test)
        monkeys.append(monkey)
    counts = [0] * len(monkeys)
    for _ in range(20):
        for idx, monkey in enumerate(monkeys):
            for item in monkey[0]:
                item = monkey[1](item)
                item //=3
                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                     monkeys[monkey[4]][0].append(item)
            counts[idx] += len(monkey[0])
            monkey[0] = []
    print(monkeys)
    print(counts)
    counts.sort()
    answerone = counts[-1] * counts[-2]
    print(answerone)


def solvePuzzleTwo():
    file = open(sys.argv[1])
    groups = file.read().strip().split("\n\n")
    file.close()
    monkeys = []

    for group in groups:
        lines = group.splitlines()
        monkey = []
        items = list(map(int, lines[1].split(": ")[1].split(", ")))
        operation = eval("lambda old:" + lines[2].split(" = ")[1])
        monkey.append(items)
        monkey.append(operation)
        for line in lines[3:]:
            test = int(line.split()[-1])
            monkey.append(test)
        monkeys.append(monkey)
    counts = [0] * len(monkeys)

    mod = 1
    for monkey in monkeys:
        mod *= monkey[2]


    for _ in range(10000):
        for idx, monkey in enumerate(monkeys):
            for item in monkey[0]:
                item = monkey[1](item)
                item %= mod
                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                     monkeys[monkey[4]][0].append(item)
            counts[idx] += len(monkey[0])
            monkey[0] = []
    print(monkeys)
    print(counts)
    counts.sort()
    answerone = counts[-1] * counts[-2]
    print(answerone)


solvePuzzle()
solvePuzzleTwo()
