from tkinter import ttk
from tkinter import *
import tkinter as tk
import tkinter.messagebox

import pyaudio
import wave
import os
import sys


class Rec:
	def __init__(self, chunk = 1024, frmt = pyaudio.paInt16, channels = 1, rate = 44100, py = pyaudio.PyAudio()):
	
		self.main = tkinter.Tk()
		self.collections = []
		self.main.title('Record')
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

		self.buttons = tkinter.Frame(self.main)
		self.buttons.pack(fill = tk.BOTH)
		self.labels = tkinter.Frame(self.main)
		self.labels.pack(fill = tk.BOTH)
#		self.entry = tkinter.Frame(self.main)
#		self.entry.pack(fill =  tk.BOTH)

		label1 = ttk.Label(self.labels, text = 'File Name')
		label1.grid(row = 0, column = 0)

#		entry1 = ttk.Entry(self.entry, width = 40) 
#		entry1.grid(row = 0, column = 2, columnspan = 4)

		label2 = ttk.Label(self.labels, text = 'Your Text')
		label2.grid(row = 4, column = 0)

#		entry2 = ttk.Entry(self, width = 40)
#		entry2.grid(row = 4, column = 2, columnspan = 4)
	
		MyButton1 = ttk.Button(self.buttons, text='Start', width=10, command=lambda: self.start_rec())
		MyButton1.grid(row = 0, column = 8)

		MyButton2 = ttk.Button(self.buttons, text='Stop', width=10, command=lambda: self.stop_rec())
		MyButton2.grid(row = 0, column = 18)

		MyButton3 = ttk.Button(self.buttons, text = 'Save Text', width=10, command=lambda: self.save_text())
		MyButton3.grid(row = 4, column = 8)

		MyButton4 = ttk.Button(self.buttons, text = 'Quit', width=10,  command=lambda: self.quit())
		MyButton4.grid(row = 4, column = 18)

		tkinter.mainloop()

	def callback():
		if len(entry1.get()) == 0:
			messagebox.showinfo("Error", "Enter File Name")
		else:
			word = entry1.get()
			

	def start_rec(self):
		self.st = 1
		self.frames = []
#		self.filename = word + ".wav"
		stream = self.p.open(format = self.FORMAT, 
							channels = self.CHANNELS,
							rate = self.RATE,
							input = True,
							frames_per_buffer = self.CHUNK)

		while self.st == 1 :
			data = stream.read(self.CHUNK)
			self.frames.append(data)
			self.main.update()

		stream.close()
			
		wf = wave.open('test_recording.wav', 'wb')
		wf.setnchannels(self.CHANNELS)
		wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
		wf.setframerate(self.RATE)
		wf.writeframes(b''.join(self.frames))
		wf.close()

	def stop_rec(self):
		self.st = 0

	def save_text(self):
		sys.exit()
		#work in progress

	def quit(self):
		sys.exit()			


guiAUD = Rec()		


##definitions here
def callback():
	if len(entry1.get()) == 0:
		messagebox.showinfo("Error", "Enter File Name")
	else:
		word = entry1.get()
		record.record_audio(word)

