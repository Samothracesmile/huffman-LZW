#!/bin/sh

cd /home/yihaoxia/Desktop/EE565_information_theory/Project/EE565_project

source activate python2

# # Huffman Coding
# python Huffman_encoding.py --input ./data/principia.txt \
#                             --output ./data/principia_huffman_comp.txt

# python Huffman_decoding.py --input ./data/principia_huffman_comp.txt \
#                             --output ./data/principia_huffman_decomp.txt \
#                             --valid_input ./data/principia.txt \

# # LZW Compression
# python LZW_encoding.py --input ./data/principia.txt \
#                             --codeword_bit 12 \
#                             --output ./data/principia_LZW_comp_12.txt

# python LZW_decoding.py --input ./data/principia_LZW_comp_12.txt \
#                             --output ./data/principia_LZW_decomp_12.txt \
#                             --valid_input ./data/principia.txt \


# # LZW Compression
# python LZW+Huffman_encoding.py --input ./data/principia.txt \
#                             --codeword_bit 12 \
#                             --output ./data/principia_LZH_comp_12.txt

python LZW+Huffman_decoding.py --input ./data/principia_LZH_comp_12.txt \
                            --output ./data/principia_LZH_decomp_12.txt \
                            --valid_input ./data/principia.txt \