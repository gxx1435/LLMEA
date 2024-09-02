import random
import string
from zhon.hanzi import punctuation
from urllib.parse import unquote
from run.utils import  get_id_entity_dict
from run.utils import clear_entity_text

def preprocess_ent_ids():
    """
    :return:
    """
    idx_ent_dict = {}
    with open(ent_ids_1, 'r') as f:
        for line in f.readlines():
            idx = line.split('\t')[0]
            ent = line.split('\t')[1].replace('\n', '').split('(')[0].replace('_', ' ')
            idx_ent_dict.update({idx: ent})

    with open(ent_ids_1+'_strip', 'w') as f:
        for idx in idx_ent_dict.keys():
            f.write(idx +'\t' + idx_ent_dict[idx] +'\n')

    idxs = []
    ents = []
    with open(ent_ids_2_aligned, 'r') as f:
        for line in f.readlines():
            idx = line.split('\t')[0]
            ent = line.split('\t')[1].replace('\n', '').split('(')[0].replace('_', ' ')
            idxs.append(idx)
            ents.append(ent)

    with open(ent_ids_2_aligned + '_strip', 'w') as f:
        for i, idx in enumerate(idxs):
            f.write(idx + '\t' + ents[i] + '\n')

def random_sample_data(percentage=0.3, seed=7):
    """
    :return:
    """
    ids_1 = []
    ent_ids_1_dict = {}
    with open(ent_ids_1, 'r') as f:
        for line in f.readlines():
            line = unquote(line).replace('\n', '')
            idx = line.split('\t')[0]
            entity = line.split('\t')[1]
            ids_1.append(idx)
            ent_ids_1_dict.update({idx: entity})

    ids_2 = []
    ent_ids_2_dict = {}
    with open(ent_ids_2_aligned, 'r') as f:
        for line in f.readlines():
            line = unquote(line).replace('\n', '')
            idx = line.split('\t')[0]
            entity = line.split('\t')[1]
            ids_2.append(idx)
            ent_ids_2_dict.update({idx: entity})

    print(len(ids_1), len(ids_2))

    random.seed(seed)

    sample_size = int(percentage * len(ids_1))
    indices = list(range(len(ids_1)))
    random_indices = random.sample(indices, sample_size)

    ids_1_random_samples = [ids_1[i] for i in random_indices]
    ids_2_random_samples = [ids_2[i] for i in random_indices]

    with open(ent_ids_1 + '_rs_{}'.format(percentage), 'w') as f:
        for idx in ids_1_random_samples:
            f.write(str(idx) +'\t'+ent_ids_1_dict[str(idx)]+'\n')

    with open(ent_ids_2_aligned + '_rs_{}'.format(percentage), 'w') as f:
        for idx in ids_2_random_samples:
            f.write(str(idx) +'\t'+ent_ids_2_dict[str(idx)]+'\n')

