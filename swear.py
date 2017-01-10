#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
from tkinter import messagebox 

#imports
import shows
import psa
import instructions

class swearLog:

	def __init__(self):

		#create the window and title it
		self.root = Toplevel()
		self.root.title("SWEAR LOG")
		self.root.resizable(FALSE,FALSE)

		self.songName     = StringVar()
		self.songArtist   = StringVar()
		self.songComposer = StringVar()

		#create the frames
		self.infoFrame   = ttk.Frame(self.root, borderwidth=5, relief="sunken")
		self.whoFrame    = ttk.Frame(self.root, borderwidth=5, relief="sunken")
		self.songFrame   = ttk.Frame(self.root, borderwidth=5, relief="sunken")
		self.djFrame     = ttk.Frame(self.root, borderwidth=5, relief="sunken")
		self.swearFrame  = ttk.Frame(self.root, borderwidth=5, relief="sunken")
		self.submitFrame = ttk.Frame(self.root, borderwidth=5, relief="sunken")

		#place frames
		self.infoFrame.grid(    column=0,  row=0,  columnspan=50,  rowspan=5,  sticky=(N, W, E, S))
		self.whoFrame.grid(     column=0,  row=5,  columnspan=50,  rowspan=5,  sticky=(N, W, E, S))
		self.songFrame.grid(    column=0,  row=10,  columnspan=50,  rowspan=7,  sticky=(N, W, E, S))
		self.djFrame.grid(      column=0,  row=10,  columnspan=50,  rowspan=7,  sticky=(N, W, E, S))
		self.swearFrame.grid(   column=0,  row=17,  columnspan=50,  rowspan=5,  sticky=(N, W, E, S))
		self.submitFrame.grid(  column=0,  row=22,  columnspan=50,  rowspan=5,  sticky=(N, W, E, S))

		#Create labels
		self.songName_lbl     = ttk.Label(self.songFrame, text="Song Name:")
		self.songArtist_lbl   = ttk.Label(self.songFrame, text="Song Artist:")
		self.songComposer_lbl = ttk.Label(self.songFrame, text="Song Composer:")

		self.djName_lbl     = ttk.Label(self.djFrame, text="DJ Name:")

		#Place labels
		self.songName_lbl.grid(    column=0, row=1, columnspan=3, sticky=W)
		self.songArtist_lbl.grid(  column=0, row=2, columnspan=3, sticky=W)
		self.songComposer_lbl.grid(column=0, row=3, columnspan=3, sticky=W)

		self.djName_lbl.grid(column=0, row=1, columnspan=3, sticky=W)

		#Create text boxes
		self.songName_entry     = ttk.Entry(self.songFrame, width=7, textvariable=self.songName)
		self.songArtist_entry   = ttk.Entry(self.songFrame, width=7, textvariable=self.songArtist)
		self.songComposer_entry = ttk.Entry(self.songFrame, width=7, textvariable=self.songComposer)

		self.djName_entry = ttk.Entry(self.djFrame, width=7, textvariable=self.songComposer)


		#Place Text Boxes
		self.songComposer_entry.grid(column=3, row=3, columnspan=6, sticky=(W, E))
		self.songArtist_entry.grid(  column=3, row=2, columnspan=6, sticky=(W, E))
		self.songName_entry.grid(    column=3, row=1, columnspan=6, sticky=(W, E))

		self.djName_entry.grid(    column=3, row=1, columnspan=6, sticky=(W, E))

		self.radioWho = [ ("Song", "SONG"), ("DJ", "DJ"),]

		self.radioVar = IntVar()
		self.radioVar.set(1)
		#self.radioVar.set(self.radioWho[0][1])


		self.radioButtonA = ttk.Radiobutton(self.infoFrame, text=self.radioWho[0][0], 
										variable=self.radioVar, value=1, 
										command=self.switchMode)
		self.radioButtonB = ttk.Radiobutton(self.infoFrame, text=self.radioWho[1][0], 
										variable=self.radioVar, value=2, 
										command=self.switchMode)
		
		self.radioButtonA.pack(anchor=W)

		self.radioButtonB.pack(anchor=W)

		self.root.mainloop()

	def openSwearLog(self,show_name):
		x =1

		


	def switchMode(self):
		if self.radioVar == 1:
			x = 1
			self.djFrame.grid_remove()

			self.songFrame.grid(    column=0,  row=10,  columnspan=50,  rowspan=7,  sticky=(N, W, E, S))
		elif self.radioVar == 2:
			x = 1
			self.songFrame.grid_remove()
			self.djFrame.grid(      column=0,  row=10,  columnspan=50,  rowspan=7,  sticky=(N, W, E, S))



	
