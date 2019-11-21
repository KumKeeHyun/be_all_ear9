import socket
import sys
import os

host = '172.17.0.1'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

while True:
	sd, addr = s.accept()
	print('Got sdection from', addr)
	
	file_path = './flac_set/wav_file/wav_example.wav'
	f = open(file_path, 'rb')
	line = f.read(1024)
	while (line):
		sd.send(line)
		line = f.read(1024)

	print('Done sending')
	sd.close()


