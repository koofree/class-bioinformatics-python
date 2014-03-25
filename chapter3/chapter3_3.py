__author__ = 'koo'

__author__ = 'koo'

'''
CODE CHALLENGE: Implement GREEDYMOTIFSEARCH with pseudocounts.
     Input: Integers k and t, followed by a collection of strings Dna.
     Output: A collection of strings BestMotifs resulting from applying GREEDYMOTIFSEARCH(Dna,k,t) with
     pseudocounts. If at any step you find more than one Profile-most probable k-mer in a given string,
     use the one occurring first.
'''


def mismatch(str1, str2):
    count = 0
    for num in range(0, len(str1)):
        if str1[num] is not str2[num]:
            count += 1

    return count


sample_input = '''3 5
GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG'''

sample_data = sample_input.split('\n')

initial_numbers = sample_data[0].split(' ')
input_text = sample_data[1:]

k = int(initial_numbers[0])
d = int(initial_numbers[1])

best_motifs = []
best_motifs_score = []

initial_line = input_text[0]
initial_pattern = initial_line[0:k]

for line in input_text:
    best_motifs.append(line[0:k])
    best_motifs_score.append(mismatch(initial_pattern, line[0:k]))

for _k in range(0, len(initial_line) - k + 1):
    motif = []
    motif_score = []
    pattern = initial_line[_k:_k + k]
    motif.append(pattern)
    for num in range(1, d):
        line = input_text[num]
        _motif = line[0:k]
        _motif_score = mismatch(pattern, _motif)
        for _k in range(1, len(initial_line) - k + 1):
            _pattern = line[_k:_k + k]
            new_count = mismatch(pattern, _pattern)
            old_count = mismatch(pattern, _motif)
            if new_count < old_count:
                _motif = _pattern
                _motif_score = new_count
        motif.append(_motif)
        motif_score.append(_motif_score)

    new_sum = sum(motif_score)
    old_sum = sum(best_motifs_score)
    if new_sum < old_sum:
        best_motifs = motif
        best_motifs_score = motif_score

for line in best_motifs:
    print line

