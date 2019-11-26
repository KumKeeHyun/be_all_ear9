#extract information using anly_node_que

from find_error import *
from ast import literal_eval

c_path = 'C:/Users/SmartSystemsSoftware/Desktop/text/correct.txt'
v_path = 'C:/Users/SmartSystemsSoftware/Desktop/text/voice.txt'

c_sentence_list, v_sentence_list = read_sentence_file(c_path, v_path)

for k in range(len(c_sentence_list)):
    c_word_list = split_sentence(c_sentence_list[k])
    v_word_list = split_sentence(v_sentence_list[k])

    statistics = open('C:/Users/SmartSystemsSoftware/Desktop/text/statistics.txt', 'r')
    error_cnt = statistics.readline()
    error_cnt = literal_eval(error_cnt)

    for i in range(len(c_word_list)):
        print('%s : %s =>' %(c_word_list[i], v_word_list[i]),end=' ')
        q1 = anlys_node(c_word_list[i],v_word_list[i])
        error_dict = q1.error_cnt
        
        for j in error_cnt:
            error_cnt[j] = error_cnt[j] + error_dict[j]
    data = error_cnt      
    statistics.close()
    statistics = open('C:/Users/SmartSystemsSoftware/Desktop/text/statistics.txt', 'w')
            

    statistics.write(str(data))
    statistics.close()


    

