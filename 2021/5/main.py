import sys
import numpy as np

input = open(sys.argv[1],'r').readlines()

lines = []
for entry in input:
    p1, p2 = entry.strip().split('->')
    xy_1 = (int(p1.split(',')[0]),int(p1.split(',')[1]))
    xy_2 = (int(p2.split(',')[0]),int(p2.split(',')[1]))
    lines.append((xy_1,xy_2))

dim = 0

for line in lines:
    p1 = line[0]
    p2 = line[1]
    dim = max(dim, p1[0], p1[1], p2[0], p2[1])
    
dim += 1
plane = np.zeros((dim,dim))

def part1():
    for line in lines:
        p1 = line[0]
        p2 = line[1]
        if p1[0] == p2[0]:
            # x1 == x2
            y_min = min(p1[1],p2[1])
            y_max = max(p1[1],p2[1]) + 1
            plane[p1[0],y_min:y_max] += 1
        elif p1[1] == p2[1]:
            # y1 == y2
            x_min = min(p1[0],p2[0])
            x_max = max(p1[0],p2[0]) + 1
            plane[x_min:x_max,p1[1]] += 1

    print(f'Part 1: {(plane > 1).sum()}')

def part2():
    for line in lines:
        p1 = line[0]
        p2 = line[1]
        if p1[0] == p2[0]:
            # x1 == x2
            y_min = min(p1[1],p2[1])
            y_max = max(p1[1],p2[1]) + 1
            plane[p1[0],y_min:y_max] += 1
        elif p1[1] == p2[1]:
            # y1 == y2
            x_min = min(p1[0],p2[0])
            x_max = max(p1[0],p2[0]) + 1
            plane[x_min:x_max,p1[1]] += 1
        else:
            # diagonal
            slope = (p2[1] - p1[1])/(p2[0]-p1[0])
            start, end = (p1, p2) if p1[0] < p2[0] else (p2, p1)
            if slope == 1:
                # dx = +change, dy = +change
                change = 0
                while start[0] + change <= end[0]:
                    plane[start[0] + change, start[1] + change] += 1
                    change += 1 
            else:
                # dx = +change, dy = -change
                change = 0
                while start[0] + change <= end[0]:
                    plane[start[0] + change, start[1] - change] += 1
                    change += 1

    print(f'Part 2: {(plane > 1).sum()}')


part2()