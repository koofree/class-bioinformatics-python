__author__ = 'koo'

# Counting Peptides with Given Mass Problem: Compute the number of peptides of given total mass.
# Input: An integer m.
# Output: The number of linear peptides having integer mass m.

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
amino_acid_mass_list = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

input1_text = pkg_resources.resource_string('chapter2', 'data/2-4/input1')
output1_text = pkg_resources.resource_string('chapter2', 'data/2-4/output1')