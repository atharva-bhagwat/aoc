import sys

input = [int(x) for x in open(sys.argv[1],'r').read().strip().split(',')]

high = max(input)

def part1():
    prev_cost = float('inf')
    for ind in range(high+1):
        cost = 0
        for val in input:
            cost += abs(ind-val)
        if prev_cost > cost:
            prev_cost = cost
        else:
            print(f'Part 1: {prev_cost}')
            return

def calc_sum(n):
    return n*(n+1)/2

def part2():
    prev_cost = float('inf')
    for ind in range(high+1):
        cost = 0
        for val in input:
            cost += calc_sum(abs(ind-val))
        if prev_cost > cost:
            prev_cost = cost
        else:
            print(f'Part 2: {prev_cost}')
            return

part1()
part2()