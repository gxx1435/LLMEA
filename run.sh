!bin/bash


echo "Start recall API"
python3 ReAct_API_call_Nan.py -d icews_yago -i code_motif_lite -l gpt_4_turbo -t 5000 -r graph_motif_ReAct_v4_100_50candidates_tmp2 -s '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/icews_yago/candiadtes_semantic_embed_100_3765_all add_corrected.txt' -cn1 100 -cn2 40 -ent1 'new_ent_ids_1_rs_0.3_new' -ent2 'new_ent_ids_2_aligned_rs_0.3_new'
