!bin/bash

echo "DBP15K dataset start"
#python3 ReAct_API_call.py -d DBP15K/zh_en -i code_motif_lite -l gpt_4_turbo -t 4500 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/candiadtes_semantic_embed_50_4267_cosine_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v0
#python3 ReAct_API_call.py -d DBP15K/ja_en -i code_motif_lite -l gpt_4_turbo -t 4500 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/ja_en/candiadtes_semantic_embed_50_4232_cosine_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v0
#python3 ReAct_API_call.py -d DBP15K/fr_en -i code_motif_lite -l gpt_4_turbo -t 4500 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/fr_en/candiadtes_semantic_embed_50_4467_cosine_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v0


echo "Icews series start"
#python3 ReAct_API_call.py -d icews_wiki -i code_motif_lite -l gpt_4_turbo -t 1500 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_wiki/candiadtes_semantic_embed_50_1496_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v3
#python3 ReAct_API_call.py -d icews_wiki -i text_motif_lite -l gpt_4_turbo -t 1500 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_wiki/candiadtes_semantic_embed_50_1496_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v0


#python3 ReAct_API_call.py -d icews_yago -i code_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_orginal_ranking.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v6 -e True
#python3 ReAct_API_call.py -d icews_yago -i code_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_orginal_ranking.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v6 -e True

#python3 ReAct_API_call.py -d icews_yago -i text_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v6
#python3 ReAct_API_call.py -d icews_yago -i text_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v6


#python3 ReAct_API_call.py -d icews_yago -i text_motif_lite -l llama3_70B -t 500 -s '/Users/jinyangli/Desktop/big_batches_API_call/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_orginal_ranking.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v4

#python3 ReAct_API_call.py -d icews_yago -i 1_neighbor -l gpt_4_turbo -t 500 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_orginal_ranking.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v5
#python3 ReAct_API_call.py -d icews_yago -i text_motif_lite -l gpt_4_turbo -t 500 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_orginal_ranking.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v5
#python3 ReAct_API_call.py -d icews_yago -i text_motif_base -l gpt_4_turbo -t 500 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_orginal_ranking.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v5

#python3 ReAct_API_call.py -d icews_yago -i code_motif_lite -l gpt_4_turbo -t 500 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_orginal_ranking.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v4
#python3 ReAct_API_call.py -d icews_yago -i code_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_orginal_ranking.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v5
#python3 ReAct_API_call.py -d icews_yago -i 1_neighbor -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_orginal_ranking.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v2


#python3 ReAct_API_call.py -d icews_yago -i code_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v4
#python3 ReAct_API_call.py -d icews_yago -i text_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v4

#python3 ReAct_API_call.py -d icews_yago -i code_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5

#python3 ReAct_API_call.py -d icews_yago -i text_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 7
#python3 ReAct_API_call.py -d icews_yago -i code_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 7

#python3 ReAct_API_call.py -d icews_yago -i text_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_20_5041_all add_orginal_ranking.txt' -cn1 20 -cn2 20 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#python3 ReAct_API_call.py -d icews_yago -i text_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_20_5041_all add_orginal_ranking.txt' -cn1 20 -cn2 20 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'

#python3 ReAct_API_call.py -d icews_yago -i text_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#python3 ReAct_API_call.py -d icews_yago -i text_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'

#python3 ReAct_API_call.py -d icews_yago -i code_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_20_5041_all add_orginal_ranking.txt' -cn1 20 -cn2 20 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#python3 ReAct_API_call.py -d icews_yago -i code_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_20_5041_all add_orginal_ranking.txt' -cn1 20 -cn2 20 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#
#
#python3 ReAct_API_call.py -d icews_yago -i code_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_20_5041_all add_put_correct_ans_last.txt' -cn1 20 -cn2 20 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#python3 ReAct_API_call.py -d icews_yago -i code_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_20_5041_all add_put_correct_ans_last.txt' -cn1 20 -cn2 20 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#
#
#python3 ReAct_API_call.py -d icews_yago -i code_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_10_5041_all add_orginal_ranking.txt' -cn1 10 -cn2 10 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#python3 ReAct_API_call.py -d icews_yago -i code_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_10_5041_all add_orginal_ranking.txt' -cn1 10 -cn2 10 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#
#
#python3 ReAct_API_call.py -d icews_yago -i code_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_10_5041_all add_put_correct_ans_last.txt' -cn1 10 -cn2 10 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#python3 ReAct_API_call.py -d icews_yago -i code_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_10_5041_all add_put_correct_ans_last.txt' -cn1 10 -cn2 10 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'

#python3 ReAct_API_call.py -d icews_yago -i code_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_orginal_ranking.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#python3 ReAct_API_call.py -d icews_yago -i code_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_orginal_ranking.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#
#python3 ReAct_API_call.py -d icews_yago -i code_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#python3 ReAct_API_call.py -d icews_yago -i code_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#
#
#python3 ReAct_API_call.py -d icews_yago -i code_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_70_5041_all add_orginal_ranking.txt' -cn1 70 -cn2 70 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#python3 ReAct_API_call.py -d icews_yago -i code_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_70_5041_all add_orginal_ranking.txt' -cn1 70 -cn2 70 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#
#python3 ReAct_API_call.py -d icews_yago -i code_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_70_5041_all add_put_correct_ans_last.txt' -cn1 70 -cn2 70 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#python3 ReAct_API_call.py -d icews_yago -i code_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_70_5041_all add_put_correct_ans_last.txt' -cn1 70 -cn2 70 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#
#python3 ReAct_API_call.py -d icews_yago -i code_motif_lite -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_100_5041_all add_orginal_ranking.txt' -cn1 100 -cn2 100 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
#python3 ReAct_API_call.py -d icews_yago -i code_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_100_5041_all add_orginal_ranking.txt' -cn1 100 -cn2 100 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
