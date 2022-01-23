import sys
from collections import defaultdict

input = [x.split('-') for x in open(sys.argv[1], 'r').read().strip().split('\n')]

def is_small_cave(cave):
    return cave.islower()

graph = defaultdict(list)

for p1, p2 in input:
    graph[p1].append(p2)
    graph[p2].append(p1)

visited_1 = set()
paths_1 = 0

def part1(node):
    global paths_1
    if node == 'end':
        paths_1 += 1
        return
    if is_small_cave(node) and node in visited_1:
        return
    if is_small_cave(node):
        visited_1.add(node)
    for path in graph[node]:
        if path == 'start':
            continue
        part1(path)
    
    if is_small_cave(node):
        visited_1.remove(node)

visited_2 = defaultdict(int)
paths_2 = 0

def part2(node):
    global paths_2
    if node == 'end':
        paths_2 += 1
        return
    if is_small_cave(node):
        visited_2[node] += 1
        times_visited = 0
        for small_cave in visited_2:
            times_visited += visited_2[small_cave] > 1
            if visited_2[small_cave] > 2:
                visited_2[node] -= 1
                return
        if times_visited > 1:
            visited_2[node] -= 1
            return
    for path in graph[node]:
        if path == "start":
            continue
        part2(path)

    if is_small_cave(node):
        visited_2[node] -= 1

part1('start')
print(f'Part 1: {paths_1}')

part2('start')
print(f'Part 2: {paths_2}')