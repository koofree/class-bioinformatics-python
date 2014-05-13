__author__ = 'koo'

class Trie:
    """ Trie Class """

    def __init__(self):
        self.offset = 0
        self.trie = [list()]
        self.nodes = list()
        start_node = {'parent': None, 'child': [], 'value': '!', 'seq': self.offset + 1}
        self.add_node(start_node)

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
                self.offset += 1
                new_node = {'parent': parent, 'child': [], 'value': ch, 'seq': self.offset + 1}
                parent['child'].append(new_node)
                parent = new_node

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
        self.traversal_node(self.root_node())

    def traversal_node(self, node):
        for child in node['child']:
            print node['seq'], child['seq'], child['value']
            self.traversal_node(child)

    def root_node(self):
        return self.nodes[0]


def prefix_trie_matching(text, trie):
    i = 0
    length = len(text)
    start_node = trie.root_node()
    v = start_node
    while True:
        if i >= length:
            return True
        symbol = text[i]
        i += 1
        if trie.has_edge(v, symbol):
            v = trie.get_child(v, symbol)
        else:
            return False

sample_input = '''AATCGGGTTCAATCGGGGT
ATCG
GGGT'''

input_lines = sample_input.split('\n')

result = ''
for i in range(0, len(input_lines[0])):
    trie = Trie()
    trie.make_node(input_lines[0][i:])
    for line in input_lines[1:]:
        if prefix_trie_matching(line, trie):
            result += str(i) + ' '

print result