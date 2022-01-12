from functools import reduce
import sys
from typing import Deque

input = open(sys.argv[1], 'r').read().strip().split('\n')

heatmap = []
for entry in input:
    row = []
    for val in entry:
        row.append(int(val))

    heatmap.append(row)

nrow, ncol = len(heatmap), len(heatmap[0])
neighbors = [(1,0),(-1,0),(0,1),(0,-1)]

def low_point(i,j):
    for di, dj in neighbors:
        ni = i + di
        nj = j + dj
        if 0 <= ni < nrow and 0 <= nj < ncol:
            if heatmap[i][j] >= heatmap[ni][nj]:
                return False
    return True

def part1():
    risk_levels = []
    for i in range(nrow):
        for j in range(ncol):
            if low_point(i,j):
                risk_levels.append(heatmap[i][j]+1)

    print(f'Part 1: {sum(risk_levels)}')

def part2():
    visited = []
    def get_basin_size(i,j):
        stack = Deque([(i,j)])
        size = 0
        while stack:
            cur_i, cur_j = stack.popleft()

            if heatmap[cur_i][cur_j] == 9:
                continue
            else:
                size += 1
            for di, dj in neighbors:
                ni = cur_i + di
                nj = cur_j + dj
                if 0 <= ni < nrow and 0 <= nj < ncol and (ni,nj) not in visited and heatmap[ni][nj] > heatmap[cur_i][cur_j]:
                    visited.append((ni,nj))
                    stack.append((ni,nj))

        return size

    basin_size = []
    for i in range(nrow):
        for j in range(ncol):
            if low_point(i,j):
                visited.append((i,j))
                basin_size.append(get_basin_size(i,j))
    
    basin_size.sort(reverse=True)

    print(f'Part 2: {reduce((lambda x,y : x*y), basin_size[:3])}')

part1()
part2()