__author__ = 'koo'

import operator, random

Sample_input = '''ATG
ATG
TGT
TGG
CAT
GGA
GAT
AGA'''

split_input = Sample_input.split('\n')

length = 0


def is_next_overlap_kmer(kmer2, kmer1):
    length = len(kmer1)
    return kmer1[0: length - 2] == kmer2[1: length - 1]


def sort_lexicographic_order(overlap_kmers):
    Order_Number = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    kmers_size = []
    for kmer in overlap_kmers:
        size_str = ''
        for c in kmer:
            size_str += str(Order_Number[c])

        kmers_size.append([{kmer: overlap_kmers[kmer]}, int(size_str)])

    sorted_kmers_size = sorted(kmers_size, key=operator.itemgetter(1))

    result = []
    for kmer_size in sorted_kmers_size:
        result.append(kmer_size[0])

    return result


def possible_count(kmer, overlap_kmers):
    for overlap_kmer in overlap_kmers:
        if (overlap_kmers.has_key(kmer)):
            return len(overlap_kmers[kmer])
        else:
            return 0


overlap_kmers = {}
adjacency_list = []
temp_count = 0
result = []


def generate_kmer(kmer, overlap_kmers):
    if len(result) is 0:
        result.append(kmer)
    target_kmers = overlap_kmers[kmer]
    for target_kmer in target_kmers:
        result.append(kmer + target_kmer[length - 2])
    for idx in range(0, (len(target_kmers) + 1) / 2):
        result.remove(result[0])

    generate_sub_kmers(target_kmers, overlap_kmers)


def generate_sub_kmers(kmers, overlap_kmers):
    for idx in range(0, len(kmers)):
        if overlap_kmers.has_key(kmers[idx]):
            target_kmers = overlap_kmers[kmers[idx]]
            if len(target_kmers) > 1:
                continue
            elif len(target_kmers) is 1:
                for target_kmer in target_kmers:
                    result.append(result[idx] + target_kmer[length - 2])
                for idx in range(0, (len(target_kmers) + 1) / 2):
                    result.remove(result[0])
                generate_sub_kmers(target_kmers, overlap_kmers)


for kmer in split_input:
    length = len(kmer)
    kmer1 = kmer[0:length - 1]
    kmer2 = kmer[1:length]
    if is_next_overlap_kmer(kmer1, kmer2):
        if overlap_kmers.has_key(kmer1):
            overlap_kmers[kmer1].insert(0, kmer2)
        else:
            overlap_kmers[kmer1] = [kmer2]

        adjacency_list.append([kmer1, kmer2, False])

total_count = len(adjacency_list)
eulerian_cycle = list()


def addLast(adjacency_list, eulerian_cycle):
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


def addFirst(adjacency_list, eulerian_cycle):
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


while len(adjacency_list) > 1:
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
        # print eulerian_cycle
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
    # print str(total_count - len(adjacency_list)) + '/' + str(total_count) + '(' + complete_rate + ')'

# print adjacency_list
# print eulerian_cycle
# print overlap_kmers

result_str = ''
for kmer in overlap_kmers:
    result = []
    generate_kmer(kmer, overlap_kmers)
    for r in result:
        result_str += r + ' '

print result_str