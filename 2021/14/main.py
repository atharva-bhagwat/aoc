import sys
from collections import defaultdict

def read():
    template, mapping_block = open(sys.argv[1], 'r').read().strip().split('\n\n')
    polymers = {''.join(pair): 1 for pair in zip(template, template[1:])}

    rules = {}

    for mapping in mapping_block.split('\n'):
        key, value = mapping.split(' -> ')
        rules[key] = value

    rules = {k: [k[0] + v, v + k[1]] for k, v in rules.items()}

    return polymers, rules

def update(polymers, rules):
    updated_polymer = defaultdict(int)
    for polymer, count in polymers.items():
        for rule in rules[polymer]:
            updated_polymer[rule] += count
    return updated_polymer

def run(steps, message):
    polymers, rules = read()
    while steps > 0:
        polymers = update(polymers, rules)
        steps -= 1
    count = defaultdict(int)
    for k, v in polymers.items():
        for ch in k:
            count[ch] += v
    sorted_count = sorted((item+1)//2 for item in count.values())
    print(f'{message} {sorted_count[-1]-sorted_count[0]}')


run(10, 'Part 1:')
run(40, 'Part 2:')
