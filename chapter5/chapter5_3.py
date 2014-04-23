__author__ = 'koo'

from copy import deepcopy

input_text = '''0
4
0->1:7
0->2:4
2->3:2
1->4:1
3->4:3'''

input_line = input_text.split('\n')
source_node = input_line[0]
sink_node = input_line[1]
s = [[0 for i in range(0, int(sink_node) + 1)] for j in range(0, int(sink_node) + 1)]
for line in input_line[2:]:
    split_line = line.split(':')
    state_change = map(int, split_line[0].split('->'))
    s[state_change[0]][state_change[1]] = int(split_line[1])

state = [0 for i in range(0, len(s))]
step = [[0] for i in range(0, len(s))]
for i in range(0, len(s)):
    for j in range(0, len(s[0])):
        if s[i][j] != 0 and state[j] < state[i] + s[i][j]:
            state[j] = state[i] + s[i][j];
            step[j] = deepcopy(step[i]);
            step[j].append(j);

print state[int(sink_node)]
result = str(step[int(sink_node)][0])
for s in step[int(sink_node)][1:]:
    result += ('->' + str(s))
print result