'''
Use the LZW to compress the text
Yihao Xia 

USC 2021Spring EE565 Information Theory Project
'''
import numpy as np
from lzwutils import lzw_encoder, lzw_decoder
from utils import bins2chars, digit2bin, chars2bins
import argparse


parser = argparse.ArgumentParser()

# data set setting
parser.add_argument('--input', type=str)
parser.add_argument('--output', type=str)
parser.add_argument('--codeword_bit', type=int, default=17)

args = parser.parse_args()
print('Args Setting:', args)


# A. Encoding
input_filename = args.input
comp_filename = args.output
codeword_bit = args.codeword_bit

# load input
all_str = open(input_filename, 'r').read()

# A. LZW encoding
# codeword_bit = 15
# for codeword_bit in range(8, 19):
dict_size = 2**codeword_bit
lwz_codewords = lzw_encoder(all_str,dict_size=dict_size)
# de_all_str = lzw_decoder(lwz_codewords)
# assert de_all_str == all_str

# lwz_codewords to char and save 
lwz_cw_bin_str = ''
magic_str = '\n'
for digit in lwz_codewords:
    lwz_cw_bin_str += digit2bin(digit, codeword_bit)
lwz_cw_char_str = bins2chars(lwz_cw_bin_str)
# add codeword_bit info into char
lwz_cw_char_str = str(codeword_bit) + magic_str + lwz_cw_char_str

print(30*'*')
print('The compression rate is {}'.format(float(len(lwz_cw_char_str))/len(all_str)))

# 5. save the comp_str to file
with open(comp_filename, 'w') as f:
    f.write(lwz_cw_char_str)
