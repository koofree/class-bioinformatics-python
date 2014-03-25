__author__ = 'koo'

# Peptide Encoding Problem

import urllib2
import pkg_resources

# DNA Transport Map
################################################
DNA_opp_dic = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


def DNA_opp(DNA_str):
    result = ""
    for char in DNA_str:
        result += DNA_opp_dic[char]
    return result

################################################

# RNA Transform Map
################################################
RNA_tran_div = {'A': 'A', 'T': 'U', 'G': 'G', 'C': 'C'}


def RNA_tran(DNA_str):
    result = ""
    for char in DNA_str:
        result += RNA_tran_div[char]
    return result

################################################


# Make RNA Codon Dictionary
################################################
RNA_codon_table_1_url = "https://stepic.org/media/attachments/lessons/96/RNA_codon_table_1.txt"
RNA_codon_table_1 = urllib2.urlopen(RNA_codon_table_1_url)

RNA_codon_dic = {}
Inverted_RNA_dic = {}

for line in RNA_codon_table_1:
    split_line = line.split(' ')
    DNA_value = split_line[0]
    RNA_value = split_line[1].rstrip('\n')
    RNA_codon_dic[DNA_value] = RNA_value

    if not (Inverted_RNA_dic.has_key(RNA_value)):
        Inverted_RNA_dic[RNA_value] = []

    Inverted_RNA_dic[split_line[1].rstrip('\n')].append(split_line[0])

################################################


# Matching Peptide
################################################

def matchingPeptide(Peptide, RNA_str):
    result = False
    for number in range(0, len(Peptide)):
        list = Inverted_RNA_dic[Peptide[number:number + 1]]
        if RNA_str[number * 3:(number + 1) * 3] in list:
            result = True
        else:
            return False

    return result

################################################

input1_text = pkg_resources.resource_string('chapter2', 'data/2-2/input1')
input2_text = pkg_resources.resource_string('chapter2', 'data/2-2/input2')
output1_text = pkg_resources.resource_string('chapter2', 'data/2-2/output1')
output2_text = pkg_resources.resource_string('chapter2', 'data/2-2/output2')

split_input1_text = input1_text.split('\n')
DNA_str = split_input1_text[0]
Peptide = split_input1_text[1]
window_size = len(Peptide) * 3

# Make Inverse DNA
Opp_DNA_str = DNA_opp(DNA_str)

RNA_str = RNA_tran(DNA_str)
Opp_RNA_str = RNA_tran(Opp_DNA_str)

result = ""
for number in range(0, len(RNA_str) - window_size):
    RNA_window = RNA_str[number:number + window_size]
    Opp_RNA_window = Opp_RNA_str[number:number + window_size]
    if matchingPeptide(Peptide, RNA_window) or matchingPeptide(Peptide, Opp_RNA_window[::-1]):
        result += DNA_str[number:number + window_size] + '\n'

print result
print 'success'