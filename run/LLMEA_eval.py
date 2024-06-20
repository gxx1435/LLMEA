import sys
import json


def get_hits(llm_resp, ent_left, ent_right, top_k=(1, 10)):
    top_lr = [0] * len(top_k)
    for e_left, answer in llm_resp.items():
        find_idx = ent_left.index(e_left)
        assert e_left == ent_left[find_idx], "Wrong target entity!!!"
        if "</ANSWER>" in answer and "<ANSWER>" not in answer:
            cut_idx = answer.find("</ANSWER>")
            align_ent = answer[:cut_idx].replace("'", "")
            cut_idx_sort_1 = answer.find("<SORT>'")
            cut_idx_sort_2 = answer.find("'</SORT>")
            sort_list = answer[cut_idx_sort_1:cut_idx_sort_2].replace("<SORT>'", "").split("','")
    
            if align_ent == ent_right[find_idx] or sort_list[0] == ent_right[find_idx]:
                top_lr[0] += 1
            else:
                 print(ent_left[find_idx] + "  <---->  " + align_ent + "     |     " + ent_right[find_idx])
            if ent_right[find_idx] in sort_list[:10] or align_ent == ent_right[find_idx]:
                top_lr[1] += 1

    print('For each left:')
    for i in range(len(top_lr)):
        print('Hits@%d: %.2f%%' % (top_k[i], top_lr[i] / len(llm_resp) * 100))

if __name__ == '__main__':
    ent_left_path = sys.argv[1] 
    ent_right_path = sys.argv[2]   
    llm_resp_path = sys.argv[3] 
    
    with open(ent_right_path, 'r', encoding='utf8') as f:
            ent_right = json.load(f)

    with open(ent_left_path, 'r', encoding='utf8') as f:
            ent_left = json.load(f)

    with open(llm_resp_path, 'r', encoding='utf8') as f:
            llm_resp = json.load(f)
    
    get_hits(llm_resp, ent_left, ent_right)





