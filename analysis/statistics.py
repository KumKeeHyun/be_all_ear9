#extract information using anly_node_que

from find_error import *

c_word, v_word = read_sentence_file('C:/Users/SmartSystemsSoftware/Desktop/text/correct.txt', 'C:/Users/SmartSystemsSoftware/Desktop/text/voice.txt')


c_word_list = split_sentence(c_word)
v_word_list = split_sentence(v_word)

for i in range(len(c_word_list)):
    print('%s : %s =>' %(c_word_list[i], v_word_list[i]),end=' ')
    q1 = anlys_node(c_word_list[i],v_word_list[i])
