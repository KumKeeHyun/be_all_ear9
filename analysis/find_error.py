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
			#fill function

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


#open a file, read sentence by sentence and fill anal_node_que
#use analysis_sentence
def read_sentence_file(c_txt_path, v_txt_path):
        c = open(c_txt_path, mode = 'r')
        c_sentence = c.read()
        
        v = open(v_txt_path, mode = 'r')
        v_sentence = v.read()

