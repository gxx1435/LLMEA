
# yago_new_id_1_path = 'icews_yago/new_ent_ids_1'
# yago_new_id_2_path = 'icews_yago/new_ent_ids_2_aligned'
#
# yago_1_dataset = open(yago_new_id_1_path).readlines()
# yago_2_dataset = open(yago_new_id_2_path).readlines()
#
# with open('icews_yago_complex_cases.txt', 'w') as f:
#     for i, line in enumerate(yago_1_dataset):
#         if i == 3765: break
#         entity_1 = line.split('\t')[1].strip()
#         entity_2 = yago_2_dataset[i].split('\t')[1].strip()
#         if entity_1 != entity_2:
#             f.write(entity_1+'\t\t\t'+entity_2+'\n')

# input1 = 'icews_yago/text_input_no_train_11_wxt.txt'
# input2 = 'icews_yago/text_input_no_train_22_wxt.txt'
#
# with open(input1, 'r') as f:
#     print(len(f.readlines()))
#
# with open(input2, 'r') as f:
#     print(len(f.readlines()))

# text_wrong = open('text_motif_wrong').readlines()
# code_wrong = open('code_motif_wrong').readlines()
#
# text_wrong_entity = []
# for line in text_wrong:
#     text_wrong_entity.append(line.split('\t')[0].strip())
#
# code_wrong_entity = []
# for line in code_wrong:
#     code_wrong_entity.append(line.split('\t')[0].strip())
#
# s_entity = 0
# badcase_idx = []
# badcase_entity = []
# for i, entity in enumerate(code_wrong_entity):
#     if entity not in text_wrong_entity:
#         print(entity)
#         badcase_entity.append(entity)
#         badcase_idx.append(i)
#         # s_entity += 1
#
# for idx in badcase_idx:
#     print(code_wrong[idx])

# print("Both badcases:{}".format(s_entity))

#train_input_no_trai_11_new = open('icews_wiki/text_input_no_train_11_wxt_rs_0.3_new.txt').readlines()
# print(len(train_input_no_trai_11_new))
# train_input_no_trai_22_new = open('icews_wiki/text_input_no_train_22_wxt_rs_0.3_new.txt').readlines()
# print(len(train_input_no_trai_22_new))

icews_yago_ent_1 = []
with open('icews_yago/new_ent_ids_1_rs_0.3_new') as f:
    for line in f.readlines():
        ent = line.split('\t')[1].strip()
        icews_yago_ent_1.append(ent)

icews_wiki_ent_1 = []
with open('icews_wiki/new_ent_ids_1_rs_0.3_new') as f:
    for line in f.readlines():
        ent = line.split('\t')[1].strip()
        icews_wiki_ent_1.append(ent)

for ent in icews_wiki_ent_1:
    if ent in icews_yago_ent_1:
        print(ent)



