from tkinter import ttk
from tkinter import *
import tkinter as tk

import time
import sys
import os
import record
import readline
import subprocess

root = tk.Tk()
root.title('Recorder')

label1 = ttk.Label(root, text = 'File Name')
label1.grid(row = 0, column = 0)

entry1 = ttk.Entry(root, width = 40) 
entry1.grid(row = 0, column = 2, columnspan = 4)

label2 = ttk.Label(root, text = 'Your Text')
label2.grid(row = 4, column = 0)

entry2 = ttk.Entry(root, width = 40)
entry2.grid(row = 4, column = 2, columnspan = 4)

##definitions here
def callback():
	if len(entry1.get()) == 0:
		messagebox.showinfo("Error", "Enter File Name")
	else:
		word = entry1.get()
		record.record_audio(word)

def stop():
	sys.exit()

def quit():
	sys.exit()

def save_text():
	sys.exit()

###


MyButton1 = ttk.Button(root, text='Start', width=10, command=callback)
MyButton1.grid(row = 0, column = 8)

MyButton2 = ttk.Button(root, text='Stop', width=10, command=stop)
MyButton2.grid(row = 0, column = 18)

MyButton3 = ttk.Button(root, text = 'Save Text', width=10, command=save_text)
MyButton3.grid(row = 4,column = 8)

MyButton4 = ttk.Button(root, text = 'Quit', width=10, command=quit)
MyButton4.grid(row = 4, column = 18)

root.mainloop()
