import json
from run.utils import hit_1_10_rate, baseline_hit_rate


if __name__ == '__main__':
    dataset = 'DBP15K/fr_en'
    save_dir = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/output/{}/gpt_4_turbo/t4500_50_50_corrected_5motif_v1'.format(dataset)
    if 'zh' in dataset:
        ent1_f = 'new_ent_ids_1_rs_0.3_new_cn'
    elif 'ja' in dataset:
        ent1_f = 'new_ent_ids_1_rs_0.3_new_ja'
    elif 'fr' in dataset:
        ent1_f = 'new_ent_ids_1_rs_0.3_new_fr'
    else:
        ent1_f = 'new_ent_ids_1_rs_0.3_new'

    ent2_f = 'new_ent_ids_2_aligned_rs_0.3_new'
    ## setting
    type = 'all'
    method = 'code'
    lite_or_base = 'lite'
    f_or_l = 'final_answer'


    if dataset == 'icews_wiki':
        length_all = 1496
    elif dataset == 'icews_yago':
        length_all = 4999
    elif 'DBP15K' in dataset:
        length_all = 4500

    with open(save_dir + '/{}_{}_motif_{}_1.json'.format(f_or_l,method, lite_or_base)) as f:
        final_answer_direct_match = json.load(f)
    length_recall_all = length_all - len(final_answer_direct_match)


    final_answers = {}
    if type == 'recall_all':
        for i in [2, 3, 4]:
            with open(save_dir + '/{}_{}_motif_{}_{}.json'.format(f_or_l, method,lite_or_base, i), 'r') as f:
                final_answer = json.load(f)
                final_answers.update(final_answer)
    elif type == 'all':
        for i in [1, 2, 3, 4]:
            with open(save_dir + '/{}_{}_motif_{}_{}.json'.format(f_or_l, method, lite_or_base, i), 'r') as f:
                final_answer = json.load(f)
                final_answers.update(final_answer)

    print(length_all, length_recall_all, len(final_answers))

    with open(save_dir+'/{}_{}_motif_{}_{}.json'.format(f_or_l,method, lite_or_base, type), 'w') as f:
        json.dump(final_answers, f, indent=4)

    # baseline_response = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/output/icews_yago_gpt_4_turbo_t5000_50_50_corrected/baseline/idx_prompt_dict_baseline_final_ans.json'
    # hit_rate = baseline_hit_rate(baseline_response,dataset, ent1_f, ent2_f, 'hit1')

    if type == 'all':
        length = length_all
    elif type == 'recall_all':
        length = length_recall_all

    hit_rate = hit_1_10_rate(save_dir+'/{}_{}_motif_{}_{}.json'.format(f_or_l, method, lite_or_base, type),
                             dataset=dataset,
                             ent1_f=ent1_f,
                             ent2_f=ent2_f,
                             hit='hit1',
                             length=length)
    print(hit_rate)

    # from run.utils import mean_reciprocal_rank
    # mrr = mean_reciprocal_rank(final_answers)
    # print(mrr)