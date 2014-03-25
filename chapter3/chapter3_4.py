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
    motif = rand_motif()
    motif_score = score(motif)

    new_sum = sum(motif_score)
    old_sum = sum(best_motifs_score)
    if new_sum < old_sum:
        best_motifs = motif
        best_motifs_score = motif_score

print best_motifs_score

for line in best_motifs:
    print line

