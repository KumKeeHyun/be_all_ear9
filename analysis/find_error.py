#find error
from queue import Queue

#------------------------class-----------------------------
class anlys_node:
    
    def __init__(self, correct_word, voice_word):
        self.c_word = correct_word.lower()
        self.v_word = voice_word.lower()
        #self.word_tag = ""
        self.typo_cnt = 0
        self.error = []
        self.error_match = {'&' : 'th',
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
        
        self.to_phonics = {'th' : '&',
                           'ck' : '^',
                           'ph' : '#',
                           'oo' : '0',
                           'aw' : '9',
                           'ou' : '8',
                           'oa' : '7',
                           'ir' : '6',
                           'ur' : '5',
                           'or' : '4',
                           'ar' : '3',
                           'er' : '2',
                           'ow' : '1'}
        
        self.error_cnt = {'&' : 0,
                          '^' : 0,
                          '#' : 0,
                          '0' : 0,
                          '9' : 0,
                          '8' : 0,
                          '7' : 0,
                          '6' : 0,
                          '5' : 0,
                          '4' : 0,
                          '3' : 0,
                          '2' : 0,
                          '1' : 0}
        
        self.convert_phonics()
        self.analysis_str()
        self.count_error()
        if self.c_word == self.v_word:
            print('no error')
        for error in list(set(self.error)):
            print("occur","\"", self.error_match[error],"\"", "error, ", self.typo_cnt,"times")
        
                
    def analysis_str(self): #fill self.error(list)
        if (self.c_word is not self.v_word):
            
            if len(self.v_word) <= len(self.c_word):
                same_list = find_same_string(self.c_word, self.v_word)
                for error in remove_same(self.c_word, self.v_word):
                    if error in self.error_match:
                        self.error.append(error)
            
            else:
                same_list = find_same_string(self.v_word, self.c_word)
                for error in remove_same(self.c_word, self.v_word):
                    if error in self.error_match:
                        self.error.append(error)
            
    def count_error(self):
        for error in self.error:
            if error in self.error:
                self.error_cnt[error] += 1
                self.typo_cnt += 1
        return self.error_cnt, self.typo_cnt

    def convert_phonics(self): # ex) 'th' -> '&'
        phonics_list = list(self.error_match.values())
        for phonics in phonics_list:
            if phonics in self.c_word:
                self.c_word = self.c_word.replace(phonics, self.to_phonics[phonics])
#------------------------class-----------------------------


#------------------------functions-----------------------------
def find_same_string(str1, str2): # len(str1) >= len(str2)
        answer = []
        for i in range(len(str1)):
                same = ''
                for j in range(len(str2)):
                        if (i+j < len(str1)):
                                if (str1[i+j] == str2[j]):
                                        same += str2[j]
                if (same != ''):
                        answer.append(same)

        return answer

def remove_same(converted_str1, str2):
    if len(converted_str1) >= len(str2):
        for letter in find_same_string(converted_str1, str2):
            if letter in converted_str1:
                converted_str1 = converted_str1.replace(letter, "")
    else :
        for letter in find_same_string(str2, converted_str1):
            if letter in converted_str1:
                converted_str1 = converted_str1.replace(letter, "")
    return converted_str1


#stored analysis_node temporarily
anal_node_que = Queue(100)

#take a sentence and divide it into words and save, return in a list
def split_sentence(sentence):
    word_list = []
	
    for word in sentence.split(): 
        word_list.append(word)
            
    return word_list


#take a list of words and analyze them and store them in a queue	
#use split_sentence, anlys_node
#the way to add anly_node to queue is
#anal_node_que.put(anlys_node(c_word, v_word))
def analysis_sentence(c_sentence, v_sentence):
        pass
	#fill function
        print(c_sentence.split(' '))
        print(v_sentence.split(' '))
        while(1):
                if c_sentence.split(' ')[i]==v_sentence[i]:
                    pass
                else:
                    anlys_node_que+=v_sentence[i]
                i+=1


#open a file, read sentence by sentence and fill anal_node_que
#use analysis_sentence
def read_sentence_file(c_txt_path, v_txt_path):
    c_sentence_list = []
    v_sentence_list = []
    c_sentence = 'none'
    v_sentence = 'none'
    
    c = open(c_txt_path, mode = 'r')
    v = open(v_txt_path, mode = 'r')

    while c_sentence != '':
        c_sentence = c.readline()
        c_sentence_list.append(c_sentence)

    while v_sentence != '':
        v_sentence = v.readline()
        v_sentence_list.append(v_sentence)

    c.close()
    v.close()
    
        
    return c_sentence_list, v_sentence_list

