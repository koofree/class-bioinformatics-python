__author__ = 'koo'

import operator

Sample_input = '''GAGG
GGGG
GGGA
CAGG
AGGG
GGAG'''

split_input = Sample_input.split('\n')


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


overlap_kmers = {}

for kmer in split_input:
    length = len(kmer)
    kmer1 = kmer[0:length - 1]
    kmer2 = kmer[1:length]
    if is_next_overlap_kmer(kmer1, kmer2):
        if overlap_kmers.has_key(kmer1):
            overlap_kmers[kmer1].insert(0, kmer2)
        else:
            overlap_kmers[kmer1] = [kmer2]

for overlap_kmer in sort_lexicographic_order(overlap_kmers):
    str = ''
    for key in overlap_kmer:
        str += key + ' -> '
        for value in overlap_kmer[key]:
            str += value + ','
    print str[:-1]