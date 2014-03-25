__author__ = 'koo'

# Protein Translation Problem

import pkg_resources
import lib

print "starting chapter2-1 assignment"

# Make RNA Codon Dictionary
################################################
RNA_codon_table_1 = lib.read_url_string("https://stepic.org/media/attachments/lessons/96/RNA_codon_table_1.txt")

RNA_codon_dic = {}

for line in RNA_codon_table_1:
    split_line = line.split(' ')
    RNA_codon_dic[split_line[0]] = split_line[1].rstrip('\n')

################################################

input1_text = lib.read_file_string('chapter2/data/2-1/input1')
input2_text = pkg_resources.resource_string('chapter2', 'data/2-1/input2')
output1_text = pkg_resources.resource_string('chapter2', 'data/2-1/output1')
output2_text = pkg_resources.resource_string('chapter2', 'data/2-1/output2')

result_of_input1 = ""
for number in range(0, len(input1_text), 3):
    result_of_input1 += RNA_codon_dic.get(input1_text[number:number + 3])

result_of_input2 = ""
for number in range(0, len(input2_text), 3):
    result_of_input2 += RNA_codon_dic.get(input2_text[number:number + 3])

# check results
print result_of_input1
print result_of_input2

assert result_of_input1 == output1_text
assert result_of_input2 == output2_text

print "success"