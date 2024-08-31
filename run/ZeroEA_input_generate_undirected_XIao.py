#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np 
import re
import sys
from transformers import BertTokenizer
from tqdm import tqdm
import time

def text_save(filename, data):
    file = open(filename, 'w')
    for i in range(len(data)):
        s = str(data[i])#.replace('[','').replace(']','')
        s = s + "\n"
        file.write(s)
    file.close()


def entity2text(text_id_l, entity_id, ent_l_text, ent_ids, rel_ids, nodes, graph_id, trans_flg):
    text_all = []
    error_flg = False
    print('len text_id_l: ', len(text_id_l))
    if len(text_id_l) > 3000:
        text_id_l = text_id_l[:3000]

    for char_set in text_id_l:
        # print(char_set)
        triple_flg = char_set[1]
        char = char_set[0]
        content = char.split("\t")
        head_text = ent_l_text.replace("_", " ")
        rel_text = rel_ids[content[0]]
        tail_text = ent_ids[content[1]].replace("_", " ")
        # print(head_text, rel_text, tail_text, '\n')

        word_list = re.findall('[a-zA-Z][^A-Z]*', rel_text)
        if word_list:
            rel_text_en = word_list[0]

            for i in range(len(word_list)):
                if i == 0:
                    continue
                if rel_text_en[-1] == "_" or word_list[i][0] == '-':
                    rel_text_en = rel_text_en + word_list[i]
                else:
                    rel_text_en = rel_text_en + ' ' + word_list[i]

        else:
            try:
                rel_text_en = rel_text
            except:
                print("relation error: ", rel_text)
                error_flg = True
                return None, None, error_flg

        head_text_en = head_text
        tail_text_en = tail_text
        
        if triple_flg == 1:
            text_to_add = head_text_en + " is the " + rel_text_en + " of " + tail_text_en
        else:
            text_to_add = tail_text_en + " is the " + rel_text_en + " of " + head_text_en
#         text_2hop,_,_ = entity2text_2hop(content[1], ent_ids, rel_ids, False)
        text_all.append(text_to_add)
#         text_all.extend(text_2hop)
#         print(text_all)
        
    return text_all, head_text_en, error_flg 


def text_tokenizer(text_all):
    bert_name = 'bert-base-uncased'
    tokenizer = BertTokenizer.from_pretrained(bert_name)
    tokens = tokenizer.tokenize(text_all)
    input_ids = tokenizer.convert_tokens_to_ids(tokens)

    return tokens, input_ids

# paras:
data_dir = sys.argv[1]
fn_save_1 = sys.argv[2]
fn_save_2 = sys.argv[3]
fn_id_save_1 = fn_save_1.replace('.','_id.')
fn_id_save_2 = fn_save_2.replace('.','_id.')
KI_flg = int(sys.argv[4])
Idtxt_flg = sys.argv[5]

ent_ids = {}
ent_ids_cn = {}
rel_ids = {}
random_sample = 0.3

# with open(data_dir+"new_ent_ids_1_random_sample_{}".format(random_sample), "r") as ent_1:
with open(data_dir + "ent_ids_1", "r") as ent_1:
    print('ent_ids_1')
    for line in tqdm(ent_1):
        tmp = line.strip()
        tmp = tmp.replace('\n',"")
        tmp = tmp.replace('_', ' ')
        tmp = tmp.replace("  ", " ")
        content = tmp.split("\t")
        if len(content[0])>5:
            assert False
        text = content[1].split("/")[-1]
        ent_ids[content[0]] = text.replace('/', ' ')     
        
# with open(data_dir+"new_ent_ids_2_aligned_random_sample_{}".format(random_sample), "r") as ent_2:
with open(data_dir + "ent_ids_2", "r") as ent_2:

    print('ent_ids_2')
    for line in tqdm(ent_2):
        tmp = line.strip()
        tmp = tmp.replace('\n',"")
        tmp = tmp.replace('_', ' ')
        tmp = tmp.replace("  ", " ")
        content = tmp.split("\t")
        text = content[1].split("/")[-1]
        ent_ids[content[0]] = text.replace('/', ' ')

with open(data_dir+"rel_ids_1", "r") as rel_1:
    print('rel_ids_1')
    for line in tqdm(rel_1):
        tmp = line.strip()
        tmp = tmp.replace('\n',"")
        tmp = tmp.replace('_', ' ')
        tmp = tmp.replace("  ", " ")
        content = tmp.split("\t")
        if len(content[0])>5:
            assert False
        text = content[1].split("/")[-1]
        rel_ids[content[0]] = text

with open(data_dir+"rel_ids_2", "r") as rel_2:
    print('rel_ids_2')
    for line in tqdm(rel_2):
        tmp = line.strip()
        tmp = tmp.replace('\n',"")
        content = tmp.split("\t")
        text = content[1].split("/")[-1]
        rel_ids[content[0]] = text

