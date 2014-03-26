__author__ = 'koo'

'''
CODE CHALLENGE: Implement RANDOMIZEDMOTIFSEARCH.
     Input: Integers k and t, followed by a collection of strings Dna.
     Output: A collection BestMotifs resulting from running RANDOMIZEDMOTIFSEARCH(Dna, k, t) 1000 times.
     Remember to use pseudocounts!
'''

import random


def mismatch(str1, str2):
    count = 0
    for num in range(0, len(str1)):
        if str1[num] is not str2[num]:
            count += 1

    return count


def rand_motif():
    motif = []
    for line in input_text:
        randomInt = random.randint(0, len(line) - k)
        motif.append(line[randomInt: randomInt + k])

    return motif


def score(motif):
    modif_score = [0]
    init_motif = motif[0]
    for num in range(1, len(motif)):
        modif_score.append(mismatch(init_motif, motif[num]))
    return modif_score


def optimize_motif(motifs, k, input_text):
    result_motif = ''
    for num in range(0, k):
        count = {'C': 0, 'G': 0, 'T': 0, 'A': 0}
        for motif in motifs:
            count[motif[num]] += 1

        result_ch = ''
        c = 0
        for ch in count:
            if c < count[ch]:
                result_ch = ch
                c = count[ch]
        result_motif += result_ch

    new_motifs = []
    for line in input_text:
        _motif = line[0:k]
        for _k in range(0, len(line) - k + 1):
            _pattern = line[_k:_k + k]
            new_count = mismatch(result_motif, _pattern)
            old_count = mismatch(result_motif, _motif)
            if new_count < old_count:
                _motif = _pattern
        new_motifs.append(_motif)

    return motifs


sample_input = '''8 5
CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
TAGTACCGAGACCGAAAGAAGTATACAGGCGT
TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
AATCCACCAGCTCCACGTGCAATGTTGGCCTA'''

random_count = 1000

sample_data = sample_input.split('\n')

initial_numbers = sample_data[0].split(' ')
input_text = sample_data[1:]

k = int(initial_numbers[0])
d = int(initial_numbers[1])

best_motifs = rand_motif()
best_motifs_score = score(best_motifs)

for _k in range(0, random_count):
    temp_motif = rand_motif()

    while True:
        op_motif = optimize_motif(temp_motif, k, input_text)
        temp_score = score(temp_motif)
        op_score = score(op_motif)
        if sum(op_score) < sum(temp_score):
            temp_motif = op_motif
        else:
            break

    motif_score = score(temp_motif)

    new_sum = sum(motif_score)
    old_sum = sum(best_motifs_score)
    if new_sum < old_sum:
        best_motifs = temp_motif
        best_motifs_score = motif_score

print best_motifs_score

for line in best_motifs:
    print line

