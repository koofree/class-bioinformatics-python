__author__ = 'koo'

sample_input = '''GGTA
CG
GGC'''


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

            if has_child:
                parent = child
            else:
                self.offset += 1
                new_node = {'parent': parent, 'child': [], 'value': ch, 'seq': self.offset + 1}
                parent['child'].append(new_node)
                parent = new_node


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
        self.traversal_node(self.nodes[0])

    def traversal_node(self, node):
        for child in node['child']:
            print node['seq'], child['seq'], child['value']
            self.traversal_node(child)


input_lines = sample_input.split('\n')

trie = Trie()
for line in input_lines:
    trie.make_node(line)

trie.traversal()