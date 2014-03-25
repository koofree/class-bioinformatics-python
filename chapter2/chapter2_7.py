__author__ = 'koo'

'''
Spectral Convolution Problem: Compute the convolution of a spectrum.
    Input: A collection of integers Spectrum.
    Output: The list of elements in the convolution of Spectrum. If an element has multiplicity k, it should
    appearexactly k times; you may return the elements in any order.

CODE CHALLENGE: Solve the Spectral Convolution Problem.

Sample Input:
    0 137 186 323

Sample Output:
    137 137 186 186 323 49
'''

import lib


def spectral_convolution(spectrum, last_idx):
    result = []

    for integer in spectrum:
        for inx in range(0, len(spectrum) - last_idx):
            result.append(spectrum[inx + 1])

            if last_idx > 1:
                last_idx = last_idx - 1
                spectral_convolution(spectrum, last_idx)

    return result


spectrum_text1 = lib.read_file_string('chapter2/data/2-7/input1')
spectrum = spectrum_text1.split(' ')

print spectral_convolution(spectrum, len(spectrum))




