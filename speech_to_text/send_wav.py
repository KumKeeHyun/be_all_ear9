import socket
import sys
import os

#host = '172.17.0.1'
host = '192.168.0.12'
port = 8080

#--------------------------------------

sd = socket.socket()
sd.connect((host, port))

f_path = './flac_set/wav_file/wav_example.wav'

with open(f_path, 'rb') as fd:
	print('file opened', f_path)

	line = fd.read(1024)
	while (line):
		sd.send(line)
		line = fd.read(1024)

	print('send done')
	sd.close()
