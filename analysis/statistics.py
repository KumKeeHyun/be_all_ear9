#extract information using anly_node_que

from find_error import *
from ast import literal_eval

error_match = {'&' : 'th',
			   '^' : 'ck',
			   '#' : 'ph',
			   '0' : 'oo',
			   '9' : 'aw',
			   '8' : 'ou',
			   '7' : 'oa',
			   '6' : 'ir',
			   '5' : 'ur',
			   '4' : 'or',
			   '3' : 'ar',
			   '2' : 'er',
			   '1' : 'ow'}

c_path = './c_output.txt'
v_path = '../speech_to_text/flac_set/output/output.txt'
statistics_path = './statistics.txt'

def input_c_txt():
	cd = open(c_path, 'w')
	vd = open(v_path, 'r')

	while True:
		voice_line = vd.readline()
		if not voice_line:
			break;
		print('v_sentence :', voice_line, end='')
		correct_line = input('enter sentence :')
		cd.write(correct_line + '\n')

input_c_txt()

print('\nanlaysis..')
c_sentence_list, v_sentence_list = read_sentence_file(c_path, v_path)

for k in range(len(c_sentence_list)):
    c_word_list = split_sentence(c_sentence_list[k])
    v_word_list = split_sentence(v_sentence_list[k])

    statistics = open(statistics_path, 'r')
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
    statistics = open(statistics_path, 'w')
    
    statistics.write(str(data))
    statistics.close()


    
statistics = open(statistics_path, 'r')
error_cnt = statistics.readline()
error_dict = literal_eval(error_cnt)
statistics.close()
statistics = open(statistics_path, 'w')


error_dict['th']=error_dict['&']
del error_dict['&']
error_dict['ck']=error_dict['^']
del error_dict['^']
error_dict['ph']=error_dict['#']
del error_dict['#']
error_dict['oo']=error_dict['0']
del error_dict['0']
error_dict['aw']=error_dict['9']
del error_dict['9']
error_dict['ou']=error_dict['8']
del error_dict['8']
error_dict['oa']=error_dict['7']
del error_dict['7']
error_dict['ir']=error_dict['6']
del error_dict['6']
error_dict['ur']=error_dict['5']
del error_dict['5']
error_dict['or']=error_dict['4']
del error_dict['4']
error_dict['ar']=error_dict['3']
del error_dict['3']
error_dict['er']=error_dict['2']
del error_dict['2']
error_dict['ow']=error_dict['1']
del error_dict['1']

value_sum = 0
for error in error_dict:
	value_sum += error_dict[error]

sorted(error_dict.items(), key=lambda x: x[1], reverse = True)

print('\n-----stat-----')	
for error in error_dict:
	if (error_dict[error] > value_sum/3):
		print('your main pronunciation error is','[', error,']',error_dict[error],'times')

statistics.write(str(error_cnt))
statistics.close()
