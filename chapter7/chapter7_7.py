__author__ = 'koo'

from chapter7_6 import generate_first_column, FIRST_COLUMN, LAST_TO_FIRST

# find count of matching pattern on last column
def BWMatching(first_column, last_column, pattern, last_to_first):
    top = 0
    bottom = len(last_column) - 1
    _pattern = pattern
    while top <= bottom:
        if len(_pattern) is not 0:
            symbol = _pattern[len(_pattern) - 1]
            _pattern = _pattern[:-1]

            # find top and bottom index
            # if it has not find same symbol at string between top to bottom
            # than it will be return zero
            is_first = True
            is_changed = False
            for i in xrange(top, bottom + 1):
                if last_column[i] == symbol:
                    if is_first:
                        top_index = i
                        is_first = False
                    bottom_index = i
                    is_changed = True

            if not is_changed:
                return 0

            # set value top and bottom
            top = last_to_first[top_index]
            bottom = last_to_first[bottom_index]

        else:
            # all of pattern character removed than return
            # distance of top and bottom
            return bottom - top + 1

    raise Exception('wrong top bottom values. top[' + str(top) + '] bottom[' + str(bottom) + ']')


input = '''TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC
CCT CAC GAG CAG ATC'''

correct_answer = '2 1 1 0 1'
split_input = input.split('\n')

bwt_string = split_input[0]
patterns = split_input[1].split(' ')

result = str()
# use all pattern using iterate function
for pattern in patterns:
    first_column = generate_first_column(bwt_string)
    result += str(BWMatching(first_column[FIRST_COLUMN], bwt_string, pattern, first_column[LAST_TO_FIRST])) + ' '

assert result.strip(' ') == correct_answer