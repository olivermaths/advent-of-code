f = open('d01/input', 'r')
lines = f.readlines()
f.close()

elves_in = []
elf = []
first  = 0
second = 0
third  = 0


for line in lines:
    if(line != '\n'): elf.append(int(line.replace('\n','')))
    if(line == '\n' or line == lines[-1]):
        elves_in.append(elf)
        s = sum(elf)
        if s > first:
            third = second
            second = first
            first = s
        elif s > second:
            third = second
            second = s
        elif s > third:
            third = s
        elf = []
        continue

print(elves_in)
print([first, second, third])
print(sum([first, second, third]))


