import re
with open("d05/input") as file:
    stack_strings, moves = (x.splitlines() for x in file.read().strip('\n').split('\n\n'))
    


stacks = {int(digit):[] for digit in stack_strings[-1].replace(' ', '')}
indexes = [index for index, char in enumerate(stack_strings[-1]) if char != ' ']


def fillStacks():
    for string in stack_strings[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] != " ": 
                stacks[stack_num].insert(0,string[index])
            stack_num += 1
fillStacks()

def move_crates():
    for idx, move in enumerate(moves):
        move  = [x for x in re.sub(r'[a-zA-Z]', "",move).strip().split(" ") if x != ""]
        move  = [int(x) for x in move]
        crates     = move[0]
        from_stack = move[1]
        to_stack   = move[2]
        for crate in range(crates):
            crate_removed = stacks[from_stack].pop()
            stacks[to_stack].append(crate_removed)

def moveCratesPuzzleTwo():
    for idx, move in enumerate(moves):
        move  = [x for x in re.sub(r'[a-zA-Z]', "",move).strip().split(" ") if x != ""]
        move  = [int(x) for x in move]
        crates     = move[0]
        from_stack = move[1]
        to_stack   = move[2]
        crates_to_remove = stacks[from_stack][-crates:]
        stacks[from_stack] = stacks[from_stack][:-crates]
        for crate in crates_to_remove:
            stacks[to_stack].append(crate)

def solvePuzzleOne():
    move_crates()
    result = ""
    for stack in stacks:
        result += stacks[stack][-1]
    return result

def solvePuzzleTwo():
    moveCratesPuzzleTwo()
    result = ""
    for stack in stacks:
        result += stacks[stack][-1]
    return result


print(solvePuzzleTwo())
