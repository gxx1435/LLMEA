import json

# with open('text_input_no_train_11_wxt.txt') as f:
#     lines = f.readlines()
# print(len(lines))

# dict = {}
# with open('newgraph_2', 'r') as f:
#     for line in f.readlines():
#
#         id1 = line.split(' ')[0]
#         id2 = line.split(' ')[1]
#         dict.update({id1: id2})
#
# with open('newgraph_2', 'w') as f:
#     for key in dict.keys():
#         f.write(key+'\t'+dict[key])

import chardet
from urllib.parse import unquote
# with open('new_ent_ids_2_aligned_rs_0.3_new', 'r', encoding='ascii') as f:
#     raw_data = f.read()  # 读取文件的前 10000 字节
#     result = chardet.detect(raw_data)
#     encoding = result['encoding']
#     decoded_data = unquote(raw_data)
#     print(encoding)
#     print(decoded_data)

with open('new_ent_ids_2_aligned_rs_0.3_new', 'r', encoding='ascii') as f:
    raw_data = f.read()
    raw_data = unquote(raw_data)
print(raw_data)

with open('new_ent_ids_2_aligned_rs_0.3_new', 'w', encoding='ascii') as f:
    f.write(raw_data)
