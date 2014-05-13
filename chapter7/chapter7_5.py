__author__ = 'koo'

import sys


class Trie:
    """ Trie Class """

    def __init__(self):
        self.offset = 0
        self.trie = [list()]
        self.nodes = list()
        start_node = {'parent': None, 'child': [], 'value': '!', 'seq': self.offset + 1}
        self.add_node(start_node)
        self.parent_map = dict()
        self.temp_str = ''
        self.traversal_str = list()

    def make_node(self, str):
        parent = self.nodes[0]
        for i in range(0, len(str)):

            ch = str[i]
            has_child = False
            child = None
            for _child in parent['child']:
                if _child['value'] == ch:
                    child = _child
                    has_child = True
                    break

            if has_child:
                parent = child
            else:
                if not self.parent_map.has_key(ch):
                    self.parent_map[ch] = list()

                self.offset += 1
                new_node = {'parent': parent, 'child': [], 'value': ch, 'seq': self.offset + 1}
                parent['child'].append(new_node)
                parent = new_node
                self.parent_map[ch].append(new_node)

    def has_edge(self, node, ch):
        has_child = False
        for _child in node['child']:
            if _child['value'] == ch:
                has_child = True

        return has_child

    def get_child(self, node, ch):
        child = None
        for _child in node['child']:
            if _child['value'] == ch:
                child = _child
                break
        return child

    def add_node(self, node):
        if len(self.nodes) < self.offset + 1:
            self.nodes.append(node)
        else:
            self.nodes[self.offset] = node;

    def reset(self):
        self.offset = 0

    def get_nodes(self):
        return self.nodes

    def traversal(self):
        self.traversal_str = list()
        self.traversal_node(self.root_node())
        return self.traversal_str

    def traversal_node(self, node):
        for child in node['child']:
            if not len(node['child']) is 1:
                self.traversal_str.append(self.temp_str)
                self.temp_str = ''
            self.temp_str += child['value']
            self.traversal_node(child)

    def root_node(self):
        return self.nodes[0]

    def parent_nodes(self, ch):
        return self.parent_map[ch]


def trie_matching(text, trie):
    result = ''
    temp_result = ''
    i = 0
    length = len(text)
    start_node = trie.root_node()
    v = start_node
    exist = False
    while True:
        if i >= length:
            if exist:
                return temp_result
            else:
                exist = True
                i = 0
                continue
        symbol = text[i]
        if len(v['child']) is 0:
            return result
        elif trie.has_edge(v, symbol):
            v = trie.get_child(v, symbol)
            if exist:
                temp_result += symbol
            i += 1
        else:
            if len(result) < len(temp_result):
                result = temp_result
            if len(v['child']) is 1:
                v = v['child'][0]
            else:
                return temp_result


sample_input = '''TCGGTAGATTGCGCCCACTC
AGGGGCTCGCAGTGTAAGAA'''

inputs = sample_input.split('\n')

trie = Trie()
for i in range(0, len(inputs[0])):
    trie.make_node(inputs[0][i:])

trie2 = Trie()
for i in range(0, len(inputs[1])):
    trie2.make_node(inputs[1][i:])

traversal1 = trie.traversal()
traversal2 = trie2.traversal()

result = ''
temp_result = ''
for i in range(0, len(traversal1)):
    for j in range(0, len(traversal2)):
        temp_result = ''
        str1 = traversal1[i]
        str2 = traversal2[j]
        for k in range(0, len(str1) if len(str1) < len(str2) else len(str2)):
            if str1[k] == str2[k]:
                temp_result += str1[k]
            else:
                if len(result) < len(temp_result):
                    result = temp_result
                break

print result