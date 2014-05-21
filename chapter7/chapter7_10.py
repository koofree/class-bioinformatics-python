__author__ = 'koo'

from chapter7_6 import FIRST_COLUMN, COLUMN_TYPE
from chapter7_8 import generate_first_occurrence, generate_first_column, generate_count, \
    FIRST_OCCURRENCE
from chapter7_BWT import generate_matrix, sort_matrix, SUFFIX_ARRAY, MATRIX, extract_last_column


def MultipleBetterBWMatching(first_occurrence, last_column, pattern, count, column_type, suffix_array):
    top = 0
    bottom = len(last_column) - 1
    _pattern = pattern
    while top <= bottom:
        if len(_pattern) is not 0:
            symbol = _pattern[len(_pattern) - 1]
            _pattern = _pattern[:-1]

            is_first = True
            is_changed = False
            for i in xrange(top, bottom + 1):
                if last_column[i] == symbol:
                    top = first_occurrence[column_type.index(symbol)] + count[top][column_type.index(symbol)]
                    bottom = first_occurrence[column_type.index(symbol)] \
                             + count[bottom + 1][column_type.index(symbol)] - 1

                    is_changed = True
                    break

            if not is_changed:
                return 0
        else:
            results = []
            for i in xrange(top, bottom + 1):
                results.append(suffix_array[i])
            return results


input = '''AATCGGGTTCAATCGGGGT
ATCG
GGGT'''

correct_answer = '1 4 11 15'

split_input = input.split('\n')

string = split_input[0]
patterns = split_input[1:]

bwt_genome = sort_matrix(generate_matrix(string))

suffix_array = bwt_genome[SUFFIX_ARRAY]

last_column = extract_last_column(bwt_genome[MATRIX])

first_column = generate_first_column(last_column)

first_occurrence = generate_first_occurrence(first_column[FIRST_COLUMN])

count = generate_count(last_column, first_column[COLUMN_TYPE])

results = list()
results.extend(MultipleBetterBWMatching(first_occurrence[FIRST_OCCURRENCE], last_column, patterns[0], count,
                                        first_column[COLUMN_TYPE],
                                        suffix_array))
results.extend(MultipleBetterBWMatching(first_occurrence[FIRST_OCCURRENCE], last_column, patterns[1], count,
                                        first_column[COLUMN_TYPE],
                                        suffix_array))

assert correct_answer == str(sorted(results)).strip('[]').replace(',', '')
