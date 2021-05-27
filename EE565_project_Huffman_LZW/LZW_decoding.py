import numpy as np
from lzwutils import lzw_encoder, lzw_decoder
from utils import bins2chars, digit2bin, chars2bins, bin2digit

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


# B. LZW deconding
# comp_filename = './data/principia_lzw_15_compressed.txt'
with open(comp_filename, 'r') as f:
    codeword_bit = int(f.readline())
    lwz_cw_com_str = f.read()
    lwz_cw_com_bin_str = chars2bins(lwz_cw_com_str)
    lwz_com_bin_codewords = [lwz_cw_com_bin_str[i:i+codeword_bit] for i in range(0, len(lwz_cw_com_bin_str), codeword_bit)]
    lwz_com_codewords = [bin2digit(cw) for cw in lwz_com_bin_codewords]
    deco_all_str = lzw_decoder(lwz_com_codewords)


# save the decomp_str to file
with open(decomp_filename, 'w') as f:
    f.write(deco_all_str)


# C. Valid the decompressed text is lossless
if input_filename:
    all_str = open(input_filename, 'r').read()
    if not deco_all_str == all_str:
        print('Error the decompression is not lossless')
    else:
        print('The decompression works properly')