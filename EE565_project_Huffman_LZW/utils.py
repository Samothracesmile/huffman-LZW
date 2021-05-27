import numpy as np


magic_str = '\n'


def bins2chars(bin_str, bin_chunk_len=8):
    char_str=''
    bin_chunk_len=8
    chunks = [bin_str[i:i+bin_chunk_len] for i in range(0, len(bin_str), bin_chunk_len)]
    
    # convert the bin chunks into char
    for chunk in chunks:
        char_str += chr(int(chunk, 2))
    # add the last chunk length to char
    char_str += str(len(chunks[-1]))
    
    return char_str

def chars2bins(char_str, bin_chunk_len=8):
    bin_str = ''
    for char in char_str[:-2]:
        chunk_bin_str = bin(ord(char))[2:]
        chunk_bin_str = (bin_chunk_len - len(chunk_bin_str))*'0' + chunk_bin_str
        bin_str += chunk_bin_str

    # last chunks
    last_chunk_len = int(char_str[-1])
    last_chunk_bin_str = bin(ord(char_str[-2]))[2:]
    last_chunk_bin_str = (last_chunk_len - len(last_chunk_bin_str))*'0' + last_chunk_bin_str

    bin_str += last_chunk_bin_str

    return bin_str


def digit2bin(digit, bit_num):
    '''Convert the deci digit to zeropadded bit string'''
    assert bit_num >= np.log2(digit)
    bin_str = bin(digit)[2:]
    # zero padding
    bin_str = (bit_num - len(bin_str))*'0' + bin_str
    return bin_str


def bin2digit(bin_str):
    '''Covert the bit string back to deci digit'''
    return int(bin_str, 2)



def huffman_compress(all_str, encoding_dict):
    '''Convert the all str according to the preconstructed encoding_dict'''

    #1. get the compressed dict str
    dict_comp_str = ''
    dict_comp_str += str(len(encoding_dict)) # save dict length
    dict_comp_str += magic_str
    for cha, bin_codeword in encoding_dict.items():
    #     print(cha, bin_codeword, bins2chars(bin_codeword))
        dict_code = cha + str(len(bins2chars(bin_codeword))) + bins2chars(bin_codeword)
        dict_comp_str += dict_code
    # print(repr(dict_comp_str))

    #2. get the compressed context str
    context_comp_str = ''
    context_comp_binstr = ''
    for cha in all_str:
        context_comp_binstr += encoding_dict[cha]
    context_comp_str = bins2chars(context_comp_binstr, bin_chunk_len=8)


    return dict_comp_str, context_comp_str