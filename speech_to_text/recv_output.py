import socket
import os

host = '192.168.0.23'
port = 5000

f = './flac_set/output/output.txt'
fd = open(f, 'w')
fd.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)



while True:
	sd, addr = s.accept()
	print('Got sock from', addr)

	with open(f, 'ab') as fd:
		line = sd.recv(1024)
		while (line):
			fd.write(line)
			line = sd.recv(1024)
	print('recv done')
	fd.close()
	sd.close()
