__author__ = 'koo'


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


DIRECTION = enum('DOWN', 'DOWNRIGHT', 'RIGHT')


def DIRECTION_OF(num):
    if num is 0:
        return DIRECTION.DOWN
    if num is 1:
        return DIRECTION.DOWNRIGHT
    if num is 2:
        return DIRECTION.RIGHT


sample_input = '''ATATCCG
TCCGA
ATGTACTG'''

input_line = sample_input.split('\n')
v = input_line[0]
w = input_line[1]
u = input_line[2]

BLOSUM62_text = file("../BLOSUM62.txt", "r").read()
BLOSUM62 = []
keymap = {}

value = 0
for ch in BLOSUM62_text.split('\n')[0].split():
    keymap[ch] = value
    value += 1

for line in BLOSUM62_text.split('\n')[1:]:
    BLOSUM62_line = []
    for num in line.split()[1:]:
        BLOSUM62_line.append(int(num))
    BLOSUM62.append(BLOSUM62_line)


def SCORE_OF(c1, c2):
    return BLOSUM62[keymap[c1]][keymap[c2]]


s = [[[0 for k in range(len(u) + 1)] for j in range(len(w) + 1)] for i in range(len(v) + 1)]
backtrack = [[[0 for k in range(len(u) + 1)] for j in range(len(w) + 1)] for i in range(len(v) + 1)]

for i in range(1, len(v) + 1):
    for j in range(1, len(w) + 1):
        for k in range(1, len(u) + 1):
            scores = [s[i - 1][j - 1][k - 1] + int(v[i - 1] is w[j - 1] is u[k - 1]), s[i - 1][j][k], s[i][j - 1][k],
                      s[i][j][k - 1], s[i - 1][j][k - 1], s[i][j - 1][k - 1]]
            backtrack[i][j][k], s[i][j][k] = max(enumerate(scores), key=lambda p: p[1])

print scores
print backtrack

insert_indel = lambda word, i: word[:i] + '-' + word[i:]

v_aligned, w_aligned, u_aligned = v, w, u

i, j, k = len(v), len(w), len(u)
max_score = s[i][j][k]

while i * j * k is not 0:
    if backtrack[i][j][k] is 1:
        i -= 1
        w_aligned = insert_indel(w_aligned, j)
        u_aligned = insert_indel(u_aligned, k)
    elif backtrack[i][j][k] is 2:
        j -= 1
        v_aligned = insert_indel(v_aligned, i)
        u_aligned = insert_indel(u_aligned, k)
    elif backtrack[i][j][k] is 3:
        k -= 1
        v_aligned = insert_indel(v_aligned, i)
        w_aligned = insert_indel(w_aligned, j)
    elif backtrack[i][j][k] is 4:
        i -= 1
        j -= 1
        u_aligned = insert_indel(u_aligned, k)
    elif backtrack[i][j][k] is 5:
        i -= 1
        k -= 1
        w_aligned = insert_indel(w_aligned, j)
    elif backtrack[i][j][k] is 6:
        j -= 1
        k -= 1
        v_aligned = insert_indel(v_aligned, i)
    else:
        i -= 1
        j -= 1
        k -= 1

while len(v_aligned) is not max(len(v_aligned), len(w_aligned), len(u_aligned)):
    v_aligned = insert_indel(v_aligned, 0)
while len(w_aligned) is not max(len(v_aligned), len(w_aligned), len(u_aligned)):
    w_aligned = insert_indel(w_aligned, 0)
while len(u_aligned) is not max(len(v_aligned), len(w_aligned), len(u_aligned)):
    u_aligned = insert_indel(u_aligned, 0)

print str(max_score)
print v_aligned
print w_aligned
print u_aligned