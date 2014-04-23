__author__ = 'koo'

input_text = '''4 4
1 0 2 4 3
4 6 5 2 1
4 4 5 2 1
5 6 8 5 3
-
3 2 4 0
3 2 4 2
0 7 3 3
3 3 0 2
1 3 2 2
'''

# input_text = file('dataset_261_9.txt', 'r').read()


def ManhattanTourist(n, m, down, right):
    s = [[0 for i in range(0, m + 1)] for j in range(0, n + 1)]
    for i in range(1, n + 1):
        s[i][0] = s[i - 1][0] + down[i - 1][0]

    for j in range(1, m + 1):
        s[0][j] = s[0][j - 1] + right[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1])

    return s[n][m]


input_line = input_text.split('\n')
sizeOfMatrix = input_line[0].split(' ')

x_size = int(sizeOfMatrix[0])
y_size = int(sizeOfMatrix[1])

down_weight = []
right_weight = []

for line in input_line[1:1 + int(x_size)]:
    down_weight.append(map(int, line.split(' ')))

for line in input_line[2 + int(x_size):3 + 2 * int(x_size)]:
    right_weight.append(map(int, line.split(' ')))

print down_weight
print right_weight

print ManhattanTourist(x_size, y_size, down_weight, right_weight)

