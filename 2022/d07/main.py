## hello you there!!
import sys

def solvePuzzle():
    if len(sys.argv) < 2:
        print("you should pass a file path here")
        return
    commands = []
    with open(sys.argv[1]) as file:
        commands = [command.strip() for command in file.readlines()]
    processCommands(commands)

def processCommands(commands):
    path = "/"
    dirs = {"/": 0}
    spaceused = 0
    for command in commands:
        if command[0] == "$":
            if command[2:4] == "ls":
                pass
            elif command[2:4] == "cd":
                [path, dirs] = updatePath(command, path, dirs)
        elif command[0:3] == "dir":
            pass
        else:
            size  = int(command[:command.find(" ")])
            spaceused += size
            dirr = path
            for i in range(path.count("/")):
                if dirr != "":
                    dirs[dirr] += size
                    dirr = dirr[:dirr.rfind("/")]
    limit = 30000000 - (70000000 - spaceused)
    dirs["/"] = spaceused
    get_answers(dirs, limit)

def updatePath(command, path, dirs):
    if command[5:] == "/":
        path = "/"
    elif command[5:] == "..":
        path = path[:path.rfind("/")]
        if path == "": path = "/"
    else:
        dir_name = command[5:]
        if path == "/":
            path = path + dir_name
            dirs.update({path:0})
        else:
            path = path + "/" + dir_name
            dirs.update({path:0})
    return [path, dirs]


def get_answers(dirs, limit):
    total = 0
    valid_dirs = []
    smallest = 0
    for dirr in dirs:
        if dirr != "/":
            if dirs[dirr] <= 100000:
                total += dirs[dirr]
            if limit <= dirs[dirr]:
                valid_dirs.append(dirs[dirr])
    valid_dirs.append(dirs["/"])
    smallest = min(valid_dirs)
    print(f"answer one: {total}")
    print(f"answer two: {smallest}")


solvePuzzle()








