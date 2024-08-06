!bin/bash


echo "Start recall API"

python3 ReAct_API_call.py -d icews_yago -i baseline -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_20_5041_all add_orginal_ranking.txt' -cn1 20 -cn2 20 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'

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
