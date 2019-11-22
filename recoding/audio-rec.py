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
photo = PhotoImage(file='microphone.png').subsample(35, 35)

label1 = ttk.Label(root, text = 'File Name')
label1.grid(row = 0, column = 0)

entry1 = ttk.Entry(root, width = 40) 
entry1.grid(row = 0, column = 1, columnspan = 4)

btn2 = tk.StringVar()

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

def save_file():
	sys.exit()

###


MyButton1 = ttk.Button(root, text='Start', width=10, command=callback)
MyButton1.grid(row = 0, column = 6)

MyButton2 = ttk.Button(root, text='Stop', width=10, command=stop)
MyButton2.grid(row = 0, column = 16)

MyButton3 = ttk.Button(root, text = 'Save Audio', width=10, command=save_file)
MyButton3.grid(row = 2,column = 4)

MyButton4 = ttk.Button(root, text = 'Quit', width=10, command=quit)
MyButton4.grid(row = 2, column = 14)

root.mainloop()
