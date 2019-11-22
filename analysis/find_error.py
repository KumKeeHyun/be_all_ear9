#123
#find error
from queue import Queue

class anlys_node:
        def __init__(self, correct_word, voice_word):
                    self.c_word = correct_word
                    self.v_word = voice_word
                    self.word_tag = ""
                    self.typo_cnt = 0
                    self.analysis_str()
	
	#compare self.c_word and self.v_word
	#get values (word_tag and typo_cnt....)
        def analysis_str(self):
                if (self.c_word is not self.v_word):
                        if len(self.v_word) < len(self.c_word):
                                pass
                        #elif len(self.v_word) == len(self.c_word):
                                pass
                        #else:
                                pass
def make_set(s):
            result =set()
            for i in range(len(s)):
                for j in range(i+1,len(s)+1):
                    result.add(s[i:j])
            return result
def lcs(word1,word2):
            max=0
            index=0
            letters=[[0 for _ in range(len(word2)+1)]for _ in range(len(word1)+1)]
            for i in range(len(word1)):
                for j in range (len(word2)):
                    if word1[i]==word2[j]:
                        letters[i+1][j+1]=letters[i][j]+1
                    if max<letters[i+1][j+1]:
                        max=letters[i+1][j+1]
                        index=i+1
            return word1[index-max:index]

def convert_phonics(self, correct_word):
                if 'th' in correct_word:
                        converted = correct_word.replace('th', '&')
                if 'ck' in correct_word:
                        converted = correct_word.replace('ck', '!')
                if 'oo' in correct_word:
                        converted = correct_word.replace('oo','0')
                if 'aw' in correct_word:
                        converted = correct_word.replace('aw','9')
                if 'ou' in correct_word:
                        converted = correct_word.replace('ou','8')
                if 'oa' in correct_word:
                        converted = correct_word.replace('oa','7')
                if 'ir' in correct_word:
                        converted = correct_word.replace('ir','6')
                if 'ur' in correct_word:
                        converted = correct_word.replace('ur','6')
                if 'or' in correct_word:
                        converted = correct_word.replace('or','5')
                if 'ar' in correct_word:
                        converted = correct_word.replace('ar','4')
                if 'er' in correct_word:
                        converted = correct_word.replace('er','3')
                if 'ow' in correct_word:
                        converted = correct_word.replace('ow','2')


#stored analysis_node temporarily
anal_node_que = Queue(100)

#take a sentence and divide it into words and save, return in a list
def split_sentence(sentence):
	word_list = []
	for word in sentence.split:
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
        c = open(c_txt_path, mode = 'r')
        c_sentence = c.read()
        
        v = open(v_txt_path, mode = 'r')
        v_sentence = v.read()


