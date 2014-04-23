__author__ = 'koo'

input_text = '''AACCTTGG
ACACTGTGA
'''
import sys


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


DIRECTION = enum('DOWN', 'RIGHT', 'DOWNRIGHT')


def output(v):
    sys.stdout.write(v)
    sys.stdout.flush()


def OutputLCS(backtrack, v, i, j):
    if i is -1 or j is -1:
        return
    if backtrack[i][j] is DIRECTION.DOWN:
        OutputLCS(backtrack, v, i - 1, j)
    elif backtrack[i][j] is DIRECTION.RIGHT:
        OutputLCS(backtrack, v, i, j - 1)
    else:
        OutputLCS(backtrack, v, i - 1, j - 1)
        output(v[i])


def LCS(v, w):
    s = [[0 for i in range(0, len(w))] for j in range(0, len(v))]
    backtrack = [[None for i in range(0, len(w))] for j in range(0, len(v))]
    for i in range(0, len(v)):
        for j in range(0, len(w)):
            temp = 0
            if v[i] is w[j]:
                temp = s[i - 1][j - 1] + 1
            s[i][j] = max(s[i - 1][j], s[i][j - 1], temp)

            if s[i][j] is s[i - 1][j]:
                backtrack[i][j] = DIRECTION.DOWN
            elif s[i][j] is s[i][j - 1]:
                backtrack[i][j] = DIRECTION.RIGHT
            elif s[i][j] is (s[i - 1][j - 1] + 1):
                backtrack[i][j] = DIRECTION.DOWNRIGHT
    print s
    print backtrack
    return backtrack


input_line = input_text.split('\n')
s = input_line[0]
t = input_line[1]

backtrack = LCS(s, t)
OutputLCS(backtrack, t, len(s) - 1, len(t) - 1)
