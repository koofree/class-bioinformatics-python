__author__ = 'koo'

sample_input = '''3
AAACTCATC
TTTCAAATC
'''

split_input = sample_input.split('\n')
k = int(split_input[0])
v = split_input[1]
w = split_input[2]

# DNA Transport Map
# ###############################################
DNA_opp_dic = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


def DNA_opp(DNA_str):
    result = ""
    for char in DNA_str:
        result += DNA_opp_dic[char]
    return result


# ###############################################

def _kmer_range_(v, k):
    return range(0, len(v) - k + 1)


def _print(p):
    for _p in p:
        print '(' + str(_p).strip('[]') + ')'


def find_shared_kmers(v, w, k):
    result = list()
    for i in _kmer_range_(v, k):
        v_kmer = v[i: i + k]
        for j in _kmer_range_(w, k):
            w_kmer = w[j: j + k]
            if v_kmer == w_kmer:
                result.append([i, j])
        for j in _kmer_range_(w, k):
            w_kmer = w[j: j + k]
            if DNA_opp(v_kmer) == w_kmer:
                result.append([i, j])

    return result


_print(find_shared_kmers(v, w, k))