import socket
from wav_to_flac import worker
import os

host = '172.17.0.1'
#host = '192.168.0.4'
port = 8080

#---------------------------------------

class _file_name:
	def __init__(self, f_path, f_format):
		self.file_path = f_path
		self.file_format = f_format
		self.file_num = 0

	def get_file_name(self):
		result = self.file_path + str(self.file_num) + self.file_format
		self.file_num += 1
		return result



f_path = './flac_set/wav_file/voice_'
f_format = '.wav'
file_name = _file_name(f_path, f_format)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

while True:
	sd, addr = s.accept()
	print('Got sock from', addr)
	
	f = file_name.get_file_name()
	with open(f, 'wb') as fd:
		print('file opened', f)

		line = sd.recv(1024)
		while (line):
			fd.write(line)
			line = sd.recv(1024)
	
	fd.close()
	sd.close()
	print('success get file')
	
	worker(f)
	print('success change format')
	os.remove(f)

