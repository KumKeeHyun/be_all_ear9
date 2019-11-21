import socket

host = '172.17.0.1'
port = 8080

path = './flac_set/wav_file/recv_wav.wav'

s = socket.socket()
s.connect((host, port))

with open(path, 'wb') as f:
    print('file opened')
        
    line = s.recv(1024)
    while (line):
    	f.write(line)
    	line = s.recv(1024)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
