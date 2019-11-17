import sys
import os
import record
import readline
import subprocess

os.system('clear')
print("===== RECORDING =====")


def process_word():
	os.system('clear')

	fin = open('file', "r")
	data_list = fin.readlines()
	fin.close()

	print("\n\n")

	word = data_list[:!][0].replace('\n','')

	print(word)

	print("\n\n")

	record.record_audio(word)

	print("\n\n")

def process_next_word():
	print("\n\n")

	next_word = raw_input("Are you ready for next word? Y/N : ")
	next_word = next_word.lower()

	if next_word == 'y':
		process_word()
		process_next_word()

	elif next_word == 'n' :
		print("Thanks")
	
	else:
		print("Enter Y or N")

answer = raw_input("Are you ready? Y/N: ")

if answer.lower() == 'y':
	process_word()
	process_next_word()
elif answer.lower() == 'n':
	print "Thanks"
	sys.exit()
