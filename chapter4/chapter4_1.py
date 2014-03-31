__author__ = 'koo'
'''
CODE CHALLENGE: Solve the String Composition Problem
    Input: An integer k and a string text
    Output: Composition (Text), where the k-mers are written in lexicographic order.
'''

import operator

Sample_input = '''5
CAATCCAAC'''

Sample_output = '''AATCC
ATCCA
CAATC
CCAAC
TCCAA'''

split_input = Sample_input.split('\n')

K = int(split_input[0])
Text = split_input[1]


def find_all_kmer(text, k):
    kmers = []
    for i in range(0, len(text) - k + 1):
        kmer = text[i:i + k]
        kmers.append(kmer)
    return kmers


def sort_lexicographic_order(kmers):
    Order_Number = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    kmers_size = []
    for kmer in kmers:
        size_str = ''
        for c in kmer:
            size_str += str(Order_Number[c])

        kmers_size.append([kmer, int(size_str)])

    sorted_kmers_size = sorted(kmers_size, key=operator.itemgetter(1))

    result = []
    for kmer_size in sorted_kmers_size:
        result.append(kmer_size[0])

    return result


print str(sort_lexicographic_order(find_all_kmer(Text, K))).strip('[]')
