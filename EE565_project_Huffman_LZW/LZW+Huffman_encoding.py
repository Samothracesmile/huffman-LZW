'''
Use the LZW to compress the text and use the Huffman Coding to compress the LWZ codewords
1. Huffman can further reduce the compression rate because LZW codewords is not evenly distributed
2. For LZW compression with smaller dictionary size requirement, the uneven distribution maybe more serious
3. Not all the dict size would be larger than the number of codewords, futher encode teh codewords would avoid the digital length wasting

Yihao Xia 

USC 2021Spring EE565 Information Theory Project
'''
import numpy as np
from lzwutils import lzw_encoder, lzw_decoder
from utils import bins2chars, digit2bin, chars2bins,bin2digit

from collections import defaultdict
from huffNode import gen_huffman_tree

import argparse


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


parser = argparse.ArgumentParser()

# data set setting
parser.add_argument('--input', type=str)
parser.add_argument('--output', type=str)
parser.add_argument('--codeword_bit', type=int, default=12)

args = parser.parse_args()
print('Args Setting:', args)


# A. Encoding
input_filename = args.input
comp_filename = args.output
codeword_bit = args.codeword_bit


# input_filename = './data/principia.txt'
all_str = open(input_filename, 'r').read()

# A. LZW encoding
# codeword_bit = 12
# for codeword_bit in range(8, 19):
dict_size = 2**codeword_bit
lwz_codewords = lzw_encoder(all_str,dict_size=dict_size)

cw_count_dict = defaultdict(int)
for cw in lwz_codewords:
    cw_count_dict[cw] += 1

huffman_tree = gen_huffman_tree(cw_count_dict)

leafs = []
huff_encoding(huffman_tree)
huff_cws = [leaf.huffcode for leaf in leafs]
lzw_cws = [leaf.cha for leaf in leafs] # lzw code word table
encoding_dict = dict(zip(lzw_cws, huff_cws))

#1. get the compressed dict str
magic_str = '\n'
dict_comp_str = ''
dict_comp_str += str(len(encoding_dict)) # save dict length
dict_comp_str += magic_str
dict_comp_str += str(len(bins2chars(digit2bin(1, codeword_bit)))) # save lwz codeword char length
dict_comp_str += magic_str
for cha, bin_codeword in encoding_dict.items():
#     dict_code = str(cha) + str(len(bins2chars(bin_codeword))) + bins2chars(bin_codeword) # too large
    dict_code = bins2chars(digit2bin(cha, codeword_bit)) + str(len(bins2chars(bin_codeword))) + bins2chars(bin_codeword)
    dict_comp_str += dict_code

#2. get the compressed context str
context_comp_str = ''
context_comp_binstr = ''
for cha in lwz_codewords:
    context_comp_binstr += encoding_dict[cha]
context_comp_str = bins2chars(context_comp_binstr, bin_chunk_len=8)

comp_str = dict_comp_str + context_comp_str

print(30*'*')
print('codeword_bit = ',codeword_bit)
print('LZW+Huff compress size', float(len(comp_str))/len(all_str))


# 5. save the comp_str to file
# comp_filename = './data/principia_lzw_huffman_compressed.txt'
with open(comp_filename, 'w') as f:
    f.write(comp_str)