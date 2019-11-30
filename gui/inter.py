import tkinter
import sys
import os

class GUI(tkinter.Tk):
	def __init__(self):
		self.v_path = '../speech_to_text/flac_set/output/output.txt'
		self.c_path = '../analysis/c_output.txt'
		self.s_path = './stat_output.txt'
		self.main = tkinter.Tk()
		self.main.title('Statics')
		self.initialize()

	def initialize(self):
		self.frame = tkinter.Frame(self.main)
		self.frame.pack()
		
		self.resValue = tkinter.StringVar()
		self.res = tkinter.Label(self.frame, width = 80, height = 15, bg = 'skyblue', textvariable = self.resValue)
		self.res.grid(row = 0, column = 0, columnspan = 40,  padx = 1, pady = 2)

		self.resValue.set(' ')
		
		self.empty = tkinter.Label(self.frame, width = 80, height = 1)
		self.empty.grid(row = 1, column = 0, columnspan = 40, padx = 1)

		self.vsentValue = tkinter.StringVar()

		self.vsent = tkinter.Label(self.frame, anchor = 'w', width = 60, bg = 'white', textvariable = self.vsentValue)
		self.vsent.grid(row = 2, column = 1, columnspan = 20, padx = 1, pady = 2, ipadx = 2)

		self.vsentValue.set('v_sentence')
		
		self.csent = tkinter.Entry(self.frame, width = 60)
		self.csent.grid(row = 3, column = 1, columnspan = 20, padx = 1, pady = 2, ipadx = 2)

		self.enter = tkinter.Button(self.frame, text = 'enter', width = 10, command=lambda: self.entercb())
		self.enter.grid(row = 3, column = 35, padx = 1, pady = 2)

		self.start = tkinter.Button(self.frame, text = 'input start', width = 10, height = 2, command=lambda: self.callback())
		self.start.grid(row = 4, column = 1, padx = 1, pady = 2)
		
		self.out = tkinter.Button(self.frame, text = 'show result', width = 10, height = 2, command=lambda: self.showstat())
		self.out.grid(row = 4, column = 2, padx = 1, pady = 2)

		self.die = tkinter.Button(self.frame, text = 'quit', width = 10, height = 2, command=lambda: self.quit())
		self.die.grid(row = 4, column = 35, padx = 2, pady = 2)

		tkinter.mainloop()

	def callback(self):
		#print("something pressed")
		with open(self.v_path, 'r') as f:
			self.lines = f.readlines()
			self.lines_idx = 0
			f.close()
		self.c_fd = open(self.c_path, 'w')
		self.print_vline()
	
	def print_vline(self):
		if self.lines_idx == len(self.lines):
			self.c_fd.close()
			self.vsentValue.set("end of file")

		else: 
			text = self.lines[self.lines_idx][:-1]
			self.vsentValue.set(text)
			self.lines_idx += 1
		
	def entercb(self):
		if (len(self.csent.get())) == 0 :
			messagebox.showinfor("Error", "Enter sentence")
		else:
			text = self.csent.get()
			self.c_fd.write(text+'\n')
			self.print_vline()
	
	def showstat(self):
		stat_string = ''
		try:
			pid = os.fork()
		except OSError:
			exit("fork error")
		if pid == 0:
			fd = os.open(self.s_path, os.O_RDWR|os.O_TRUNC)
			os.dup2(fd, sys.stdout.fileno())
			os.execl('/usr/bin/python3', 'python3', '../analysis/statistics.py')
			exit()
		else:
			os.wait()
			with open(self.s_path, 'r') as f:
				lines = f.readlines()
				for line in lines:
					stat_string += line
				f.close()
			print(stat_string)
		self.resValue.set(stat_string)
			
	def quit(self):
		sys.exit()

guiInter = GUI()	
