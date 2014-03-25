__author__ = 'koo'

# Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.
# Input: An amino acid string Peptide.
# Output: Cyclospectrum(Peptide).

import urllib2
import pkg_resources


# Integer Math Table
################################################
Integer_Mass_url = "https://stepic.org/media/attachments/lessons/98/integer_mass_table.txt"
Integer_Mass = urllib2.urlopen(Integer_Mass_url)

Integer_Mass_dic = {}

for line in Integer_Mass:
    split_line = line.split(' ')
    code = split_line[0]
    number = split_line[1].rstrip('\n')
    Integer_Mass_dic[code] = number

# print Integer_Mass_dic
################################################


input1_text = pkg_resources.resource_string('chapter2', 'data/2-3/input1')
output1_text = pkg_resources.resource_string('chapter2', 'data/2-3/output1')

result_list = []
input1_length = len(input1_text)

# for circling data, expand original to twice string
double_input1_text = input1_text + input1_text
for number in range(0, input1_length + 1):
    for p in range(0, input1_length):
        sum = 0
        point1 = input1_length - p
        point2 = input1_length - p - number
        if point2 < 0:
            point1 = input1_length + point1
            point2 = input1_length + point2

        if point1 < point2:
            window_text = double_input1_text[point1:point2]
        else:
            window_text = double_input1_text[point2:point1]

        for char in window_text:
            sum += int(Integer_Mass_dic[char])
        result_list.append(str(sum))
        if number is 0 or number is len(input1_text):
            break;

result_list.sort()
print result_list