nodes = {}
with open(data_dir+"triples_1", "r") as G1:
    print('G1')
    for line in tqdm(G1):
        tmp = line.strip()
        tmp = tmp.replace('\n',"")
        content = tmp.split("\t")
        if content[0] in nodes.keys():
            nodes[content[0]].append((content[1]+"\t"+content[2],0))
        else:
            nodes[content[0]] = [(content[1]+"\t"+content[2],0)]
            
        if content[2] in nodes.keys():
            nodes[content[2]].append((content[1]+"\t"+content[0],1))
        else:
            nodes[content[2]] = [(content[1]+"\t"+content[0],1)]

with open(data_dir+"triples_2", "r") as G2:
    print('G2')
    for line in tqdm(G2):
        tmp = line.strip()
        tmp = tmp.replace('\n',"")
        content = tmp.split("\t")
        if content[0] in nodes.keys():
            nodes[content[0]].append((content[1]+"\t"+content[2],0))
        else:
            nodes[content[0]] = [(content[1]+"\t"+content[2],0)]

        if content[2] in nodes.keys():
            nodes[content[2]].append((content[1]+"\t"+content[0],1))
        else:
            nodes[content[2]] = [(content[1]+"\t"+content[0],1)]


### entity correction:
if KI_flg:
    with open(data_dir+"entity_correction.txt", "r") as ent_correction:
        for line in ent_correction:
            tmp = line.strip()
            tmp = tmp.replace('\n',"")
            numb = tmp.split("\t")[0].strip()
            content = tmp.split("\t")[-1].strip()
            ent_ids[numb] = content
                
            
tokens_len_all = []
tokens_all = []
input_id_len_all = []
input_ids_all = []
text_input_all_1 = []
text_input_all_2 = []
wiki_correction_dict = {}

# with open(data_dir+"ill_ent_ids_new", "r") as GT_file:
with open(data_dir+"new_ref_ent_ids", "r") as GT_file:
    print('Gold Truth pairs')
    counter = 0
    for line in tqdm(GT_file.readlines()):
        try:
            counter += 1
            tmp = line.strip()
            tmp = tmp.replace('\n',"")
            content = tmp.split("\t")
            print(content[0], content[1])
            id_l = content[0]
            id_r = content[1]
            text_id_l = nodes[content[0]]
            ent_l_text = ent_ids[content[0]]
            text_id_r = nodes[content[1]]
            ent_r_text = ent_ids[content[1]]


            text_to_add_l, head_text_en_l, error_flg_l = entity2text(text_id_l, content[0], ent_l_text, ent_ids, rel_ids, nodes, "G1: ", False)

            text_to_add_r, head_text_en_r, error_flg_r = entity2text(text_id_r, content[1], ent_r_text, ent_ids, rel_ids, nodes, "G2: ", False)


            if error_flg_l:
                continue

            if Idtxt_flg == 'id':
                text_input_1 = id_l + ": "
                text_input_2 = id_r + ": "
            elif Idtxt_flg == 'text':
                text_input_1 = ent_l_text + ": "
                text_input_2 = ent_r_text + ": "

            for text in text_to_add_l:
                text_input_1 = text_input_1 + text + ". "
            for text in text_to_add_r:
                text_input_2 = text_input_2 + text + ". "

            text_input_1 = text_input_1.replace("  ", " ")
            text_input_1 = text_input_1.replace(" .", ".")
            text_input_1 = text_input_1.replace(" )", ")")
            text_input_2 = text_input_2.replace("  ", " ")
            text_input_2 = text_input_2.replace(" .", ".")
            text_input_2 = text_input_2.replace(" )", ")")
            text_input_1 = text_input_1.strip()
            text_input_2 = text_input_2.strip()
            text_input_all_1.append(text_input_1)
            text_input_all_2.append(text_input_2)

            # print(text_input_all_1)
            # print(text_input_all_2)

            if counter % 20 == 0:
                if Idtxt_flg == 'id':

                    text_save(data_dir + fn_id_save_1, text_input_all_1)
                    text_save(data_dir + fn_id_save_2, text_input_all_2)

                elif Idtxt_flg =='text':

                    text_save(data_dir+fn_save_1, text_input_all_1)
                    text_save(data_dir+fn_save_2, text_input_all_2)

        except Exception as e:
            print(e)

            # print(ent_l_text, '\t', ent_r_text)
            # print(head_text_en_l, '\t', head_text_en_r)
            # print(text_input_1)
            # print(text_input_2)

            if Idtxt_flg == 'id':
                text_input_1 = id_l + ':' + 'The node not in graph.'
                text_input_2 = id_r + ':' + 'The node not in graph.'
            elif Idtxt_flg == 'text':
                text_input_1 = ent_l_text + ':' +'The node not in graph.'
                text_input_2 = ent_r_text + ':' +'The node not in graph.'

            text_input_all_1.append(text_input_1)
            text_input_all_2.append(text_input_2)

if Idtxt_flg == 'id':
    text_save(data_dir + fn_id_save_1, text_input_all_1)
    text_save(data_dir + fn_id_save_2, text_input_all_2)
elif Idtxt_flg == 'text':
    text_save(data_dir + fn_save_1, text_input_all_1)
    text_save(data_dir + fn_save_2, text_input_all_2)





        