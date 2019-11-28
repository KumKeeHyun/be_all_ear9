from tkinter import messagebox
import tkinter

import RPi.GPIO as GPIO

import pyaudio
import wave
import os
import sys
import socket

host = '192.168.0.12'
port = 8080

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def send_wav_file(fn):
	print('filename : ', fn)
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


class Rec(tkinter.Tk):
	def __init__(self):	
		self.main = tkinter.Tk()
		self.collections = []
	#chunk = 66536
		self.CHUNK = 66538 
		self.FORMAT = pyaudio.paInt16
		self.CHANNELS = 1
		self.RATE = 44100
		self.p = pyaudio.PyAudio()
		self.frames = []
		self.st = 1
		self.stream = self.p.open(format = self.FORMAT, channels = self.CHANNELS, rate = self.RATE, input = True, frames_per_buffer = self.CHUNK)
	
		self.initialize()
		
	def initialize(self):
		GPIO.add_event_detect(21, GPIO.FALLING, callback=self.callback)

		self.frame = tkinter.Frame(self.main)
		self.frame.pack()
	
		self.label1 = tkinter.Label(self.frame, text = 'File Name')
		self.label1.grid(row = 0, column = 5)

		self.entry1 = tkinter.Entry(self.frame, width = 40) 
		self.entry1.grid(row = 0, column = 6, columnspan = 4)

		self.label2 = tkinter.Label(self.frame, text = 'Your Text')
		self.label2.grid(row = 1, column = 5)

		self.entry2 = tkinter.Entry(self.frame, width = 40)
		self.entry2.grid(row = 1, column = 6, columnspan = 4)
	
		self.labelValue = tkinter.StringVar()
		self.label = tkinter.Label(self.frame, width = 60, fg ='white', bg = 'skyblue', textvariable=self.labelValue)
		self.label.grid(row = 3, column = 0, columnspan = 50)

		self.labelValue.set('empty') 

		self.MyButton3 = tkinter.Button(self.frame, text = 'Save Text', width=10, height=1, command=lambda: self.save_text())
		self.MyButton3.grid(row = 2, column = 7)

		self.MyButton4 = tkinter.Button(self.frame, text = 'Quit', width=10, height=1, command=lambda: self.quit())
		self.MyButton4.grid(row = 2, column = 8)

		tkinter.mainloop()

	def callback(self, channel):
		if (len(self.entry1.get())) == 0:
			messagebox.showinfo("Error", "Enter File Name")
		else:
			self.word =  self.entry1.get()
			self.start_rec(self.word)			

	def start_rec(self, word):
		self.st = 1
		self.frames = []
		self.filename = '/home/pi/github/be_all_ear9/speech_to_text/flac_set/wav_file/' + self.word + ".wav"
		WAVE_OUTPUT_FILENAME = self.filename
		#stream = self.p.open(format = self.FORMAT, channels = self.CHANNELS, rate = self.RATE, input = True, frames_per_buffer = self.CHUNK)
		stream = self.stream
		self.labelValue.set('recording') 
		GPIO.wait_for_edge(20, GPIO.FALLING)

		while (self.st == 1) :
			if GPIO.input(20) == GPIO.LOW:
				print('press')
				self.st = 0
				self.labelValue.set('done recording') 
			data = stream.read(self.CHUNK, exception_on_overflow = False)
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
