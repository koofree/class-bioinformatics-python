__author__ = 'koo'

import urllib2

Tyrocidine_B1_theoretical_spectrum_url = 'https://stepic.org/media/attachments/lessons/98/Tyrocidine_B1_theoretical_spectrum_1.txt'
Tyrocidine_B1_theoretical_spectrum = urllib2.urlopen(Tyrocidine_B1_theoretical_spectrum_url)

Tyrocidine_B1_theoretical_spectrum_dic = {}

for line in Tyrocidine_B1_theoretical_spectrum:
    split_line = line.split(' ')
    code = split_line[0]
    number = split_line[1].rstrip('\n')
    Tyrocidine_B1_theoretical_spectrum_dic[code] = number

print Tyrocidine_B1_theoretical_spectrum_dic