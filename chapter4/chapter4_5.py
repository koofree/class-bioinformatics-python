__author__ = 'koo'

sample_input = '''0 -> 3
1 -> 0
2 -> 1,6
3 -> 2
4 -> 2
5 -> 4
6 -> 5,8
7 -> 9
8 -> 7
9 -> 6'''

import random
import pkg_resources

adjacency_list = list()

#sample_input = pkg_resources.resource_string('chapter4', 'data/chapter4_5_input')

for line in sample_input.split('\n'):
    adjacency = dict()
    line_items = line.split(' -> ')
    adjacency['left'] = line_items[0]
    adjacency_item = list()
    for right_item in line_items[1].split(','):
        item = [adjacency['left'], right_item, False]
        adjacency_list.append(item)

total_count = len(adjacency_list)
temp_count = 0
eulerian_cycle = list()


def addLast():
    added = False
    if (len(eulerian_cycle) > 1 and eulerian_cycle[0][2] is True and eulerian_cycle[1][0] == adjacency[1]):
        temp_adjacency = eulerian_cycle[0]
        temp_adjacency[2] = False
        adjacency_list.append(temp_adjacency)
        eulerian_cycle.remove(temp_adjacency)
        eulerian_cycle.insert(0, adjacency)
        adjacency_list.remove(adjacency)
        added = True
    elif (len(eulerian_cycle) > 1 and eulerian_cycle[len(eulerian_cycle) - 2][1] == adjacency[0]):
        adjacency[2] = True
        temp_adjacency = eulerian_cycle[len(eulerian_cycle) - 1]
        temp_adjacency[2] = False
        adjacency_list.append(temp_adjacency)
        eulerian_cycle.remove(temp_adjacency)
        eulerian_cycle.insert(len(eulerian_cycle), adjacency)
        adjacency_list.remove(adjacency)
        added = True
    return added


def addFirst():
    added = False
    if (eulerian_cycle[0][0] == adjacency[1] and eulerian_cycle[0][2] is False):
        eulerian_cycle[0][2] = True
        eulerian_cycle.insert(0, adjacency)
        adjacency_list.remove(adjacency)
        added = True
    elif (eulerian_cycle[len(eulerian_cycle) - 1][1] == adjacency[0]):
        adjacency[2] = True
        eulerian_cycle.insert(len(eulerian_cycle), adjacency)
        adjacency_list.remove(adjacency)
        added = True
    return added


while len(adjacency_list) > 0:
    for num in range(0, len(adjacency_list)):
        adjacency = adjacency_list[random.randint(0, len(adjacency_list)-1)]
        if (len(eulerian_cycle) == 0):
            eulerian_cycle.append(adjacency)
            adjacency_list.remove(adjacency)
            continue

        if random.randint(1, 2) is 1:
            if addFirst() is False:
                addLast()
        else:
            if addLast() is False:
                addFirst()

    if len(eulerian_cycle) is temp_count:
        if random.randint(1, 2) is 1:
            temp_adjacency = eulerian_cycle[len(eulerian_cycle) - 1]
            temp_adjacency[2] = False
            adjacency_list.append(temp_adjacency)
            eulerian_cycle.remove(temp_adjacency)
        else:
            temp_adjacency = eulerian_cycle[0]
            temp_adjacency[2] = False
            adjacency_list.append(temp_adjacency)
            eulerian_cycle.remove(temp_adjacency)

    temp_count = len(eulerian_cycle)

    complete_rate = str(int(float(total_count - len(adjacency_list)) / total_count * 100)) + '%'
    print str(total_count - len(adjacency_list)) + '/' + str(total_count) + '(' + complete_rate + ')'

result = list()
for adjacency in eulerian_cycle:
    if len(result) is 0:
        result.append(adjacency[0])
    result.append(adjacency[1])

result_line = result[0]
for line in result[1:len(result)]:
    result_line += '->' + line

print result_line