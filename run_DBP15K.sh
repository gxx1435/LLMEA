!bin/bash

echo "DBP15K dataset start"
python3 ReAct_API_call.py -d DBP15K/zh_en -i code_motif_lite -l gpt_4_turbo -t 4500 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/candiadtes_semantic_embed_50_4500_cosine_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v0
#python3 ReAct_API_call.py -d DBP15K/ja_en -i code_motif_lite -l gpt_4_turbo -t 4500 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/ja_en/candiadtes_semantic_embed_50_4500_cosine_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new_ja' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v0
#python3 ReAct_API_call.py -d DBP15K/fr_en -i code_motif_lite -l gpt_4_turbo -t 4500 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/fr_en/candiadtes_semantic_embed_50_4500_cosine_put_correct_ans_last.txt' -cn1 50 -cn2 50 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new' -top_n 5 -v v0


