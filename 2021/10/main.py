import sys

input = open(sys.argv[1], 'r').read().strip().split('\n')

pairs = {
    '(':')',
    '[':']',
    '{':'}',
    '<':'>'
}

p1_score = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
}

p2_score = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}

def part1():
    global input
    fault = []
    corrupted = []
    for row in input:
        stack = []
        for char in row:
            if char in pairs:
                stack.append(char)
            else:
                if len(stack) == 0:
                    fault.append(char)
                    corrupted.append(row)
                    break
                top = stack.pop()
                if pairs[top] != char:
                    fault.append(char)
                    corrupted.append(row)
                    break

    points = 0
    for char in fault:
        points += p1_score[char]

    print(f'Part 1: {points}')

    input = [row for row in input if row not in corrupted]

def part2():
    all_points = []
    for row in input:
        stack = []
        autocomplete = []
        points = 0
        for char in row:
            if char in pairs:
                stack.append(char)
            else:
                if len(stack) == 0:
                    break
                top = stack.pop()
                if pairs[top] != char:
                    continue
        if len(stack) != 0:
            while stack:
                top = stack.pop()
                autocomplete.append(pairs[top])
            
        for char in autocomplete:
            points = 5*points + p2_score[char]

        all_points.append(points)

    all_points.sort()

    print(f'Part 2: {all_points[len(all_points)//2]}')
    
part1()
part2()