import os
import sys

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def get_flacFile():
	path = '/root/speech-to-text-wavenet/flac_data'
	files = [f for f in os.listdir(path) if os.path.isfile(os.ath.join(path, f))]
	return files

def tmp_child_process(): #test child process function
	fd = os.open('output.txt', os.O_RDWR|os.O_CREAT|os.O_APPEND)
	os.dup2(fd, sys.stdout.fileno())
	data_path = 'asset/data/LibriSpeech/test-clean/1089/134686/1089-134686-0001.flac'
	os.execl('/usr/bin/python', 'python', './recognize.py', '--file', data_path)


def child_process(flac_list):
	fd = os.open('output.txt', os.O_RDWR|os.O_CREAT|os.O_APPEND)
	os.dup2(fd, sys.stdout.fileno())
	data_path = '/root/speech-to-text-wavenet/flac_data/'

	for flac_data in flac_list:
		flac_path = data_path + flac_data
		os.execl('/usr/bin/python', 'python', './recognize.py', '--file', flac_path)


try:
    pid = os.fork()
except OSError:
    exit('fork error')

if pid == 0: #child process
	tmp_child_process()
	
	#flac_list = get_flacFile()
	#child_process(flac_list)
	exit()
else:
	status = os.wait()
