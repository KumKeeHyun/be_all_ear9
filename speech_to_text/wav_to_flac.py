import os
from pydub import AudioSegment

def worker(filename):
	file_path = './flac_set/wav_file/'
	file_path = file_path + filename
	wav_sound = AudioSegment.from_wav(file_path)
	new_name = filename.replace('.wav', '.flac')
	file_path = './flac_set/input/'
	file_path = file_path + new_name
	flac_sound = wav_sound.export(file_path, format='flac')
	return flac_sound

file_name = 'recv_wav.wav'
worker(file_name)
