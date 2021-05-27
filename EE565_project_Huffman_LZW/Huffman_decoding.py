'''
Use the Huffman decoding to decompress the text
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
parser.add_argument('--valid_input', type=str, default='', help='original text file')

args = parser.parse_args()
print('Args Setting:', args)


# B. Decoding
comp_filename = args.input
decomp_filename = args.output
input_filename = args.valid_input

with open(comp_filename, 'r') as f:
    dict_size = int(f.readline())
    # readout the huff dictionary
    chars = []
    bin_codewords = []
    for i in range(dict_size):
        char = f.read(1)
        codeword_size = f.read(1)
        codeword_size = int(codeword_size)
        bin_codeword = chars2bins(f.read(codeword_size), bin_chunk_len=8)
    #     print(repr(char),codeword_size,bin_codeword)
        chars.append(char)
        bin_codewords.append(bin_codeword)    

    decoding_dict = dict(zip(bin_codewords, chars))
    # readout the context binary string
    context_comp_binstr = chars2bins(f.read(), bin_chunk_len=8)

# faster
bin_codewords_size = [len(codeword) for codeword in bin_codewords]
unique_bin_codewords_size = np.unique(bin_codewords_size)

deco_all_str = ''
while len(context_comp_binstr) > 0:
    for cw_size in unique_bin_codewords_size:
        abin_cw_seg = context_comp_binstr[:cw_size]
        if abin_cw_seg in bin_codewords:
            deco_all_str += decoding_dict[abin_cw_seg]
            context_comp_binstr = context_comp_binstr[cw_size:]


# 5. save the decomp_str to file
with open(decomp_filename, 'w') as f:
    f.write(deco_all_str)


# C. Valid the decompressed text is lossless
if input_filename:
    all_str = open(input_filename, 'r').read()
    if not deco_all_str == all_str:
        print('Error the decompression is not lossless')
    else:
        print('The decompression works properly')