import sys
from pprint import pprint

def read():
    input, instructions_txt = open(sys.argv[1], 'r').read().strip().split('\n\n')

    input = input.split('\n')

    dot_loc = []

    nrow = ncol = 0

    for entry in input:
        x, y = entry.split(',')
        dot_loc.append([int(x), int(y)])
        nrow = max(nrow, int(y))
        ncol = max(ncol, int(x))

    nrow += 1
    ncol += 1

    paper = [["."] * ncol for _ in range(nrow)]

    for x, y in dot_loc:
        paper[y][x] = '#'

    instructions_raw = instructions_txt.split('\n')
    instructions = []

    for instruction in instructions_raw:
        axis, val = instruction.split(' ')[-1].split('=')
        instructions.append([axis, int(val)])

    return paper, instructions

def fold(paper, axis, val):
    if axis == 'x':
        # vertical
        split = [x[val + 1 :][::-1] for x in paper]
        paper = [x[:val] for x in paper]
        # adjust for uneven folds
        if len(split[0]) > len(paper[0]):
            paper = [["."] * len(split[0]) - len(paper[0]) + paper for _ in paper]
        elif len(paper) > len(split):
            split = [["."] * len(paper[0]) - len(split[0]) + split for _ in split]
    else:
        # horizontal
        split = paper[val + 1 :][::-1]
        paper = paper[:val]
        # adjust for uneven folds
        if len(split) > len(paper):
            paper = [["."] * len(split[0])] * (len(split) - len(paper)) + paper
        elif len(paper) > len(split):
            split = [["."] * len(paper[0])] * (len(paper) - len(split)) + split

    for y in range(len(paper)):
        for x in range(len(paper[0])):
            if split[y][x] == "#":
                paper[y][x] = "#"
    return paper

def part1():
    paper, instructions = read()
    axis, val = instructions[0]
    paper = fold(paper, axis, val)

    print(f'Part 1: {sum([line.count("#") for line in paper])}')

def print_code(paper):
    for row in paper:
        print("".join([' ' if x == '.' else '#' for x in row]))

def part2():
    paper, instructions = read()
    for axis, val in instructions:
        paper = fold(paper, axis, val)

    print_code(paper)
        
part1()
part2()