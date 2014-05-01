__author__ = 'koo'


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


DIRECTION = enum('DOWN', 'DOWNRIGHT', 'RIGHT')


def DIRECTION_OF(num):
    if num is 0:
        return DIRECTION.DOWN
    if num is 1:
        return DIRECTION.RIGHT
    if num is 2:
        return DIRECTION.DOWNRIGHT


sample_input = '''PLEASANTLY
MEANLY'''

input_line = sample_input.split('\n')
v = input_line[0]
w = input_line[1]

BLOSUM62_text = file("../BLOSUM62.txt", "r").read()
BLOSUM62 = []
keymap = {}
penalty = -5

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


def global_alignment(v, w):
    s = [[0 for i in range(0, len(w) + 1)] for j in range(0, len(v) + 1)]
    backtrack = [[0 for i in range(0, len(w) + 1)] for j in range(0, len(v) + 1)]

    for i in range(1, len(v) + 1):
        s[i][0] = i * penalty
    for j in range(1, len(w) + 1):
        s[0][j] = j * penalty

    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            scores = [s[i - 1][j] + penalty, s[i][j - 1] + penalty, s[i - 1][j - 1] + SCORE_OF(v[i - 1], w[j - 1])]
            s[i][j] = max(scores)
            backtrack[i][j] = DIRECTION_OF(scores.index(s[i][j]))

    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    v_aligned, w_aligned = v, w

    i, j = len(v), len(w)
    max_score = str(s[i][j])

    while i * j is not 0:
        if backtrack[i][j] is DIRECTION.DOWN:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] is DIRECTION.RIGHT:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        else:
            i -= 1
            j -= 1

    for _ in range(i):
        w_aligned = insert_indel(w_aligned, 0)
    for _ in range(j):
        v_aligned = insert_indel(v_aligned, 0)

    return max_score, v_aligned, w_aligned


def middle_scores(v, w):
    s = [[i * j * penalty for j in range(-1, 1)] for i in range(len(v) + 1)]
    s[0][1] = penalty
    backtrack = [0] * (len(v) + 1)
    for j in range(1, len(w) / 2 + 1):
        for i in range(0, len(v) + 1):
            if i is 0:
                s[i][1] = j * penalty
            else:
                scores = [s[i - 1][0] + SCORE_OF(v[i - 1], w[j - 1]), s[i][0] + penalty,
                          s[i - 1][1] + penalty]
                s[i][1] = max(scores)
                backtrack[i] = DIRECTION_OF(scores.index(s[i][1]))

            if j is not len(w) / 2:
                s = [[row[1]] * 2 for row in s]
    return [row[1] for row in s], backtrack


def middle_edge(v, w):
    middle_score = middle_scores(v, w)[0]

    fixed_v = v[::-1]
    fixed_w = w[::-1] + ['', '$'][len(w) % 2 == 1 and len(w) > 1]

    middle_sink, sink_backtrack = map(lambda l: l[::-1],
                                      middle_scores(fixed_v, fixed_w))
    scores = map(sum, zip(middle_score, middle_sink))

    max_middle = max(range(len(scores)), key=lambda i: scores[i])

    if max_middle == len(scores) - 1:
        next_node = (max_middle, len(w) / 2 + 1)
    else:
        next_node = [(max_middle + 1, len(w) / 2 + 1), (max_middle, len(w) / 2 + 1), (max_middle + 1, len(w) / 2), ][
            sink_backtrack[max_middle]]

    return (max_middle, len(w) / 2), next_node


def linear_space_alignment(top, bottom, left, right):
    if left is right:
        return [v[top:bottom], '-' * (bottom - top)]
    elif top is bottom:
        return ['-' * (right - left), w[left:right]]
    elif bottom - top is 1 or right - left is 1:
        return global_alignment(v[top:bottom], w[left:right])[1:]
    else:
        mid_node, next_node = middle_edge(v[top:bottom], w[left:right])
        mid_node = tuple(map(sum, zip(mid_node, [top, left])))
        next_node = tuple(map(sum, zip(next_node, [top, left])))

        current = [['-', v[mid_node[0] % len(v)]][next_node[0] - mid_node[0]],
                   ['-', w[mid_node[1] % len(w)]][next_node[1] - mid_node[1]]]

        A = linear_space_alignment(top, mid_node[0], left, mid_node[1])
        B = linear_space_alignment(next_node[0], bottom, next_node[1], right)
        return [A[i] + current[i] + B[i] for i in range(2)]


v_aligned, w_aligned = linear_space_alignment(0, len(v), 0, len(w))
score = sum([penalty if '-' in pair else SCORE_OF(pair[0], pair[1]) for pair in zip(v_aligned, w_aligned)])

print score
print v_aligned
print w_aligned