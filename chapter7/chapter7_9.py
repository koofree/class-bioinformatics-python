__author__ = 'koo'

from chapter7_BWT import generate_matrix, sort_matrix, SUFFIX_ARRAY


def SuffixArray(text, k):
    bwt_genome = sort_matrix(generate_matrix(text))
    suffix_array = bwt_genome[SUFFIX_ARRAY]
    partial_suffix_array = list()
    for i in xrange(0, len(suffix_array)):
        if suffix_array[i] % k == 0:
            partial_suffix_array.append([i, suffix_array[i]])
    return partial_suffix_array


input = '''PANAMABANANAS$
5'''

correct_answer = '''1,5
11,10
12,0
'''

split_input = input.split('\n')

text = split_input[0]
k = int(split_input[1])

partial_suffix_array = SuffixArray(text, k)

result = ''
for value in partial_suffix_array:
    result += str(value[0]) + ',' + str(value[1]) + '\n'

assert result == correct_answer