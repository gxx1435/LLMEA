import subprocess, sys, os
import numpy as np
import pickle
from googletrans import Translator
from transformers import BertModel, BertTokenizer
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

from rouge_score import rouge_scorer
from deep_translator import GoogleTranslator
import json
from numpy import dot
from numpy.linalg import norm

def compute_csls(X_src, X_tgt, k=10):
    """
    Compute Cross-domain Similarity Local Scaling (CSLS).

    Parameters:
    X_src : np.array
        Source domain embeddings (n_samples_src, n_features)
    X_tgt : np.array
        Target domain embeddings (n_samples_tgt, n_features)
    k : int
        Number of nearest neighbors for local scaling

    Returns:
    csls_matrix : np.array
        CSLS similarity scores matrix (n_samples_src, n_samples_tgt)
    """
    # Compute cosine similarity matrix
    cosine_sim = np.dot(X_src, X_tgt.T)

    # Normalize vectors to have unit norm
    X_src_norm = np.linalg.norm(X_src, axis=1, keepdims=True)
    X_tgt_norm = np.linalg.norm(X_tgt, axis=1, keepdims=True)
    cosine_sim /= (X_src_norm @ X_tgt_norm.T)

    # Compute nearest neighbor similarity for source and target domains
    src_nn_sim = np.zeros(X_src.shape[0])
    tgt_nn_sim = np.zeros(X_tgt.shape[0])

    for i in range(X_src.shape[0]):
        src_nn_sim[i] = np.mean(np.sort(cosine_sim[i, :])[-k:])

    for j in range(X_tgt.shape[0]):
        tgt_nn_sim[j] = np.mean(np.sort(cosine_sim[:, j])[-k:])

    # Compute CSLS similarity scores
    csls_matrix = np.zeros(cosine_sim.shape)
    for i in range(X_src.shape[0]):
        for j in range(X_tgt.shape[0]):
            csls_matrix[i, j] = 2 * cosine_sim[i, j] - src_nn_sim[i] - tgt_nn_sim[j]

    return csls_matrix

def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))

def translate_text(text, src_lang, dest_lang):
    """
    :param text:
    :param src_lang:
    :param dest_lang:
    :return:
    """
    translator = GoogleTranslator(source=src_lang, target=dest_lang)
    translated = translator.translate(text)
    return translated

def translate_chinese_entity(entity):
    """
    :param entity:
    :return:
    """
    # Translate from Chinese to English
    english_translation = translate_text(entity, src_lang='zh-CN', dest_lang='en')
    print(english_translation)
    # Translate back from English to Chinese
    chinese_translation = translate_text(english_translation, src_lang='en', dest_lang='zh-CN')
    print(chinese_translation, '\n')

    return chinese_translation

def get_entity_embed(entity_text, tokenizer, model):
    """
    :param entity_text:
    :param tokenizer:
    :param model:
    :return:
    """
    input_txt_ent = "[MASK] is identical with " + entity_text + '. '

    tokens_ent = tokenizer(
        input_txt_ent,
        return_token_type_ids=False,
        return_attention_mask=True,
        return_tensors='pt')

    tokenized_ent_text = tokenizer.convert_ids_to_tokens(tokens_ent["input_ids"][0])

    encoded_layers_ent = model(input_ids=tokens_ent["input_ids"],
                               attention_mask=tokens_ent["attention_mask"])['last_hidden_state']

    last_hidden_state_ent = encoded_layers_ent[0]
    mask_idx = tokenized_ent_text.index("[MASK]")
    entity_embed = last_hidden_state_ent[mask_idx]

    return entity_embed.detach().numpy()

def calculate_entity_bert_embed_similarity(entity_list1, entity_list2):
    """
    :param entity_list1:
    :param entity_list2:
    :return:
    """
    bert_model = 'bert-base-chinese'
    tokenizer = BertTokenizer.from_pretrained(bert_model)
    model = BertModel.from_pretrained(bert_model, output_hidden_states=True)
    model.eval()

    entity_similarity = [0] * len(entity_list1)
    for i in range(len(entity_list1)):
        entity1 = entity_list1[i]
        entity2 = entity_list2[i]
        entity1_embed = get_entity_embed(entity1, tokenizer, model)
        entity2_embed = get_entity_embed(entity2, tokenizer, model)

        entity_similarity[i] = cosine_similarity(entity1_embed, entity2_embed)
        print(entity_similarity[i])

    return entity_similarity

def get_entity_need_retrans(cn_entity_dict, similarity):
    """
    :param cn_entity_dict:
    :param similarity:
    :return:
    """

    cn_entity_dict_need_retrans = {}
    for i, idx in enumerate(cn_entity_dict.keys()):
        # if i == 100: break
        if similarity[i] < 0.95:
            cn_entity_dict_need_retrans.update({idx: cn_entity_dict[str(idx)]})

    return cn_entity_dict_need_retrans

def main():

    try:
        import rouge_score
        import deep_translator
        import urllib3
    except ImportError:
        install('rouge_score')
        import rouge_score
        install('deep_translator')
        import deep_translator
        install('urllib3')
        import urllib3

    cn_entity_path = '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/ent_ids_1_cn'
    idx = []
    entities = []
    with open(cn_entity_path) as f:
        for line in f.readlines():
            line = line.split('\t')
            idx.append(line[0])
            entities.append(line[1].split('/')[-1].strip())

    try:
        with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/ent_ids_1_cn_original', 'r', encoding='utf-8') as file:
            cn_entity_dict = json.load(file)

        with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/ent_ids_1_cn_trans', 'r', encoding='utf-8') as file:
            # cn_translate_entity_dict = json.load(file)
            cn_translate_entity = file.readlines()

        # with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/ent_ids_1_cn_trans_similarity', 'rb') as file:
        #     entity_similarity = pickle.load(file)

    except:

        cn_entity_dict = dict(zip(idx, entities))
        with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/ent_ids_1_cn_original', 'w', encoding='utf-8') as file:
            json.dump(cn_entity_dict, file, ensure_ascii=False, indent=4)

        cn_translate_entity_dict = dict(zip(cn_entity_dict.keys(),
                                            [translate_chinese_entity(entity) if entity is not None else None for entity in cn_entity_dict.values()]))
        with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/ent_ids_1_cn_trans', 'w', encoding='utf-8') as file:
            json.dump(cn_translate_entity_dict, file, ensure_ascii=False, indent=4)

    similarity_path= '/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/ent_ids_1_cn_trans_similarity'

    if os.path.exists(similarity_path):
        with open(similarity_path, 'rb') as file:
            entity_similarity = pickle.load(file)
    else:
        entity_similarity = calculate_entity_bert_embed_similarity(list(cn_entity_dict.values()), list(cn_translate_entity))
        with open(similarity_path, 'wb') as file:
            pickle.dump(entity_similarity, file)

    print(entity_similarity)
    cn_entity_dict_need_retrans = get_entity_need_retrans(cn_entity_dict, entity_similarity)
    with open('/Users/gxx/Documents/2024/research/ZeroEA_for_Xiao/data/DBP15K/zh_en/ent_ids_1_cn_need_retrans', 'w',
              encoding='utf-8') as file:
        json.dump(cn_entity_dict_need_retrans, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':

    # entity = "巴不得妈妈"
    # translated_entity = translate_chinese_entity(entity)
    # print(f"原始实体: {entity}")
    # print(f"回译后的实体: {translated_entity}")

    main()




