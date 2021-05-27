'''
Use the Huffman Coding to compress the text
Yihao Xia 

USC 2021Spring EE565 Information Theory Project
'''
import numpy as np

from collections import defaultdict
from huffNode import gen_huffman_tree
from utils import bins2chars, chars2bins, huffman_compress

import argparse


parser = argparse.ArgumentParser()

# data set setting
parser.add_argument('--input', type=str)
parser.add_argument('--output', type=str)

args = parser.parse_args()
print('Args Setting:', args)


def huff_encoding(node):
    if (not node.l0 and not node.l1):
        leafs.append(node)
        
    if node.l0:
        if node.huffcode:
            node.l0.huffcode = node.huffcode + '0'
        else:
            node.l0.huffcode = '0' 
        huff_encoding(node.l0)
        
    if node.l1:
        if node.huffcode:
            node.l1.huffcode = node.huffcode + '1'
        else:
            node.l1.huffcode = '1'
        huff_encoding(node.l1)

# A. Encoding
input_filename = args.input
comp_filename = args.output

all_str = open(input_filename, 'r').read()

# 1. scan the doc and record frequency
cha_count_dict = defaultdict(int)
for cha in all_str:
    cha_count_dict[cha] += 1

# 2. gen Huffman Tree
huffman_tree = gen_huffman_tree(cha_count_dict)

# 3. gen Huffman Encoding Dictionary
leafs = []
huff_encoding(huffman_tree)
code_words = [leaf.huffcode for leaf in leafs]
chas = [leaf.cha for leaf in leafs]
encoding_dict = dict(zip(chas, code_words))

# 4. convert the doc to Huffman code
dict_comp_str, context_comp_str = huffman_compress(all_str, encoding_dict)
comp_str = dict_comp_str + context_comp_str

print('The compression rate is {}'.format(float(len(comp_str))/len(all_str)))

# 5. save the comp_str to file
with open(comp_filename, 'w') as f:
    f.write(comp_str)