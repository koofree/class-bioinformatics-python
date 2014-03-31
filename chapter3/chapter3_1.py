__author__ = 'koo'

import itertools

dna_chars = ['A', 'T', 'G', 'C']


def all_pattern_of_dna(length):
    result = []
    for s in itertools.product(dna_chars, repeat=length):
        str = ''
        for c in s:
            str += c
        result.append(str)
    return result


def mismatch(str1, str2):
    count = 0
    for num in range(0, len(str1)):
        if str1[num] is not str2[num]:
            count += 1

    return count


sample_input = '''3 1
ATTTGGC
TGCCTTA
CGGTATC
GAAAATT'''

sample_data = sample_input.split('\n')

initial_numbers = sample_data[0].split(' ')

k = int(initial_numbers[0])
d = int(initial_numbers[1])

result = []
for pattern in all_pattern_of_dna(k):
    match1 = True
    for line in sample_data[1:]:
        match2 = False
        for _pattern_num in range(0, len(line) - k + 1):
            if mismatch(line[_pattern_num:_pattern_num + k], pattern) == d:
                match2 = True
                break

        if not match2:
            match1 = False
            break
    if match1:
        result.append(pattern)

print result