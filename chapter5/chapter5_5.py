__author__ = 'koo'

import sys


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


DIRECTION = enum('DOWN', 'RIGHT', 'DOWNRIGHT')

input_text = '''MEANLY
PENALTY'''

input_line = input_text.split('\n')
protein1 = input_line[0]
protein2 = input_line[1]

PAM250_text = file("../PAM250.txt", "r").read()
PAM250 = []
keymap = {}
penalty = -5
value = 0
for ch in PAM250_text.split('\n')[0].split():
    keymap[ch] = value
    value += 1

for line in PAM250_text.split('\n')[1:]:
    PAM250_line = []
    for num in line.split()[1:]:
        PAM250_line.append(int(num))
    PAM250.append(PAM250_line)

s = [[0 for i in range(0, len(protein2))] for j in range(0, len(protein1))]
backtrack = [[0 for i in range(0, len(protein2))] for j in range(0, len(protein1))]

for i in range(0, len(protein1)):
    for j in range(0, len(protein2)):
        s[i][j] = max(0, (s[i - 1][j] + penalty), (s[i][j - 1] + penalty),
                      (s[i - 1][j - 1] + PAM250[keymap[protein1[i]]][keymap[protein2[j]]]))

        if s[i][j] is s[i - 1][j] + penalty:
            backtrack[i][j] = DIRECTION.DOWN
        elif s[i][j] is s[i][j - 1] + penalty:
            backtrack[i][j] = DIRECTION.RIGHT
        elif s[i][j] is s[i - 1][j - 1] + PAM250[keymap[protein1[i]]][keymap[protein2[j]]]:
            backtrack[i][j] = DIRECTION.DOWNRIGHT


def output(v):
    sys.stdout.write(v)
    sys.stdout.flush()


def OutputLCS(backtrack, v, i, j):
    if i is -1:
        str = ''
        return str
    if j is -1:
        str = ''
        return str
    if backtrack[i][j] is DIRECTION.DOWN:
        return OutputLCS(backtrack, v, i - 1, j)
    elif backtrack[i][j] is DIRECTION.RIGHT:
        return OutputLCS(backtrack, v, i, j - 1) + '-'
    else:
        return OutputLCS(backtrack, v, i - 1, j - 1) + v[j]


print s
print backtrack
print s[len(protein1) - 1][len(protein2) - 1]
print OutputLCS(backtrack, protein2, len(protein1) - 1, len(protein2) - 1)