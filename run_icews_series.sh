!bin/bash



echo "Icews series start"

echo "Icews yago"
python3 ReAct_API_call.py -d icews_yago -i code_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v19 -e 0
python3 ReAct_API_call.py -d icews_yago -i text_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v19 -e 0

python3 ReAct_API_call.py -d icews_yago -i code_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v19 -e 3
python3 ReAct_API_call.py -d icews_yago -i text_motif_base -l gpt_4_turbo -t 5000 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_50_5041_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v19 -e 3

echo "Icews wiki"
python3 ReAct_API_call.py -d icews_wiki -i code_motif_lite -l gpt_4_turbo -t 1500 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_wiki/candiadtes_semantic_embed_50_1496_all add_orginal_ranking.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v2 -e 3
python3 ReAct_API_call.py -d icews_wiki -i text_motif_lite -l gpt_4_turbo -t 1500 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_wiki/candiadtes_semantic_embed_50_1496_all add_orginal_ranking.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v2 -e 3


python3 ReAct_API_call.py -d icews_wiki -i code_motif_base -l gpt_4_turbo -t 1500 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_wiki/candiadtes_semantic_embed_50_1496_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v4 -e 4
python3 ReAct_API_call.py -d icews_wiki -i text_motif_base -l gpt_4_turbo -t 1500 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_wiki/candiadtes_semantic_embed_50_1496_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v4 -e 4

python3 ReAct_API_call.py -d icews_wiki -i text_motif_lite -l gpt_4_turbo -t 1500 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_wiki/candiadtes_semantic_embed_50_1496_all add_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v4 -e 3
