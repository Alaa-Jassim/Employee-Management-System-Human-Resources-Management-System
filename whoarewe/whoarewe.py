



from tkinter import *
from tkinter import filedialog
import csv
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image , ImageTk
from datetime import datetime
from threading import Thread
import webbrowser
from babel.dates import format_date, parse_date, get_day_names 
from babel.numbers import * 
from management_destination.management_exe import manager_Images


class WhoAreWe:
	def __init__(self,master):
		self.master = Toplevel()
		self.master.geometry("1000x400+450+100")
		self.master.title("الإتصال بنا")
		self.master.resizable(width=False,height=False)
		self.master.iconbitmap(manager_Images("images_whoarewe","title_app.ico"))
		self.master.configure(bg='white')

		self.title_app = Label(self.master,background="#E8E4FA",text='من نحن' , font=("bold",18))
		self.title_app.pack(fill=X)


		self.text = Text(self.master,width=200,height=20,font=("bold",20))
		self.text.place(x=4,y=40)