import sys

input_str = open(sys.argv[1], 'r').read().strip().split('\n')

input = []
for entry in input_str:
    key_value = entry.split('|')
    key, value = [tuple(sorted(digit)) for digit in key_value[0].strip().split(' ')], [tuple(sorted(digit)) for digit in key_value[1].strip().split(' ')]
    input.append((key,value))

unique_len = [2,3,4,7]

def part1():
    counter = 0
    for _, output in input:
        for digit in output:
            if len(digit) in unique_len:
                counter += 1
    print(f'Part 1: {counter}')

def filter_digits(digits, length):
    return list(filter(lambda x: len(x) == length, digits))

def digit_has_segment(digit, segment):
    return all(item in digit for item in segment)

def find_one(digits):
    return filter_digits(digits, 2)

def find_four(digits):
    return filter_digits(digits, 4)

def find_seven(digits):
    return filter_digits(digits, 3)

def find_eight(digits):
    return filter_digits(digits, 7)

def find_three(digits, one):
    for digit in filter_digits(digits, 5):
        if digit_has_segment(digit, one):
            return digit

def find_nine(digits, four):
    for digit in filter_digits(digits, 6):
        if digit_has_segment(digit, four):
            return digit

def find_zero_and_six(digits, one, nine):
    for digit in filter_digits(digits, 6):
        if digit == nine:
            continue
        if digit_has_segment(digit, one):
            zero = digit
        else:
            six = digit

    return zero, six

def find_two_and_five(digits, three, six):
    for digit in filter_digits(digits, 5):
        if digit == three:
            continue
        if digit_has_segment(six, digit):
            five = digit
        else:
            two = digit

    return two, five

def part2():
    sum = 0
    for ref, output in input:
        one = find_one(ref)[0]
        four = find_four(ref)[0]
        seven = find_seven(ref)[0]
        eight = find_eight(ref)[0]

        three = find_three(ref, one)
        nine = find_nine(ref, four)
        zero, six = find_zero_and_six(ref, one, nine)
        two, five = find_two_and_five(ref, three, six)

        nums = {
            zero:'0',
            one:'1',
            two:'2',
            three:'3',
            four:'4',
            five:'5',
            six:'6',
            seven:'7',
            eight:'8',
            nine:'9'
        }
        digit = []
        for out_str in output:
            digit.append(nums[out_str])
        sum += int(''.join(digit))
    print(f'Part 2: {sum}')

part1()
part2()