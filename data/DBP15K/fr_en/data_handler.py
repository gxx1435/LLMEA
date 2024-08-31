from urllib.parse import unquote
import chardet

# with open('ent_ids_1', 'rb') as f:
#     raw_data = f.read()  # 读取文件的前 10000 字节
#     result = chardet.detect(raw_data)
#     encoding = result['encoding']
#     print(encoding)

# entity_correction = {}
# with open('entity_correction.txt', 'r') as f:
#     for line in f.readlines():
#         line = line.split('\t')
#         id = line[0].strip()
#         ent = line[1].strip()
#         entity_correction.update({id: ent})


ent_ids_1_dict_corrected = {}
with open('ent_ids_1', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = unquote(line)
        tmp = line.strip()
        tmp = tmp.replace('\n', "")
        tmp = tmp.replace('_', ' ')
        tmp = tmp.replace("  ", " ")
        tmp = tmp.replace(' )', ')')
        content = tmp.split("\t")
        if len(content[0]) > 5:
            assert False
        id = content[0]
        ent = content[1].split("/")[-1]
        # if id in entity_correction.keys():
        #     ent = entity_correction[id]
        ent_ids_1_dict_corrected.update({id: ent})

with open('ent_ids_1_new', 'w') as f:
    for key in ent_ids_1_dict_corrected.keys():
        f.write(key+'\t'+ent_ids_1_dict_corrected[key]+'\n')

ent_ids_2_dict = {}
with open('ent_ids_2', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = unquote(line)
        tmp = line.strip()
        tmp = tmp.replace('\n', "")
        tmp = tmp.replace('_', ' ')
        tmp = tmp.replace("  ", " ")
        tmp = tmp.replace(' )', ')')
        content = tmp.split("\t")
        if len(content[0]) > 5:
            assert False
        id = content[0]
        ent = content[1].split("/")[-1]
        # line = line.split('\t')
        # id = line[0].strip()
        # ent = line[1].split('/')[-1].strip()
        # ent = ent.replace('_', ' ')
        # ent = ent.split('(')[0]
        # ent = ent.split('（')[0]
        ent_ids_2_dict.update({id: ent})

with open('ent_ids_2_new', 'w') as f:
    for key in ent_ids_2_dict.keys():
        f.write(key+'\t'+ent_ids_2_dict[key]+'\n')

id_1s = []
id_2s = []
with open('ill_ent_ids') as f:
    for line in f.readlines():
        line = line.split('\t')
        id_1 = line[0].strip()
        id_2 = line[1].strip()
        id_1s.append(id_1)
        id_2s.append(id_2)
ill_ent_ids_new = sorted([(id_1, id_2) for id_1, id_2 in zip(id_1s, id_2s)], key=lambda x: int(x[0]))

with open('ill_ent_ids_new', 'w') as f:
    for line in ill_ent_ids_new:
        f.write(line[0]+'\t'+line[1]+'\n')

ill_ent_pairs = {}
with open('ill_ent_ids_new', 'r') as f:
    for line in f.readlines():
        line = line.split('\t')
        id_1 = line[0].strip()
        id_2 = line[1].strip()
        ill_ent_pairs.update({id_1: id_2})

with open('new_ent_ids_1', 'w') as f1, open('new_ent_ids_2_aligned', 'w') as f2:
    for id in ill_ent_pairs.keys():
        f1.write(id+'\t'+ent_ids_1_dict_corrected[id]+'\n')
        f2.write(ill_ent_pairs[id]+'\t'+ent_ids_2_dict[ill_ent_pairs[id]]+'\n')


# id_dict = []
# with open('newgraph_1', 'r') as f:
#     for line in f.readlines():
#         if line == '\n':
#             continue
#         id_1 = line.split(' ')[0]
#         id_2 = line.split(' ')[1].strip()
#         id_dict.append((id_1, id_2))
#
# with open('newgraph_1', 'w') as f:
#     for item in id_dict:
#         f.write(item[0]+'\t'+item[1]+'\n')

# id_dict = []
# with open('newgraph_2', 'r') as f:
#     for line in f.readlines():
#         if line == '\n':
#             continue
#         id_1 = line.split(' ')[0]
#         id_2 = line.split(' ')[1].strip()
#         id_dict.append((id_1, id_2))
#
# with open('newgraph_2', 'w') as f:
#     for item in id_dict:
#         f.write(item[0]+'\t'+item[1]+'\n')




