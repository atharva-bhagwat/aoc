import sys
import pandas as pd

input = pd.DataFrame([list(row) for row in open(sys.argv[1],'r').read().strip().split('\n')])

# part 1
gamma_rate = []
epsilon_rate = []
for col in input.columns:
    gamma_rate.append(input[col].value_counts().index[0])
    epsilon_rate.append(input[col].value_counts().index[1])

gamma_rate = int(''.join(gamma_rate),2)
epsilon_rate = int(''.join(epsilon_rate),2)
print(f'Part 1: {gamma_rate*epsilon_rate}')

# part 2
oxygen_rate = input.copy()
co2_rate = input.copy()
while len(oxygen_rate) != 1:
    for col in oxygen_rate.columns:
        if len(oxygen_rate) == 1:
            break
        occur = dict(oxygen_rate[col].value_counts())
        if occur['0'] != occur['1']:
            max_occur = oxygen_rate[col].value_counts().index[0]
        else:
            max_occur = '1'
        oxygen_rate.drop(oxygen_rate[oxygen_rate[col]!=max_occur].index, inplace=True)

while len(co2_rate) != 1:
    for col in co2_rate.columns:
        if len(co2_rate) == 1:
            break
        occur = dict(co2_rate[col].value_counts())
        if occur['0'] != occur['1']:
            least_occur = co2_rate[col].value_counts().index[1]
        else:
            least_occur = '0'
        co2_rate.drop(co2_rate[co2_rate[col]!=least_occur].index, inplace=True)

oxygen_rate = int(''.join(oxygen_rate.values.tolist()[0]),2)
co2_rate = int(''.join(co2_rate.values.tolist()[0]),2)
print(f'Part 2: {oxygen_rate*co2_rate}')