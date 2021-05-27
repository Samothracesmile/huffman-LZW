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


parser = argparse.ArgumentParser()

# data set setting
parser.add_argument('--input', type=str)
parser.add_argument('--output', type=str)
parser.add_argument('--valid_input', type=str, default='', help='original text file')

args = parser.parse_args()
print('Args Setting:', args)


comp_filename = args.input
decomp_filename = args.output
input_filename = args.valid_input


# B. Decoding
# comp_filename = './data/principia_huffman_compressed.txt'
# comp_filename = './data/principia_lzw_huffman_compressed.txt'
with open(comp_filename, 'r') as f:
    dict_size = int(f.readline())
    lwz_cw_size=int(f.readline())
    # readout the huff dictionary
    lwz_cws = []
    bin_codewords = []
    for i in range(dict_size):
        lwz_cw = f.read(lwz_cw_size)
        lwz_cw = bin2digit(chars2bins(lwz_cw))
        codeword_size = f.read(1)
        
        bin_codeword = chars2bins(f.read(int(codeword_size)), bin_chunk_len=8)
    #     print(repr(char),codeword_size,bin_codeword)
        lwz_cws.append(lwz_cw)
        bin_codewords.append(bin_codeword)    

    decoding_dict = dict(zip(bin_codewords, lwz_cws))
    # readout the context binary string
    context_comp_binstr = chars2bins(f.read(), bin_chunk_len=8)

# Huffman decoding 
bin_codewords_size = [len(codeword) for codeword in bin_codewords]
unique_bin_codewords_size = np.unique(bin_codewords_size)

lwz_codewords = []
while len(context_comp_binstr) > 0:
    for cw_size in unique_bin_codewords_size:
        abin_cw_seg = context_comp_binstr[:cw_size]
        if abin_cw_seg in bin_codewords:
            lwz_codewords += [decoding_dict[abin_cw_seg]]
            context_comp_binstr = context_comp_binstr[cw_size:]

# LZW decoding
deco_all_str = lzw_decoder(lwz_codewords)
# 5. save the decomp_str to file
# decomp_filename = './data/principia_lzw_huffman_decompressed.txt'
with open(decomp_filename, 'w') as f:
    f.write(deco_all_str)



# C. Valid the decompressed text is lossless
# input_filename = './data/principia.txt'
if input_filename:
    all_str = open(input_filename, 'r').read()

    if not deco_all_str == all_str:
        print('Error the decompression is not lossless')
    else:
        print('The decompression works properly')