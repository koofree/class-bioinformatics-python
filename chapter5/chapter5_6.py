__author__ = 'koo'


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


DIRECTION = enum('DOWN', 'RIGHT', 'DOWNRIGHT')


def DIRECTION_OF(num):
    if num is 0:
        return DIRECTION.DOWN
    if num is 1:
        return DIRECTION.DOWNRIGHT
    if num is 2:
        return DIRECTION.RIGHT


input_text = '''YHFDVPDCWAHRYWVENPQAIAQMEQICFNWFPSMMMKQPHVFKVDHHMSCRWLPIRGKKCSSCCTRMRVRTVWE
YHEDVAHEDAIAQMVNTFGFVWQICLNQFPSMMMKIYWIAVLSAHVADRKTWSKHMSCRWLPIISATCARMRVRTVWE'''

input_line = input_text.split('\n')
protein1 = input_line[0]
protein2 = input_line[1]

BLOSUM62_text = file("../BLOSUM62.txt", "r").read()
BLOSUM62 = []
keymap = {}
penalty_op = -11
penalty_ex = -1

value = 0
for ch in BLOSUM62_text.split('\n')[0].split():
    keymap[ch] = value
    value += 1

for line in BLOSUM62_text.split('\n')[1:]:
    BLOSUM62_line = []
    for num in line.split()[1:]:
        BLOSUM62_line.append(int(num))
    BLOSUM62.append(BLOSUM62_line)

s = [[[0 for i in range(0, len(protein2) + 1)] for j in range(0, len(protein1) + 1)] for k in range(3)]
backtrack = [[[0 for i in range(0, len(protein2) + 1)] for j in range(0, len(protein1) + 1)] for k in range(3)]

for i in range(1, len(protein1) + 1):
    s[0][i][0] = penalty_op + (i - 1) * penalty_ex
    s[1][i][0] = penalty_op + (i - 1) * penalty_ex
    s[2][i][0] = 10 * penalty_op

for i in range(1, len(protein2) + 1):
    s[2][0][i] = 10 * penalty_op
    s[1][0][i] = penalty_op + (i - 1) * penalty_ex
    s[0][0][i] = penalty_op + (i - 1) * penalty_ex

for i in range(1, len(protein1) + 1):
    for j in range(1, len(protein2) + 1):
        lower = [s[0][i - 1][j] + penalty_ex, s[1][i - 1][j] + penalty_op]
        s[0][i][j] = max(lower)
        backtrack[0][i][j] = DIRECTION_OF(lower.index(s[0][i][j]))

        upper = [s[2][i][j - 1] + penalty_ex, s[1][i][j - 1] + penalty_op]
        s[2][i][j] = max(upper)
        backtrack[2][i][j] = DIRECTION_OF(upper.index(s[2][i][j]))

        middle = [s[0][i][j], s[1][i - 1][j - 1] + BLOSUM62[keymap[protein1[i - 1]]][keymap[protein2[j - 1]]],
                  s[2][i][j]]
        s[1][i][j] = max(middle)
        backtrack[1][i][j] = DIRECTION_OF(middle.index(s[1][i][j]))

i, j = len(protein1), len(protein2)
protein1_aligned, protein2_aligned = protein1, protein2

matrix_scores = [s[0][i][j], s[1][i][j], s[2][i][j]]
max_score = max(matrix_scores)
backtrack_matrix = matrix_scores.index(max_score)

insert_indel = lambda word, i: word[:i] + '-' + word[i:]

while i * j != 0:
    if backtrack_matrix == DIRECTION.DOWN:
        if backtrack[0][i][j] == DIRECTION.DOWNRIGHT:
            backtrack_matrix = DIRECTION.DOWNRIGHT
        i -= 1
        protein2_aligned = insert_indel(protein2_aligned, j)

    elif backtrack_matrix == DIRECTION.DOWNRIGHT:
        if backtrack[1][i][j] == DIRECTION.DOWN:
            backtrack_matrix = DIRECTION.DOWN
        elif backtrack[1][i][j] == DIRECTION.RIGHT:
            backtrack_matrix = DIRECTION.RIGHT
        else:
            i -= 1
            j -= 1

    else:
        if backtrack[2][i][j] == DIRECTION.DOWNRIGHT:
            backtrack_matrix = DIRECTION.DOWNRIGHT
        j -= 1
        protein1_aligned = insert_indel(protein1_aligned, i)

for _ in xrange(i):
    protein2_aligned = insert_indel(protein2_aligned, 0)
for _ in xrange(j):
    v_aligned = insert_indel(protein1_aligned, 0)

print max(s[0][len(protein1)][len(protein2)], s[1][len(protein1)][len(protein2)], s[2][len(protein1)][len(protein2)])
print protein1_aligned
print protein2_aligned