def get_text_input_no_train_11_22_wxt_random_sample_by_id(rs='rs_0.3'):
    ent_ids_1_rs_dict = {}
    with open(dataset+"/new_ent_ids_1_{}".format(rs), 'r') as f:
        for line in f.readlines():
            line = unquote(line)
            tmp = line.replace('\n', "")
            tmp = tmp.replace('_', ' ')
            tmp = tmp.replace("  ", " ")
            tmp = tmp.replace(" .", ".")
            tmp = tmp.replace(" )", ")")

            idx = tmp.split('\t')[0]
            ent = tmp.split('\t')[1].strip()
            ## The same with text prompt
            ent_txt = ent.strip().replace("...", "")
            ent_txt = ent_txt.split('(')[0].strip()
            ent_txt = ent_txt.split('（')[0].strip()

            # remove punctuation
            punctuation_eng = string.punctuation
            punctuation_zh = punctuation
            for i in punctuation_eng:
                ent_txt = ent_txt.replace(i, '')

            for j in punctuation_zh:
                ent_txt = ent_txt.replace(j, '')
            #
            ent_txt = ent_txt.replace('_', ' ')

            ent_ids_1_rs_dict.update({idx: ent_txt})

    ids_1 = []
    with open(dataset+"/new_ent_ids_1_{}_new".format(rs), 'w') as f:
        for key in ent_ids_1_rs_dict.keys():
            ids_1.append(key)
            ent = ent_ids_1_rs_dict[key]
            ent_txt = clear_entity_text(ent)
            f.write(key+'\t'+ent_txt+'\n')

    if 'zh' in dataset:
        ids_ent_1_cn_dict = get_id_entity_dict(
            '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/ent_ids_1_cn')
        with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1_{}_new_cn'.format(dataset, rs),
                  'w') as f:
            for id in ids_1:
                f.write(id + '\t' + ids_ent_1_cn_dict[id] + '\n')
    elif 'ja' in dataset:
        ids_ent_1_ja_dict = get_id_entity_dict(
            '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/ja_en/ent_ids_1_ja')
        with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1_{}_new_ja'.format(dataset, rs),
                  'w') as f:
            for id in ids_1:
                f.write(id + '\t' + ids_ent_1_ja_dict[id] + '\n')
    elif 'fr' in dataset:
        ids_ent_1_fr_dict = get_id_entity_dict(
            '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/fr_en/ent_ids_1_fr')
        with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1_{}_new_fr'.format(dataset, rs),
                  'w') as f:
            for id in ids_1:
                f.write(id + '\t' + ids_ent_1_fr_dict[id] + '\n')

    ent_ids_2_rs_dict = []
    with open(dataset+"/new_ent_ids_2_aligned_{}".format(rs), 'r') as f:
        for line in f.readlines():
            line = unquote(line)
            tmp = line.replace('\n', "")
            tmp = tmp.replace('_', ' ')
            tmp = tmp.replace("  ", " ")
            tmp = tmp.replace(" .", ".")
            tmp = tmp.replace(" )", ")")

            idx = tmp.split('\t')[0]
            ent = tmp.split('\t')[1].strip()

            ## The same with text prompt
            ent_txt = ent.strip().replace("...", "")
            ent_txt = ent_txt.split('(')[0].strip()
            ent_txt = ent_txt.split('（')[0].strip()

            # remove punctuation
            punctuation_eng = string.punctuation
            punctuation_zh = punctuation
            for i in punctuation_eng:
                ent_txt = ent_txt.replace(i, '')

            for j in punctuation_zh:
                ent_txt = ent_txt.replace(j, '')
            #
            ent_txt = ent_txt.replace('_', ' ')

            ent_ids_2_rs_dict.append((idx, ent_txt))

    with open(dataset+"/new_ent_ids_2_aligned_{}_new".format(rs), 'w') as f:
        for item in ent_ids_2_rs_dict:
            ent = item[1]
            ent_txt = clear_entity_text(ent)
            f.write(item[0] + '\t' + ent_txt  + '\n')

    print(len(ent_ids_1_rs_dict.keys()), len(ent_ids_2_rs_dict))

    id_1_desciption = {}
    with open(dataset+'/text_input_no_train_11_wxt_id.txt', 'r') as f:
        for line in f.readlines():
            line = unquote(line)
            line = line.split(':')
            id_1_desciption.update({line[0]: line[1].strip()})


    with open(dataset+'/text_input_no_train_11_wxt_{}_new.txt'.format(rs), 'w') as f:
        for key in ent_ids_1_rs_dict.keys():
            f.write(ent_ids_1_rs_dict[key]+':'+id_1_desciption[key]+'\n')


    id_2_desciption = {}
    with open(dataset + '/text_input_no_train_22_wxt_id.txt', 'r') as f:
        for line in f.readlines():
            line = unquote(line)
            line = line.split(':')
            id_2_desciption.update({line[0]: line[1].strip()})


    with open(dataset + '/text_input_no_train_22_wxt_{}_new.txt'.format(rs), 'w') as f:
        for item in ent_ids_2_rs_dict:
            f.write(item[1] + ':' + id_2_desciption[item[0]]+'\n')



