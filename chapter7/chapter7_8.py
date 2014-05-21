__author__ = 'koo'

from chapter7_6 import generate_first_column, FIRST_COLUMN, COLUMN_TYPE

# end character
END_CH = '$'

# ($) character's ordinary.
END_CH_NUM = ord('A') - 1

FIRST_OCCURRENCE = 'first_occurrence'
CHA_COUNT = 'cha_count'
COUNT = 'count'

# get character's ordinary include end character.
def custom_ord(cha):
    if cha is END_CH:
        return END_CH_NUM
    else:
        return ord(cha)


def generate_first_occurrence(first_column):
    symbol = first_column[0]

    _first_column = first_column[1:]
    occurrence = 0
    count = 1

    result = {FIRST_OCCURRENCE: [occurrence], CHA_COUNT: []}
    while len(_first_column) is not 0:
        occurrence += 1

        if symbol != _first_column[0]:
            symbol = _first_column[0]
            result[FIRST_OCCURRENCE].append(occurrence)

            result[CHA_COUNT].append(count)
            count = 0

        count += 1
        _first_column = _first_column[1:]

    result[CHA_COUNT].append(count)

    return result


def generate_count(last_column, cha_type):
    index_counts = [0 for i in xrange(0, len(cha_type))]
    result = [list(index_counts)]
    for cha in last_column:
        index_counts[cha_type.index(cha)] += 1
        result.append(list(index_counts))

    return result


def BetterBWMatching(first_occurrence, last_column, pattern, count, column_type):
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
            return bottom - top + 1


input = '''GGCGCCGC$TAGTCACACACGCCGTA
ACC CCG CAG'''

correct_answer = '1 2 1'

split_input = input.split('\n')

bwt_string = split_input[0]
patterns = split_input[1].split(' ')

first_column = generate_first_column(bwt_string)

first_occurrence = generate_first_occurrence(first_column[FIRST_COLUMN])

count = generate_count(bwt_string, first_column[COLUMN_TYPE])

result = str()
for pattern in patterns:
    result += str(
        BetterBWMatching(first_occurrence[FIRST_OCCURRENCE], bwt_string, pattern, count,
                         first_column[COLUMN_TYPE])) + ' '

assert result.strip(' ') == correct_answer