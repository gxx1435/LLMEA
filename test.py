import json

import numpy as np
import scipy


# def get_hits(Lvec, Rvec, top_k=(1, 10, 50, 100)):
#
#     # Lvec = np.array([vec[e1] for e1, e2 in test_pair])
#     # Rvec = np.array([vec[e2] for e1, e2 in test_pair])
#
#     sim = scipy.spatial.distance.cdist(Lvec, Rvec, metric='cityblock')
#     top_lr = [0] * len(top_k)
#     for i in range(Lvec.shape[0]):
#         rank = sim[i, :].argsort()
#         rank_index = np.where(rank == i)[0][0]
#         for j in range(len(top_k)):
#             if rank_index < top_k[j]:
#                 top_lr[j] += 1
#     top_rl = [0] * len(top_k)
#     for i in range(Rvec.shape[0]):
#         rank = sim[:, i].argsort()
#         rank_index = np.where(rank == i)[0][0]
#         for j in range(len(top_k)):
#             if rank_index < top_k[j]:
#                 top_rl[j] += 1
#     print('For each left:')
#     for i in range(len(top_lr)):
#         print('Hits@%d: %.2f%%' % (top_k[i], top_lr[i] / len(Lvec) * 100))
#     print('For each right:')
#     for i in range(len(top_rl)):
#         print('Hits@%d: %.2f%%' % (top_k[i], top_rl[i] / len(Lvec) * 100))

# import os, json
# with open(os.getcwd() + '/output/expel_v4/expel_code_prompts_rules_v4.txt') as f:
#     code_generated_rules = f.read().split('\n\n')
#     for i in range(1, len(code_generated_rules)):
#         if code_generated_rules[-i] != '-1\n':
#             rule = code_generated_rules[-i]
#             break
# print(rule)

with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/output/DBP15K/ja_en/gpt_4_turbo/t4500_50_50_corrected_5motif_v0/final_answer_code_motif_lite_1.json') as f:
    dict = json.load(f)
    for key in dict.keys():
        print(key, dict[key])