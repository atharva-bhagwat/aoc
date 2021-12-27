import sys

input = open(sys.argv[1],'r').read().strip().split('\n')

# part 1
location = [0,0]
for command in input:
    dir, val = command.split(' ')
    if dir == 'up':
        location[1] -= int(val)
    elif dir == 'down':
        location[1] += int(val)
    else:
        location[0] += int(val)
print(f'Part 1: {location[0]*location[1]}')

# part 2
location = [0,0]
aim = 0
for command in input:
    dir, val = command.split(' ')
    if dir == 'up':
        aim -= int(val)
    elif dir == 'down':
        aim += int(val)
    else:
        location[0] += int(val)
        location[1] += int(val)*aim
print(f'Part 2: {location[0]*location[1]}')