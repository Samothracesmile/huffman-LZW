import numpy as np
# def lzw_encoder(all_str, lwz_dict=None):

#     if not lwz_dict:
#         print('LZW Encoder using ascii for dict initialization.')

#         ascii_size = 256
#         ascii_chars = [chr(i) for i in range(ascii_size)]
#         lwz_dict = dict(zip(ascii_chars, range(ascii_size)))

#     # lwz_dict = ini_lwz_dict
#     lwz_codewords = []
    
#     # initialized string 
#     s = all_str[0]
#     pt_idx = 1
#     while pt_idx < len(all_str):
#         c = all_str[pt_idx]
#         if s+c in lwz_dict.keys():
#             s = s+c
#         else:
#             lwz_codewords.append(lwz_dict[s])
#             lwz_dict[s+c] = len(lwz_dict)
#             s = c

#         if pt_idx == len(all_str)-1: # c is the last and sigle
#             lwz_codewords.append(lwz_dict[s])

#         pt_idx += 1
    
#     return lwz_codewords
  

def lzw_encoder(all_str, dict_size=None, lwz_dict=None, return_dict=False):

    if not dict_size:
        dict_size = len(all_str) #Should aways give a dict size

    if not lwz_dict:
#         print('LZW Encoder using ascii for dict initialization.')
        ascii_size = 256
        ascii_chars = [chr(i) for i in range(ascii_size)]
        lwz_dict = dict(zip(ascii_chars, range(ascii_size)))

    # lwz_dict = ini_lwz_dict
    lwz_codewords = []
    
    # initialized string 
    s = all_str[0]
    pt_idx = 1
    while pt_idx < len(all_str):
        c = all_str[pt_idx]
        if s+c in lwz_dict.keys():
            s = s+c
        else:
            lwz_codewords.append(lwz_dict[s])
            # update the dictionary until saturated
            if len(lwz_dict) < dict_size:
                lwz_dict[s+c] = len(lwz_dict)

            s = c

        if pt_idx == len(all_str)-1: # c is the last and sigle
            lwz_codewords.append(lwz_dict[s])

        pt_idx += 1
    
    
    if not return_dict:
        return lwz_codewords
    else:
        return lwz_codewords, lwz_dict



def lzw_decoder(lwz_codewords, ini_lwz_dict=None):

    if not ini_lwz_dict:
        # print('LZW decoder using ascii for dict initialization.')

        ascii_size = 256
        ascii_chars = [chr(i) for i in range(ascii_size)]
        ini_lwz_dict = dict(zip(ascii_chars, range(ascii_size)))

    
    inv_lwz_dict = {v: k for k, v in ini_lwz_dict.items()}
    de_all_str = ''

    prior_lwz_code = lwz_codewords[0]
    s = inv_lwz_dict[prior_lwz_code]
    de_all_str += s

    pt_idx = 1
    while pt_idx < len(lwz_codewords):
    # for i in range(300):
        lwz_code = lwz_codewords[pt_idx]
        if lwz_code not in inv_lwz_dict.keys():
            new_s = inv_lwz_dict[prior_lwz_code] + inv_lwz_dict[prior_lwz_code][0]
            inv_lwz_dict[len(inv_lwz_dict)] = new_s
            de_all_str += new_s
        else:
            new_s = inv_lwz_dict[prior_lwz_code] + inv_lwz_dict[lwz_code][0]
            inv_lwz_dict[len(inv_lwz_dict)] = new_s
            de_all_str += inv_lwz_dict[lwz_code]

        pt_idx += 1
        prior_lwz_code = lwz_code

    return de_all_str
    # return de_all_str,inv_lwz_dict
