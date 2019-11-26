from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

import pyaudio
import wave
import os
import sys
import socket

host = '192,168.0.5'
port = 8080

def send_wav_file(fn):
	sd = socket.socket()
	sd.connect((host, port))
	print('connect')
	with open(fn, 'rb') as fd:
		print('open', fn)
		line = fd.read(1024)
		while (line):
			sd.send(line)
			line = fd.read(1024)
		print('send done')
		sd.close()


class Rec(tk.Tk):
	def __init__(self, chunk = 1024, frmt = pyaudio.paInt16, channels = 1, rate = 44100, py = pyaudio.PyAudio()):
	
		self.main = tk.Tk()
		tk.Tk.__init__(self)
		self.collections = []
		self.CHUNK = chunk
		self.FORMAT = frmt
		self.CHANNELS = channels
		self.RATE = rate
		self.p = py
		self.frames = []
		self.st = 1
		self.stream = self.p.open(format = self.FORMAT, 
								channels = self.CHANNELS,
								rate = self.RATE,
								input = True,
								frames_per_buffer = self.CHUNK)

		self.initialize()

	def initialize(self):
		self.label1 = tk.Label(self, text = 'File Name')
		self.label1.grid(row = 0, column = 5)

		self.entry1 = tk.Entry(self, width = 40) 
		self.entry1.grid(row = 0, column = 6, columnspan = 4)

		self.label2 = tk.Label(self, text = 'Your Text')
		self.label2.grid(row = 1, column = 5)

		self.entry2 = tk.Entry(self, width = 40)
		self.entry2.grid(row = 1, column = 6, columnspan = 4)
	
		self.labelValue = tk.StringVar()
		self.label = tk.Label(self, width = 60, fg ='white', bg = 'skyblue', textvariable=self.labelValue)
		self.label.grid(row = 3, column = 0, columnspan = 50)

		self.labelValue.set('empty') 

		self.MyButton1 = tk.Button(self, text='Start', width=10, height=1, command=lambda: self.callback())
		self.MyButton1.grid(row = 2, column = 5)

		self.MyButton2 = tk.Button(self, text='Stop', width=10, height=1, command=lambda: self.stop_rec())
		self.MyButton2.grid(row = 2, column = 6)

		self.MyButton3 = tk.Button(self, text = 'Save Text', width=10, height=1, command=lambda: self.save_text())
		self.MyButton3.grid(row = 2, column = 7)

		self.MyButton4 = tk.Button(self, text = 'Quit', width=10, height=1, command=lambda: self.quit())
		self.MyButton4.grid(row = 2, column = 8)

	def callback(self):
		if (len(self.entry1.get())) == 0:
			messagebox.showinfo("Error", "Enter File Name")
		else:
			self.word =  self.entry1.get()
			self.start_rec(self.word)			

	def start_rec(self, word):
		self.st = 1
		self.frames = []
		self.filename = '/home/userr/Desktop/ws/be_all_ear9/speech_to_text/flac_set/wav_file/' + self.word + ".wav"
		WAVE_OUTPUT_FILENAME = self.filename
		stream = self.p.open(format = self.FORMAT, 
							channels = self.CHANNELS,
							rate = self.RATE,
							input = True,
							frames_per_buffer = self.CHUNK)

		self.labelValue.set('recording') 

		while self.st == 1 :
			data = stream.read(self.CHUNK)
			self.frames.append(data)
			self.main.update()

		stream.close()
			
		wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		wf.setnchannels(self.CHANNELS)
		wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
		wf.setframerate(self.RATE)
		wf.writeframes(b''.join(self.frames))
		wf.close()
		send_wav_file(WAVE_OUTPUT_FILENAME)

	def stop_rec(self):
		self.st = 0
		self.labelValue.set('done recording') 

	def save_text(self):
		sys.exit()
		#work in progress

	def quit(self):
		sys.exit()			

guiAUD = Rec()		
guiAUD.title = 'ReCoRD'
guiAUD.mainloop()
