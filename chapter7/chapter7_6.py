__author__ = 'koo'

# end character
END_CH = '$'

# ($) character's ordinary.
END_CH_NUM = ord('A') - 1

# four type of result
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
# return : FIRST_TO_LAST, LAST_TO_FIRST, FIRST_COLUMN, COLUMN_TYPE
def generate_first_column(bwt):
    length = len(bwt)

    first_to_last = list()
    last_to_first = [None for i in range(0, length)]
    first_column = ''
    column_type = list()

    for i in xrange(0, length):
        bwt_cha = bwt[i]
        result_length = len(first_column)

        # compare and find index to insert
        inserting_index = result_length
        for _index in xrange(result_length - 1, -1, -1):
            c1 = custom_ord(bwt_cha)
            c2 = custom_ord(bwt[first_to_last[_index]])
            if c1 >= c2:
                break
            else:
                inserting_index = _index
                continue

        first_column = first_column[:inserting_index] + bwt_cha + first_column[inserting_index:]
        first_to_last.insert(inserting_index, i)

    # change first_to_last to last_to_first
    for i in xrange(0, length):
        last_to_first[first_to_last[i]] = i
        if not first_column[i] in column_type:
            column_type.append(first_column[i])

    return {FIRST_TO_LAST: first_to_last, LAST_TO_FIRST: last_to_first, FIRST_COLUMN: first_column,
            COLUMN_TYPE: column_type}


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