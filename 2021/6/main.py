from collections import defaultdict
import sys

input = [int(x) for x in open(sys.argv[1],'r').read().strip().split(',')]

def run(days, message):
    all_fish = input.copy()
    fish_map = {}
    for fish in all_fish:
        if fish not in fish_map:
            fish_map[fish] = 0
        fish_map[fish] += 1

    while days > 0:
        updated_map = defaultdict(int)
        for fish, count in fish_map.items():
            if fish == 0:
                updated_map[6] += count
                updated_map[8] += count
            else:
                updated_map[fish-1] += count
            fish_map = updated_map

        days -= 1

    print(f'{message}: {sum(fish_map.values())}')

run(80, 'Part 1')
run(256, 'Part 2')