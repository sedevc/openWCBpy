#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import Tkinter as tk
import ttk as ttk
import PIL, tkFont
from abio import TempSensor, AnalogOut, AnalogLambda, FireSensor
from jsonrpclib import Server
from requests import put, get

REST_SERVER_URL = "http://127.0.0.1:5000"




#################################################################
######################### GUI ###################################
#################################################################

def task():
	try:
		AllTemp = get(REST_SERVER_URL).json()
		print AllTemp['Boiler']
		tTempVar.set(str(int(AllTemp['Tank'])) + "℃")
		bTempVar.set(str(int(AllTemp['Boiler'])) + "℃")	
		fTempVar.set(str(int(AllTemp['Fire'])) + "℃")
		fanRpmVar.set(str(int(AllTemp['Fan rpm'])) + "rpm")
		
	except:
		pass
	root.after(1000,task)
# ----------- GUI ROOT ------------ #

root = tk.Tk()
root.geometry("%dx%d" % (800, 400))
root.title('Autoburner V0.1')
# -------------------------------- #

tTempVar = StringVar()
bTempVar = StringVar()
fTempVar = StringVar()
fanRpmVar = StringVar()

tTempVar.set(0)
bTempVar.set(0)
fTempVar.set(0)
fanRpmVar.set(0)

# ------------ Font --------------- #
f = tkFont.Font(family='helvetica', size=-16)
s = ttk.Style()
s.configure('.', font=f)
# --------------------------------- #

# ---------- Notebook ------------ #
nb = ttk.Notebook(root)
nb.pack(fill='both', expand='yes')
# create a child frame for each page
status = tk.Frame()
settings = tk.Frame()#bg='blue')
log = tk.Frame()

# create the pages
nb.add(status, text='Status')
nb.add(settings, text='Settings')
nb.add(log, text='Log')
# -------------------------------- #

# ---------- BACKGROUND ---------- #
background_image = PhotoImage(file="boiler.gif")
background_label = Label(status, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# ------------------------------- #

# ℃

# ---------- Labels ------------- #
tTempLabel = Label(status, textvariable=tTempVar, fg="black", font=("Helvetica", 16))
tTempLabel.place(x=103, y=97)

bTempLabel = Label(status, textvariable=bTempVar, fg="black", font=("Helvetica", 16))
bTempLabel.place(x=360, y=125)

fTempLabel = Label(status, textvariable=fTempVar, fg="red", font=("Helvetica", 16))
fTempLabel.place(x=500, y=270)

LambdaLabel = Label(status, text="1.4λ", fg="black", font=("Helvetica", 16))
LambdaLabel.place(x=265, y=123)

FanLabel = Label(status, textvariable=fanRpmVar, fg="black", font=("Helvetica", 12))
FanLabel.place(x=510, y=180)
# ------------------------------- #

# put a button widget on child frame f1 on page1
btn1 = tk.Button(log, text='button1')
btn1.pack(side='left', anchor='nw', padx=3, pady=5)


root.after(1000,task)



root.mainloop()
