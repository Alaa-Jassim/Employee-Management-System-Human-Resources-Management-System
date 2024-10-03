
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image , ImageTk
from datetime import datetime
import os , sys
import docx
from datetime import datetime
import os , sys , shutil
import sqlite3
from threading import Thread
from tkinter import filedialog
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 

class DataBaseSetting:
	def __init__(self, root):
		self.root = root
		self.var_language = StringVar() 

	def clicked_connect(self):
		print(self.var_language.get())