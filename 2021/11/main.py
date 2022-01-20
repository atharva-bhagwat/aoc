import sys

nrow, ncol = 0, 0

def read():
    global nrow, ncol
    rows = open(sys.argv[1], 'r').read().strip().split('\n')

    input = []

    for row in rows:
        temp_row = []
        for ele in row:
            temp_row.append(int(ele))
        input.append(temp_row)

    nrow, ncol = len(input), len(input[0])

    return input

neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def neighbor_flash(x, y, arr, flashes, visited = []):
    visited.append((x,y))
    for dx, dy in neighbors:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < nrow and 0 <= ny < ncol and (nx,ny) not in visited:
            arr[nx][ny] += 1
            if arr[nx][ny] == 10:
                arr[nx][ny] = 0
                flashes += 1
                arr, flashes, visited = neighbor_flash(nx, ny, arr, flashes, visited)
    return arr, flashes, visited
            

def step(arr, flashes):
    visited = []
    for i in range(nrow):
        for j in range(ncol):
            if (i,j) not in visited:
                arr[i][j] += 1
                if arr[i][j] == 10:
                    arr[i][j] = 0
                    flashes += 1
                    arr, flashes, visited = neighbor_flash(i, j, arr, flashes, visited)
    return arr, flashes, visited

def part1(steps = 100):
    arr_1 = read()
    flashes = 0
    for _ in range(steps):
        arr_1, flashes, _ = step(arr_1, flashes)

    print(f'Part 1: {flashes}')

def part2():
    arr_2 = read()
    steps = 0
    while True:
        steps += 1
        arr_2, _, visited = step(arr_2, 0)
        if len(visited) == nrow * ncol:
            print(f'Part 2: {steps}')
            break

part1()
part2()