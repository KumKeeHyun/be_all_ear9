import tkinter
import sys

class GUI(tkinter.Tk):
	def __init__(self):
		self.main = tkinter.Tk()
		self.initialize()

	def initialize(self):
		self.frame = tkinter.Frame(self.main)
		self.frame.pack()
		
		self.resValue = tkinter.StringVar()
		self.res = tkinter.Label(self.frame, width = 70, height = 30, bg = 'skyblue', textvariable = self.resValue)
		self.res.grid(row = 0, column = 0)

		self.resValue.set('init')
		
		self.vsentValue = tkinter.StringVar()
		self.vsent = tkinter.Label(self.frame, width = 50, bg = 'white', textvariable = self.vsentValue)
		self.vsent.grid(row = 1, column = 0, columnspan = 20)

		self.vsentValue.set('v_sentence')
		
		self.csent = tkinter.Entry(self.frame, width = 50)
		self.csent.grid(row = 2, column = 0, columnspan = 20)

		self.enter = tkinter.Button(self.frame, text = 'enter', width = 10, command=lambda: self.callback())
		self.enter.grid(row = 2, column = 50)

		self.start = tkinter.Button(self.frame, text = 'input start', width = 8, height = 4, command=lambda: self.callback())
		self.start.grid(row = 3, column = 0)
		
		self.out = tkinter.Button(self.frame, text = 'show result', width = 8, height = 4, command=lambda: self.callback())
		self.out.grid(row = 3, column = 1)

		self.quit = tkinter.Button(self.frame, text = 'quit', width = 8, height = 4, command=lambda: self.quit())
		self.quit.grid(row = 3, column = 2)

		tkinter.mainloop()

	def callback(self):
		print("something pressed")

	def quit(self):
		sys.exit()

guiInter = GUI()	
