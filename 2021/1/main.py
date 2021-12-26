input = [int(x) for x in open('input.txt','r').readlines()]

pairs = zip(input, input[1:])
increases = [b - a for a,b in pairs if b - a > 0]
print(len(increases))