!bin/bash

# PLM
# echo "Start generating PLM input prompts"
# python3 ZeroEA_input_generate_undirected.py  ../data/DBP15K/zh_en/ text_input_no_train_11_wxt.txt text_input_no_train_22_wxt.txt 0 # you can change the data dir; input file dirs; WebSearch use flag as you like
# wait

#python3 machine_translation.py

echo "Start encoding and EA"
python3 LLMEA_zero_base.py ../data/DBP15K/zh_en/text_input_no_train_11_wxt.txt ../data/DBP15K/zh_en/text_input_no_train_22_wxt.txt '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_zh_en.json' > out_log/Output_LLMEA_zero_base_3000_cos_ed_csls_union_zh_en.txt # you can change the input file dirs as you like

#python3 LLMEA_base.py ../data/DBP15K/zh_en/text_input_no_train_11_wxt.txt ../data/DBP15K/zh_en/text_input_no_train_22_wxt.txt '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/run/llm_response/gpt4_turbo_zh_en.json' > out_log/Output_LLMEA_base_15000_cos_ed_csls_union_zh_en.txt # you can change the input file dirs as you like

#python3 LLMEA_base.py ../data/DBP15K/ja_en/text_input_no_train_11_wxt.txt ../data/DBP15K/ja_en/text_input_no_train_22_wxt.txt '/Users/jinyangli/Desktop/ZeroEA-main/run/llm_response/gpt4_turbo_ja_en.json' > out_log/Output_ZeroEA_base_ja_en.txt # you can change the input file dirs as you like

#python3 LLMEA_base.py ../data/DBP15K/fr_en/text_input_no_train_11_wxt.txt ../data/DBP15K/fr_en/text_input_no_train_22_wxt.txt '/Users/jinyangli/Desktop/ZeroEA-main/run/llm_response/gpt4_turbo_fr_en.json' > out_log/Output_ZeroEA_base_fr_en.txt # you can change the input file dirs as you like
