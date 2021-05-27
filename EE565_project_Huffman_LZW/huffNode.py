import numpy as np
import random


class Node:
    def __init__(self, wgt, cha=None, huffcode=None):

        self.l0 = None
        self.l1 = None
        self.wgt = wgt
        self.cha = cha
        self.huffcode = huffcode

    # def get_huffcode(self, )

    # def get_wgt(self, )

        
    def __add__(self, other):
        return self.wgt + other.wgt
    

    def __repr__(self):
#         if self.huffcode:
#             return f'Char: {repr(self.cha)}; Weight: {self.wgt}; codeWord: {self.huffcode}'
#         else:
#             return f'Char: {repr(self.cha)}; Weight: {self.wgt}'

        if self.huffcode:
            return 'Char: {0}; Weight: {1}; codeWord: {2}'.format(self.cha, self.wgt, self.huffcode)
        else:
            return 'Char: {0}; Weight: {1}'.format(self.cha, self.wgt)

def merge_nodes(node0,node1):
    
    parent_node = Node(node0 + node1)
    parent_node.l0 = node0
    parent_node.l1 = node1
    
    return parent_node


def gen_huffman_tree(cha_count_dict):
    
    # 2. convert the dictionary to the huffNodes
    huffnode_list = [Node(count, cha=cha) for cha, count in cha_count_dict.items()]
    huffnode_chas = [node.cha for node in huffnode_list]
    huffnode_counts = [node.wgt for node in huffnode_list]

    # 3. merge the huffNodes in to a huffTree and assign the code
    # a. find the least counted 2 nodes
    # b. merge this nodes
    # c. put the parent node back to the node list
    while len(huffnode_list) > 1:
        # a. find the least counted 2 nodes
        counts_argsort = np.argsort(huffnode_counts)
        sel_indxs = counts_argsort[:2]
        sel_counts = [huffnode_counts[i] for i in sel_indxs]
        sel_nodes = [huffnode_list[i] for i in sel_indxs]
        
        # b. other nodes
        other_indxs = counts_argsort[2:]
        other_counts = [huffnode_counts[i] for i in other_indxs]
        other_nodes = [huffnode_list[i] for i in other_indxs]
        
        # c. updates the counts
        huffnode_counts = other_counts + [sum(sel_counts)]
        huffnode_list = other_nodes + [merge_nodes(sel_nodes[0],sel_nodes[1])]

    assert len(huffnode_list) == 1 #Only one tree is built

    return huffnode_list[0]