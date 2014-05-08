__author__ = 'koo'

sample_raw_input = '(+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)'

sample_input = sample_raw_input.strip('()').split(' ')


def pair(p):
    new_p = list()
    new_p.extend(p)
    new_p.insert(0, '0')
    new_p.append('+' + str(len(p) + 1))
    new_pairs = list()
    for i in range(0, len(new_p) - 1):
        new_pair = [new_p[i], new_p[i + 1]]
        new_pairs.append(new_pair)
    return new_pairs

def breakpoints(p):
    count = 0
    for _pair in p:
        count += 0 if int(_pair[1]) - int(_pair[0]) is 1 else 1

    return count


pairs = pair(sample_input)

print breakpoints(pairs)