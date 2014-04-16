__author__ = 'koo'

sample_input = '''2
GAGA|TTGA
TCGT|GATG
CGTG|ATGT
TGGT|TGAG
GTGA|TGTT
GTGG|GTGA
TGAG|GTTG
GGTC|GAGA
GTCG|AGAT'''

import random
import pkg_resources

adjacency_list = list()

# sample_input = pkg_resources.resource_string('chapter4', 'data/chapter4_5_input')

item_list = sample_input.split('\n')
d = item_list[0]
length = 0

for line in item_list[1:]:
    adjacency = dict()
    line_items = line.split('|')
    length = len(line_items[0])
    adjacency_item = [[line_items[0][0:length - 1], line_items[1][0:length - 1]],
                      [line_items[0][1:length], line_items[1][1:length]], False]

    adjacency_list.append(adjacency_item)

total_count = len(adjacency_list)

temp_count = 0
eulerian_cycle = list()


def equals(a, b):
    if (a[0] == b[0] and a[1] == b[1]):
        return True
    else:
        return False


def addLast(adjacency_list, eulerian_cycle):
    added = False
    if (len(eulerian_cycle) > 1 and eulerian_cycle[0][2] is True and equals(eulerian_cycle[1][0], adjacency[1])):
        temp_adjacency = eulerian_cycle[0]
        temp_adjacency[2] = False
        adjacency_list.append(temp_adjacency)
        eulerian_cycle.remove(temp_adjacency)
        eulerian_cycle.insert(0, adjacency)
        adjacency_list.remove(adjacency)
        added = True
    elif (len(eulerian_cycle) > 1 and equals(eulerian_cycle[len(eulerian_cycle) - 2][1], adjacency[0])):
        adjacency[2] = True
        temp_adjacency = eulerian_cycle[len(eulerian_cycle) - 1]
        temp_adjacency[2] = False
        adjacency_list.append(temp_adjacency)
        eulerian_cycle.remove(temp_adjacency)
        eulerian_cycle.insert(len(eulerian_cycle), adjacency)
        adjacency_list.remove(adjacency)
        added = True
    return added


def addFirst(adjacency_list, eulerian_cycle):
    added = False
    if (equals(eulerian_cycle[0][0], adjacency[1]) and eulerian_cycle[0][2] is False):
        eulerian_cycle[0][2] = True
        eulerian_cycle.insert(0, adjacency)
        adjacency_list.remove(adjacency)
        added = True
    elif (equals(eulerian_cycle[len(eulerian_cycle) - 1][1], adjacency[0])):
        adjacency[2] = True
        eulerian_cycle.insert(len(eulerian_cycle), adjacency)
        adjacency_list.remove(adjacency)
        added = True
    return added


while len(adjacency_list) > 0:
    for num in range(0, len(adjacency_list)):
        adjacency = adjacency_list[random.randint(0, len(adjacency_list) - 1)]
        if (len(eulerian_cycle) == 0):
            eulerian_cycle.append(adjacency)
            adjacency_list.remove(adjacency)
            continue

        if random.randint(1, 2) is 1:
            if addFirst(adjacency_list, eulerian_cycle) is False:
                addLast(adjacency_list, eulerian_cycle)
        else:
            if addLast(adjacency_list, eulerian_cycle) is False:
                addFirst(adjacency_list, eulerian_cycle)

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

front_str = ''
front_str = eulerian_cycle[0][0][0] + eulerian_cycle[0][1][0][2]
rear_str = eulerian_cycle[0][0][1] + eulerian_cycle[0][1][1][2]

for adjacency in eulerian_cycle[1:]:
    front_str += adjacency[1][0][2]
    rear_str += adjacency[1][1][2]

result_str = front_str + rear_str[len(rear_str) - (length + int(d)):]

print result_str