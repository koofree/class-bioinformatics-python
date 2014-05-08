__author__ = 'koo'

sample_raw_input = '(-3 +4 +1 +5 -2)'

sample_input = sample_raw_input.strip('()').split(' ')


def _range_(k, p):
    return range(k, len(p) + 1)


def _range_(p):
    return range(1, len(p) + 1)


def check_reflect(num1, num2):
    return int(num1) + int(num2) is 0


def _index_(k):
    return k - 1


def is_not_sorted(k, p):
    return int(p[_index_(k)]) is not k


def reversal(p):
    new_p = list()
    for i in _range_(p):
        val = int(p[_index_(i)])
        if val > 0:
            new_p.insert(0, '-' + str(val))
        elif val < 0:
            new_p.insert(0, '+' + str(-val))
        else:
            new_p.insert(0, str(-val))
    return new_p


def k_sorting_reversal(k, p):
    new_p = list()
    sub_p = list()
    done = False
    for _k in _range_(p):
        val = p[_index_(_k)]
        if _k < k:
            new_p.append(val)
        elif done:
            new_p.append(val)
        elif int(val) is k or check_reflect(val, k):
            sub_p.append(val)
            new_p.extend(reversal(sub_p))
            done = True
        else:
            sub_p.append(val)

    return new_p


def _print(p):
    result = '('
    for el in p:
        result += el + ' '
    result = result.rstrip() + ')'
    print result


def greedy_sorting(p):
    approx_reversal_distance = 0
    for k in _range_(p):
        if is_not_sorted(k, p):
            p = k_sorting_reversal(k, p)
            approx_reversal_distance += 1
            _print(p)
        if check_reflect(p[_index_(k)], k):
            p[_index_(k)] = str(-k) if k < 0 else '+' + str(k)
            approx_reversal_distance += 1
            _print(p)
    return approx_reversal_distance


distance = greedy_sorting(sample_input)