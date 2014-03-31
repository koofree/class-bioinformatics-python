__author__ = 'koo'

import operator

Sample_input = '''ATGCG
GCATG
CATGC
AGGCA
GGCAT'''

Sample_output = '''AGGCA -> GGCAT
CATGC -> ATGCG
GCATG -> CATGC
GGCAT -> GCATG'''

split_input = Sample_input.split('\n')


def is_next_overlap_kmer(kmer2, kmer1):
    length = len(kmer1)
    return kmer1[0: length - 2] == kmer2[1: length - 1]


def sort_lexicographic_order(overlap_kmers):
    Order_Number = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    kmers_size = []
    for kmer in overlap_kmers:
        size_str = ''
        for c in kmer[0]:
            size_str += str(Order_Number[c])

        kmers_size.append([kmer, int(size_str)])

    sorted_kmers_size = sorted(kmers_size, key=operator.itemgetter(1))

    result = []
    for kmer_size in sorted_kmers_size:
        result.append(kmer_size[0])

    return result


overlap_kmers = []

for kmer1 in split_input:
    for kmer2 in split_input:
        if is_next_overlap_kmer(kmer1, kmer2):
            overlap_kmers.append([kmer1, kmer2])

for overlap_kmer in sort_lexicographic_order(overlap_kmers):
    print overlap_kmer[0] + '->' + overlap_kmer[1]