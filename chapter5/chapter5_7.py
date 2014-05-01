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


sample_input = '''PLEASANTLY
MEASNLY'''

inputs = sample_input.split('\n')
v = inputs[0]
w = inputs[1]

penalty = -5

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


def middle_scores(v, w):
    s = [[i * j * penalty for j in range(-1, 1)] for i in range(len(v) + 1)]
    s[0][1] = penalty
    backtrack = [0] * (len(v) + 1)
    for j in range(1, len(w) / 2 + 1):
        for i in range(0, len(v) + 1):
            if i is 0:
                s[i][1] = j * penalty
            else:
                scores = [s[i - 1][0] + BLOSUM62[keymap[v[i - 1]]][keymap[w[j - 1]]], s[i][0] + penalty,
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


print middle_edge(v, w)