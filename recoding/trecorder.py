from tkinter import messagebox
import tkinter

import RPi.GPIO as GPIO
import time
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
GPIO.setup(4, GPIO.OUT)

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
		self.CHUNK = 66536 
		self.FORMAT = pyaudio.paInt16
		self.CHANNELS = 1
		self.RATE = 44100
		self.p = pyaudio.PyAudio()
		self.frames = []
		self.st = 1
		#self.stream = self.p.open(format = self.FORMAT, channels = self.CHANNELS, rate = self.RATE, input = True, frames_per_buffer = self.CHUNK)
	
		self.initialize()
		
	def initialize(self):
		GPIO.add_event_detect(21, GPIO.FALLING, callback=self.callback)

		self.frame = tkinter.Frame(self.main)
		self.frame.pack()
	
		self.label1 = tkinter.Label(self.frame, text = 'File Name')
		self.label1.grid(row = 0, column = 5)

		self.entry1 = tkinter.Entry(self.frame, width = 40) 
		self.entry1.grid(row = 0, column = 6, columnspan = 4)

		self.labelValue = tkinter.StringVar()
		self.label = tkinter.Label(self.frame, width = 70, fg ='white', bg = 'skyblue', textvariable=self.labelValue)
		self.label.grid(row = 1, column = 0, columnspan = 50)

		self.labelValue.set('empty') 

		self.MyButton = tkinter.Button(self.frame, text = 'Quit', width=10, height=1, command=lambda: self.quit())
		self.MyButton.grid(row = 0, column = 45)

		tkinter.mainloop()

	def callback(self, channel):
		GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		time.sleep(1)
		if (len(self.entry1.get())) == 0:
			messagebox.showinfo("Error", "Enter File Name")
		else:
			self.word =  self.entry1.get()
			self.start_rec(self.word)			

	def start_rec(self, word):
		print("0")
		self.st = 1
		self.frames = []
		self.filename = '/home/pi/github/be_all_ear9/speech_to_text/flac_set/wav_file/' + self.word + ".wav"
		WAVE_OUTPUT_FILENAME = self.filename
		stream = self.p.open(format = self.FORMAT, channels = self.CHANNELS, rate = self.RATE, input = True, frames_per_buffer = self.CHUNK)
		self.labelValue.set('recording') 
		GPIO.output(4, True)
		GPIO.wait_for_edge(20, GPIO.FALLING)

		while (self.st == 1) :
			if GPIO.input(20) == GPIO.LOW:
				GPIO.output(4, False)
				self.st = 0
				self.labelValue.set('done recording') 
				time.sleep(1)
			data = stream.read(self.CHUNK, exception_on_overflow = False)
			self.frames.append(data)
			self.main.update()

		stream.close()

		wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		wf.setnchannels(self.CHANNELS)
		wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
		wf.setframerate(self.RATE)
		wf.writeframes(b''.join(self.frames))
		print('3')	
		wf.close()
		send_wav_file(WAVE_OUTPUT_FILENAME)

	def stop_rec(self):
		self.st = 0
		self.labelValue.set('done recording') 

	def quit(self):
		sys.exit()			

guiAUD = Rec()		
