import os
from pydub import AudioSegment

def worker(filename):
	wav_sound = AudioSegment.from_wav(filename)
	new_name = filename.replace('.wav', '.flac')
	new_name = new_name.replace('wav_file', 'input')
	flac_sound = wav_sound.export(new_name, format='flac')
	return flac_sound

#file_name = 'recv_wav.wav'
#worker(file_name)
