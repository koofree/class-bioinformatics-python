__author__ = 'koo'

import pkg_resources

amino_acid_mass_dic = {'G': 57,
                       'A': 71,
                       'S': 87,
                       'P': 97,
                       'V': 99,
                       'T': 101,
                       'C': 103,
                       'I': 113,
                       'L': 113,
                       'N': 114,
                       'D': 115,
                       'K': 128,
                       'Q': 128,
                       'E': 129,
                       'M': 131,
                       'H': 137,
                       'F': 147,
                       'R': 156,
                       'Y': 163,
                       'W': 186}

inverted_amino_acid_mass_dic = {57: 'G',
                                71: 'A',
                                87: 'S',
                                97: 'P',
                                99: 'V',
                                101: 'T',
                                103: 'C',
                                113: ['I', 'L'],
                                114: 'N',
                                115: 'D',
                                128: ['K', 'Q'],
                                129: 'E',
                                131: 'M',
                                137: 'H',
                                147: 'F',
                                156: 'R',
                                163: 'Y',
                                186: 'W'}
# CYCLOPEPTIDE SEQUENCING
################################################
def cyclopeptide_sequencing(peptide_list):
    result = ''
    for number in range(len(peptide_list), 0, -1):
        if not result is '':
            result += ' '

        forward_result = ''
        for number2 in range(len(peptide_list), 0, -1):
            inx = (number + number2 - 1) % len(peptide_list)
            if not forward_result is '':
                forward_result += '-'
            forward_result += peptide_list[inx]

        backward_result = ''
        for number2 in range(0, len(peptide_list)):
            inx = (number + number2 - 1) % len(peptide_list)
            if not backward_result is '':
                backward_result += '-'
            backward_result += peptide_list[inx]

        if number % 2 is 1:
            result += forward_result + ' ' + backward_result
        else:
            result += backward_result + ' ' + forward_result
    return result

################################################

input1_text = pkg_resources.resource_string('chapter2', 'data/2-5/input1')
output1_text = pkg_resources.resource_string('chapter2', 'data/2-5/output1')
input2_text = pkg_resources.resource_string('chapter2', 'data/2-5/input2')
output2_text = pkg_resources.resource_string('chapter2', 'data/2-5/output2')

peptide_list1 = input1_text.split(' ')
peptide_list2 = input1_text.split(' ')

for peptide1 in peptide_list1:
    if not inverted_amino_acid_mass_dic.has_key(int(peptide1)):
        peptide_list2.remove(peptide1)

result1 = cyclopeptide_sequencing(peptide_list2)

peptide_list1 = input2_text.split(' ')
peptide_list2 = input2_text.split(' ')

for peptide1 in peptide_list1:
    if not inverted_amino_acid_mass_dic.has_key(int(peptide1)):
        peptide_list2.remove(peptide1)

result2 = cyclopeptide_sequencing(peptide_list2)

assert output1_text == result1

print result1
print result2

