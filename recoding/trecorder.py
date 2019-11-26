from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

import pyaudio
import wave
import os
import sys


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

#		self.buttons = tk.Frame(self.main)
#		self.buttons.pack()

#		self.labels = tk.Frame(self.main)
#		self.labels.pack(fill = tk.BOTH)

		self.label1 = tk.Label(self, text = 'File Name')
		self.label1.grid(row = 0, column = 5)

		self.entry1 = tk.Entry(self, width = 40) 
		self.entry1.grid(row = 0, column = 6, columnspan = 4)

		self.label2 = tk.Label(self, text = 'Your Text')
		self.label2.grid(row = 10, column = 5)

		self.entry2 = tk.Entry(self, width = 40)
		self.entry2.grid(row = 10, column = 6, columnspan = 4)
	
		self.MyButton1 = tk.Button(self, text='Start', width=10, height=1, command=lambda: self.start_rec())
		self.MyButton1.grid(row = 30, column = 5)

		self.MyButton2 = tk.Button(self, text='Stop', width=10, height=1, command=lambda: self.stop_rec())
		self.MyButton2.grid(row = 30, column = 6)

		self.MyButton3 = tk.Button(self, text = 'Save Text', width=10, height=1, command=lambda: self.save_text())
		self.MyButton3.grid(row = 30, column = 7)

		self.MyButton4 = tk.Button(self, text = 'Quit', width=10, height=1, command=lambda: self.quit())
		self.MyButton4.grid(row = 30, column = 8)

		tk.mainloop()

	def callback():
		if len(entry1.get()) == 0:
			messagebox.showinfo("Error", "Enter File Name")
		else:
			word = entry1.get()
		#	start_rec(word)			

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
