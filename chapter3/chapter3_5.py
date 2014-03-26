__author__ = 'koo'

import random
import copy

sample_input = '''8 5 100
CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
TAGTACCGAGACCGAAAGAAGTATACAGGCGT
TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
AATCCACCAGCTCCACGTGCAATGTTGGCCTA'''


def mismatch(str1, str2):
    count = 0
    for num in range(0, len(str1)):
        if str1[num] is not str2[num]:
            count += 1

    return count


def rand_motif(input_text, k):
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


sample_data = sample_input.split('\n')

initial_numbers = sample_data[0].split(' ')
input_text = sample_data[1:]

k = int(initial_numbers[0])
d = int(initial_numbers[1])
n = int(initial_numbers[2])

motifs = rand_motif(input_text, k)

best_motifs = motifs
for j in range(0, n):
    i = random.randint(1, d)
    _rand_motif = rand_motif([input_text[i - 1]], k)

    temp_motifs = copy.deepcopy(motifs)
    del temp_motifs[i - 1]

    temp_motifs.insert(i - 1, _rand_motif[0])

    temp_motifs_score = score(temp_motifs)
    best_motifs_score = score(best_motifs)

    if sum(temp_motifs_score) < sum(best_motifs_score):
        best_motifs = temp_motifs

for line in best_motifs:
    print line


