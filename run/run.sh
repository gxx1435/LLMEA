!bin/bash

# PLM
# echo "Start generating PLM input prompts"
# python3 ZeroEA_input_generate_undirected.py  ../data/DBP15K/zh_en/ text_input_no_train_11_wxt.txt text_input_no_train_22_wxt.txt 0 # you can change the data dir; input file dirs; WebSearch use flag as you like
# wait

#python3 machine_translation.py
#echo "Test"
#python3 LLMEA_zero_base.py ../data/DBP15K/fr_en/text_input_no_train_11_wxt.txt ../data/DBP15K/fr_en/text_input_no_train_22_wxt.txt '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_.json' /mid_results_zeroembed_DBP15K_fr_en_sample_500/ 500 > out_log/Output_LLMEA_zero_base_sample500_DBP15K_fr_en_all_add.txt
#python3 LLMEA_zero_base.py ../data/DBP15K/ja_en/text_input_no_train_11_wxt_KI.txt ../data/DBP15K/ja_en/text_input_no_train_22_wxt_KI.txt '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_.json' /mid_results_zeroembed_DBP15K_ja_en_sample_500/ 500 > out_log/Output_LLMEA_zero_base_sample500_DBP15K_ja_en_all_add.txt
#python3 LLMEA_zero_base.py ../data/DBP15K/zh_en/text_input_no_train_11_wxt_KI.txt ../data/DBP15K/zh_en/text_input_no_train_22_wxt_KI.txt '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_.json' /mid_results_zeroembed_DBP15K_zh_en_sample_500/ 500 > out_log/Output_LLMEA_zero_base_sample500_DBP15K_zh_en_all_add.txt


echo "Start DBP15K"
python3 LLMEA_zero_base.py ../data/DBP15K/fr_en/text_input_no_train_11_wxt_rs_0.3_new.txt ../data/DBP15K/fr_en/text_input_no_train_22_wxt_rs_0.3_new.txt '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_.json' /mid_results_rs_0.3_zeroembed_DBP15K_fr_en/ 5000 > out_log/Output_LLMEA_zero_base_rs_30%_DBP15K_fr_en_all_add.txt
#python3 LLMEA_zero_base.py ../data/DBP15K/ja_en/text_input_no_train_11_wxt_rs_0.3_new.txt ../data/DBP15K/ja_en/text_input_no_train_22_wxt_rs_0.3_new.txt '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_.json' /mid_results_rs_0.3_zeroembed_DBP15K_ja_en/ 5000 > out_log/Output_LLMEA_zero_base_rs_30%_DBP15K_ja_en_all_add.txt
#python3 LLMEA_zero_base.py ../data/DBP15K/zh_en/text_input_no_train_11_wxt_rs_0.3_new.txt ../data/DBP15K/zh_en/text_input_no_train_22_wxt_rs_0.3_new.txt '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_.json' /mid_results_rs_0.3_zeroembed_DBP15K_zh_en/ 5000 > out_log/Output_LLMEA_zero_base_rs_30%_DBP15K_zh_en_all_add.txt

#python3 LLMEA_zero_base.py ../data/icews_yago/text_input_no_train_11_wxt_rs_0.3_new.txt ../data/icews_yago/text_input_no_train_22_wxt_rs_0.3_new.txt '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_.json' /mid_results_rs_0.3_zeroembed_icews_yago/ 30000 > out_log/Output_LLMEA_zero_base_rs_30%_icews_yago_all_add.txt
#python3 LLMEA_zero_base.py ../data/icews_wiki/text_input_no_train_11_wxt_rs_0.3_new.txt ../data/icews_wiki/text_input_no_train_22_wxt_rs_0.3_new.txt '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_.json' /mid_results_rs_0.3_zeroembed_icews_wiki/ 30000 > out_log/Output_LLMEA_zero_base_rs_30%_icews_wiki_all_add.txt

#python3 LLMEA_base_icews.py ../data/icews_yago/text_input_no_train_11_wxt_rs_0.3_new.txt ../data/icews_yago/text_input_no_train_22_wxt_rs_0.3_new.txt '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_.json' /mid_results_rs_0.3_icews_yago/ > out_log/Output_LLMEA_base_rs_30%_icews_yago_all_add.txt

#python3 LLMEA_zero_base_icews.py ../data/icews_yago/text_input_no_train_11_wxt_rs_0.3_new.txt ../data/icews_yago/text_input_no_train_22_wxt_rs_0.3_new.txt '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_.json' /mid_results_rs_0.3_zeroembed_icews_yago/ > out_log/Output_LLMEA_zero_base_random_sample_30%_icews_yago_all_add.txt

#python3 LLMEA_zero_base.py ../data/DBP15K/zh_en/text_input_no_train_11_wxt.txt ../data/DBP15K/zh_en/text_input_no_train_22_wxt.txt '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_zh_en.json' > out_log/Output_LLMEA_zero_base_3000_cos_ed_csls_union_zh_en.txt # you can change the input file dirs as you like

#python3 LLMEA_base.py ../data/DBP15K/zh_en/text_input_no_train_11_wxt.txt ../data/DBP15K/zh_en/text_input_no_train_22_wxt.txt '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_zh_en.json' > out_log/Output_LLMEA_base_15000_cos_ed_csls_union_zh_en.txt # you can change the input file dirs as you like

#python3 LLMEA_base.py ../data/DBP15K/ja_en/text_input_no_train_11_wxt.txt ../data/DBP15K/ja_en/text_input_no_train_22_wxt.txt '/Users/jinyangli/Desktop/ZeroEA-main/run/llm_response/gpt4_turbo_ja_en.json' > out_log/Output_ZeroEA_base_ja_en.txt # you can change the input file dirs as you like

#python3 LLMEA_base.py ../data/DBP15K/fr_en/text_input_no_train_11_wxt.txt ../data/DBP15K/fr_en/text_input_no_train_22_wxt.txt '/Users/jinyangli/Desktop/ZeroEA-main/run/llm_response/gpt4_turbo_fr_en.json' > out_log/Output_ZeroEA_base_fr_en.txt # you can change the input file dirs as you like
