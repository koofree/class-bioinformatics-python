__author__ = 'koo'

# end character
END_CH = '$'

# ($) character's ordinary.
END_CH_NUM = ord('A') - 1

LAST_TO_FIRST = 'last_to_first'
FIRST_TO_LAST = 'first_to_last'
FIRST_COLUMN = 'first_column'
COLUMN_TYPE = 'column_type'

# get character's ordinary include end character.
def custom_ord(cha):
    if cha is END_CH:
        return END_CH_NUM
    else:
        return ord(cha)


# generate first column using insert sort
def generate_first_column(bwt):
    length = len(bwt)
    result = {FIRST_TO_LAST: list(),
              LAST_TO_FIRST: [None for i in range(0, length)],
              FIRST_COLUMN: '', COLUMN_TYPE: list()}
    for i in xrange(0, len(bwt)):
        bwt_cha = bwt[i]
        result_length = len(result[FIRST_COLUMN])

        inserting_index = result_length
        for _index in xrange(result_length - 1, -1, -1):
            c1 = custom_ord(bwt_cha)
            c2 = custom_ord(bwt[result[FIRST_TO_LAST][_index]])
            if c1 >= c2:
                break
            else:
                inserting_index = _index
                continue

        result[FIRST_COLUMN] = result[FIRST_COLUMN][:inserting_index] + bwt_cha + result[FIRST_COLUMN][inserting_index:]
        result[FIRST_TO_LAST].insert(inserting_index, i)

    for i in xrange(0, length):
        result[LAST_TO_FIRST][result[FIRST_TO_LAST][i]] = i
        if not result[FIRST_COLUMN][i] in result[COLUMN_TYPE]:
            result[COLUMN_TYPE].append(result[FIRST_COLUMN][i])

    return result


# generate original genome
def generate_genome(first_to_last, last_column):
    length = len(first_to_last)

    index = last_column.index(END_CH)
    result = str()
    while True:
        index = first_to_last[index]
        result += last_column[index]

        if len(result) == length:
            break

    return result


def IN_BWT(genome):
    first_to_last = generate_first_column(genome)[FIRST_TO_LAST]
    return generate_genome(first_to_last, genome)


input = 'TTCCTAACG$A'
correct_answer = 'TACATCACGT$'

assert correct_answer == IN_BWT(input)