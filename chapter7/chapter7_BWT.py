__author__ = 'koo'

MATRIX = 'matrix'
SUFFIX_ARRAY = 'suffix_array'

# ($) character's ordinary.
END_CH_NUM = ord('A') - 1

# get character's ordinary include end character.
def custom_ord(cha):
    if cha is '$':
        return END_CH_NUM
    else:
        return ord(cha)


# if str1 is smaller than str2
def compare(str1, str2):
    for i in range(0, len(str1)):
        c1 = custom_ord(str1[i])
        c2 = custom_ord(str2[i])
        if c1 < c2:
            return True
        elif c1 == c2:
            continue
        else:
            return False

    # if string is exactly same than raising exception
    raise Exception('same string was compared.')


# get rotated genome string
# last character into first position
def rotated_genome(original):
    length_original = len(original)

    # result = last character + string without last character
    result = original[length_original - 1] + original[:length_original - 1]
    return result


# generate rotated genome matrix
def generate_matrix(original):
    matrix = [original]
    for i in range(1, len(original)):
        matrix.append(rotated_genome(matrix[i - 1]))
    return matrix


# sort matrix in order by lexically
def sort_matrix(original_matrix):
    suffix_array = [0]
    sorted_matrix = [original_matrix[0]]
    for i in range(1, len(original_matrix)):
        inserted = False  # status of inserting
        original_string = original_matrix[i]
        for j in range(0, len(sorted_matrix)):
            if compare(original_string, sorted_matrix[j]):
                sorted_matrix.insert(j, original_string)
                suffix_array.insert(j, len(original_matrix) - i)
                inserted = True
                break

        if not inserted:
            sorted_matrix.append(original_string)
            suffix_array.append(len(original_matrix) - i)

    return {MATRIX: sorted_matrix, SUFFIX_ARRAY: suffix_array}


# extract string consist of last column characters of matrix
def extract_last_column(matrix):
    result = str()
    index_of_last_character = len(matrix[0]) - 1
    for genome in matrix:
        result += genome[index_of_last_character]

    return result


def BWT(genome):
    matrix = sort_matrix(generate_matrix(genome))
    return extract_last_column(matrix[MATRIX])


input = 'GCGTGCCTGGTCA$'
correct_answer = 'ACTGGCT$TGCGGC'

assert BWT(input) == correct_answer