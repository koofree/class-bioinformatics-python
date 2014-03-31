__author__ = 'koo'

'''
CODE CHALLENGE: Implement GREEDYMOTIFSEARCH.
    Input: Integers k and t, followed by a collection of strings Dna.
    Output: A collection of strings BestMotifs resulting from applying GREEDYMOTIFSEARCH(Dna,k,t).
    If at any step you find more than one Profile-most probable k-mer in a given string, use the
    one occurring first.
'''


def mismatch(str1, str2):
    count = 0
    for num in range(0, len(str1)):
        if str1[num] is not str2[num]:
            count += 1

    return count


def profile(motifs, k):
    size = float(len(motifs))
    result_profile = []
    for num in range(0, k):
        count = {'C': 0, 'G': 0, 'T': 0, 'A': 0}
        for motif in motifs:
            count[motif[num]] += 1

        for c in count:
            count[c] = float(count[c]) / size

        result_profile.append(count)

    return result_profile


def profile_probable(profile, str):
    result_count = 1.0
    for num in range(0, len(str)):
        ch = str[num]
        temp_count = profile[num]
        result_count *= temp_count[ch]

    return result_count


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

motifs_profile = profile(input_text, len(initial_line))

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

        #motif_profile = profile([line], len(line))
        motif_profile = profile([pattern, _motif], len(pattern))
        _motif_probable = profile_probable(motifs_profile, _motif)
        for _k in range(1, len(initial_line) - k + 1):
            _pattern = line[_k:_k + k]
            new_count = mismatch(pattern, _pattern)
            old_count = mismatch(pattern, _motif)

            motif_profile = profile([pattern, _pattern], len(pattern))
            new_probable = profile_probable(motifs_profile, _pattern)
            if new_probable >= _motif_probable:
                _motif = _pattern
                _motif_probable = new_probable
                _motif_score = new_count

        motif.append(_motif)
        motif_score.append(_motif_score)

    print motif
    print motif_score

    new_sum = sum(motif_score)
    old_sum = sum(best_motifs_score)
    if new_sum < old_sum:
        best_motifs = motif
        best_motifs_score = motif_score

for line in best_motifs:
    print line

