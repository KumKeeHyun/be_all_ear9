mport os
import sys
import time
import socket

host = '192.168.0.23'
port = 5000

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

def get_flacFile(path):
	#path = './flac_data/input'
	onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
	return onlyfiles

def child_process(flac_list):
	#fd = os.open('./flac_data/output/output.txt', os.O_RDWR|os.O_CREAT|os.O_APPEND)
	sd = socket.socket()
	sd.connect((host, port))

	#os.dup2(fd, sys.stdout.fileno())
	os.dup2(sd.fileno(), sys.stdout.fileno())
	data_path = './flac_data/input/'

	for flac_data in flac_list:
	flac_path = data_path + flac_data
	os.execl('/usr/bin/python', 'python', './recognize.py', '--file', flac_path)


while True:
	flac_list = get_flacFile('./flac_data/input')
	if len(flac_list) == 0:
    	print('empty input files')
        time.sleep(20)
        continue;

	print('recognize flac files!')

	try:
		pid = os.fork()
	except OSError:
		exit("fork error")

	if pid == 0:
		print(flac_list)
		child_process(flac_list)
		exit()
	else:
		status = os.wait()
		print('end child process')
		for flac in flac_list:
			path = './flac_data/input/' + flac
			print(path)
			os.remove(path)