def get_text_input_no_train_11_22_wxt_random_sample_by_text(rs='rs_0.3'):
    """
    Abandoned, too complex and remove the entity with complex punctuations
    :param rs:
    :return:
    """

    def text_input_no_train_11_22_wxt_random_sample1(rs='rs_0.3'):
        """

        :param rs:
        :return:
        """
        ent_ids_1_dict = {}
        with open(dataset+"/new_ent_ids_1_{}".format(rs), 'r') as f:
            for line in f.readlines():
                idx = line.split('\t')[0]
                ent = line.split('\t')[1].replace('\n', '')
                ent_ids_1_dict.update({ent: idx})

        ent_ids_2_dict = {}
        with open(dataset+"/new_ent_ids_2_aligned_{}".format(rs), 'r') as f:
            for line in f.readlines():
                idx = line.split('\t')[0]
                ent = line.split('\t')[1].replace('\n', '')
                ent_ids_2_dict.update({ent: idx})

        ent_descrip_dict = {}
        with open(dataset+'/text_input_no_train_11_wxt.txt', 'r') as f:
            for i, line in enumerate(f.readlines()):
                ent = line.split(":")[0]
                descrip = line.split(":")[1].replace('\n', '')
                ent_descrip_dict.update({ent: descrip})

        print(len(ent_ids_1_dict), len(ent_ids_2_dict))

        new_ent_descrip_dict = {}
        for ent in ent_ids_1_dict.keys():
            if ent not in ent_descrip_dict.keys():
                print(ent)
            if ent in ent_descrip_dict.keys():
                new_ent_descrip_dict.update({ent: ent_descrip_dict[ent]})
        print('new_ent_descrip_dict: ', len(new_ent_descrip_dict))

        with open(dataset+'/text_input_no_train_11_wxt_{}.txt'.format(rs), 'w') as f:
            for ent in new_ent_descrip_dict.keys():
                f.write(ent+":"+new_ent_descrip_dict[ent]+'\n')

        #-----------------------------------------------------------------------


        ent_descrip_dict = {}
        new_ent_descrip_dict = {}
        with open(dataset+'/text_input_no_train_22_wxt.txt', 'r') as f:
            for line in f.readlines():
                ent = line.split(":")[0]
                descrip = line.split(":")[1].replace('\n', '')
                ent_descrip_dict.update({ent: descrip})

        for ent in ent_ids_2_dict.keys():
            if ent in ent_descrip_dict.keys():
                new_ent_descrip_dict.update({ent: ent_descrip_dict[ent]})

        print('new_ent_descrip_dict: ', len(new_ent_descrip_dict))

        with open(dataset+'/text_input_no_train_22_wxt_{}.txt'.format(rs), 'w') as f:
            for ent in new_ent_descrip_dict.keys():
                f.write(ent + ":" + new_ent_descrip_dict[ent] + '\n')


    def text_input_no_train_11_22_wxt_random_sample2(rs = 'rs_0.3'):
        """
        :param rs:
        :return:
        """
        ents_1 = []
        with open(dataset+"/new_ent_ids_1_{}".format(rs), 'r') as f:
            for line in f.readlines():
                idx = line.split('\t')[0]
                ent = line.split('\t')[1].replace('\n', '')
                ents_1.append(ent)

        ents_2 = []
        with open(dataset+"/new_ent_ids_2_aligned_{}".format(rs), 'r') as f:
            for line in f.readlines():
                idx = line.split('\t')[0]
                ent = line.split('\t')[1].replace('\n', '')
                ents_2.append(ent)

        ents_12_dict = dict(zip(ents_1, ents_2))

        train_11_ents = []
        train_11_description = {}
        with open(dataset+'/text_input_no_train_11_wxt_{}.txt'.format(rs)) as f:
            for line in f.readlines():
                ent  = line.split(":")[0]
                description = line.split(":")[1]
                train_11_ents.append(ent)
                train_11_description.update({ent: description})


        train_22_ents = []
        train_22_description = {}
        with open(dataset+'/text_input_no_train_22_wxt_{}.txt'.format(rs)) as f:
            for line in f.readlines():
                ent = line.split(":")[0]
                description = line.split(":")[1]
                train_22_ents.append(ent)
                train_22_description.update({ent: description})

        ent1_list = []
        ent2_list = []
        for ent in train_11_ents:
            if ents_12_dict[ent] in train_22_ents:
                ent1_list.append(ent)
                ent2_list.append(ents_12_dict[ent])

        with open(dataset+'/text_input_no_train_11_wxt_{}_new.txt'.format(rs), 'w') as f:
            for ent in ent1_list:
                f.write(ent+":"+train_11_description[ent])

        with open(dataset+'/text_input_no_train_22_wxt_{}_new.txt'.format(rs), 'w') as f:
            for ent in ent2_list:
                f.write(ent+":"+train_22_description[ent])

    def get_ent_ids_12(rs='rs_0.3'):
        """
        根据zeroEA的prompt问件生成对应的ent_ids_1和ent_ids_2
        :return:
        """
        ent_ids_1_dict = {}
        with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1_{}'.format(dataset, rs)) as f:
            for line in f.readlines():
                idx = line.split("\t")[0]
                ent = line.split('\t')[1].replace('\n', '')
                ent_ids_1_dict.update({ent: idx})

        ent_ids_2_dict = {}
        with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_2_aligned_{}'.format(dataset, rs)) as f:
            for line in f.readlines():
                idx = line.split("\t")[0]
                ent = line.split('\t')[1].replace('\n', '')
                ent_ids_2_dict.update({ent: idx})

        ents_1 = []
        with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/text_input_no_train_11_wxt_{}_new.txt'.format(dataset,rs)) as f:
            for line in f.readlines():
                ent = line.split(':')[0]
                ents_1.append(ent)

        ents_2 = []
        with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/text_input_no_train_22_wxt_{}_new.txt'.format(dataset, rs)) as f:
            for line in f.readlines():
                ent = line.split(':')[0]
                ents_2.append(ent)

        ids_1 = []
        with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1_{}_new'.format(dataset, rs), 'w') as f:
            for ent in ents_1:
                if 'DBP15K' in dataset:
                    ent_txt = ent.strip().replace("...", "")
                    ent_txt = ent_txt.split('(')[0].strip()
                    ent_txt = ent_txt.split('（')[0].strip()

                    # remove punctuation
                    punctuation_eng = string.punctuation
                    punctuation_zh = punctuation
                    for i in punctuation_eng:
                        ent_txt = ent_txt.replace(i, '')

                    for j in punctuation_zh:
                        ent_txt = ent_txt.replace(j, '')
                    #
                    ent_txt = ent_txt.replace('_', ' ')
                    ids_1.append(ent_ids_1_dict[ent])
                f.write(ent_ids_1_dict[ent] + '\t' + ent_txt + '\n')

        if 'zh' in dataset:
            ids_ent_1_cn_dict = get_id_entity_dict('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/ent_ids_1_cn')
            with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1_{}_new_cn'.format(dataset, rs), 'w') as f:
                for id in ids_1:
                    f.write(id+'\t'+ids_ent_1_cn_dict[id]+'\n')
        elif 'ja' in dataset:
            ids_ent_1_ja_dict = get_id_entity_dict('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/ja_en/ent_ids_1_ja')
            with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1_{}_new_ja'.format(dataset, rs), 'w') as f:
                for id in ids_1:
                    f.write(id+'\t'+ids_ent_1_ja_dict[id]+'\n')
        elif 'fr' in dataset:
            ids_ent_1_fr_dict = get_id_entity_dict('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/fr_en/ent_ids_1_fr')
            with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1_{}_new_fr'.format(dataset, rs), 'w') as f:
                for id in ids_1:
                    f.write(id+'\t'+ids_ent_1_fr_dict[id]+'\n')

        with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_2_aligned_{}_new'.format(dataset, rs), 'w') as f:
            for ent in ents_2:
                if 'DBP15K' in dataset:
                    ent_txt = ent.strip().replace("...", "")
                    ent_txt = ent_txt.split('(')[0].strip()
                    ent_txt = ent_txt.split('（')[0].strip()

                    # remove punctuation
                    punctuation_eng = string.punctuation
                    punctuation_zh = punctuation
                    for i in punctuation_eng:
                        ent_txt = ent_txt.replace(i, '')

                    for j in punctuation_zh:
                        ent_txt = ent_txt.replace(j, '')
                    #
                    ent_txt = ent_txt.replace('_', ' ')
                f.write(ent_ids_2_dict[ent]+'\t'+ent_txt+'\n')

    text_input_no_train_11_22_wxt_random_sample1()
    text_input_no_train_11_22_wxt_random_sample2()
    get_ent_ids_12()


if __name__ == '__main__':

    dataset = 'DBP15K/ja_en'
    # dataset = 'icews_yago'
    # dataset = 'icews_wiki'

    ent_ids_1 = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_1'.format(dataset)
    ent_ids_2_aligned = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/{}/new_ent_ids_2_aligned'.format(dataset)

    # preprocess_ent_ids()
    random_sample_data()
    get_text_input_no_train_11_22_wxt_random_sample_by_id()
    # get_text_input_no_train_11_22_wxt_random_sample_by_text()





    exit()