import sys

input = [int(x) for x in open(sys.argv[1],'r').readlines()]

# part 1
pairs = zip(input, input[1:])
increases = [b - a for a,b in pairs if b - a > 0]
print(f'Part 1: {len(increases)}')

# part 2
windows = [sum(window) for window in zip(input, input[1:], input[2:])]
pairs = zip(windows, windows[1:])
increases = [b - a for a,b in pairs if b - a > 0]
print(f'Part 2: {len(increases)}')