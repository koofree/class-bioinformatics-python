__author__ = 'koo'

from chapter2_5 import cyclopeptide_sequencing, inverted_amino_acid_mass_dic

import pkg_resources

input1_text = pkg_resources.resource_string('chapter2', 'data/2-6/input1')
output1_text = pkg_resources.resource_string('chapter2', 'data/2-6/output1')

split_input1_text = input1_text.split('\n')

N = split_input1_text[0]
Spectrum = split_input1_text[1].split(' ')
Spectrum2 = split_input1_text[1].split(' ')
for peptide1 in Spectrum:
    if not inverted_amino_acid_mass_dic.has_key(int(peptide1)):
        Spectrum2.remove(peptide1)

print Spectrum2
print cyclopeptide_sequencing(Spectrum2).split(' ')[0]