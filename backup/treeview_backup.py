

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

sys.path.append('../')
from management_destination.management_exe import manager_Images, manager_Sqlite3
 
class NodeTreeviewBackUp:
	def __init__(self, root):
		self.root = root

		self.table_data_backup = ttk.Treeview(self.root,
			columns=("Backup", "Backup_history"))

		self.table_data_backup["show"] = "headings"
		self.table_data_backup.heading("Backup", text="النسخة الإحتياطية")
		self.table_data_backup.heading("Backup_history", text="تأريخ النسخة الإحتياطية")


		self.table_data_backup.column("Backup", width=220, anchor=CENTER)
		self.table_data_backup.column("Backup_history", width=100, anchor=CENTER)


class TreeviewBackUp(NodeTreeviewBackUp):
	def __init__(self, root):
		self.root = root 
		super().__init__(root)


	def show_treeview_backup(self):

		self.scroll_x = Scrollbar(self.table_data_backup,orient=HORIZONTAL,command=self.table_data_backup.xview)
		self.scroll_y = Scrollbar(self.table_data_backup , orient=VERTICAL,command=self.table_data_backup.yview)
		self.table_data_backup.place(x=0,y=200,width=1176,height=310)

		self.table_data_backup.configure(xscrollcommand=self.scroll_x.set)
		self.scroll_x.pack(side=BOTTOM,fill=X)

		self.table_data_backup.configure(yscrollcommand=self.scroll_y.set)
		self.scroll_y.pack(side=LEFT,fill=Y)


	def select_data_backup(self):
		connection = sqlite3.connect(manager_Sqlite3("database_backup","Backup.db"))
		cursor = connection.cursor()

		cursor.execute(""" SELECT Backup, Backup_history FROM Backup""")
		rows_coulmns = cursor.fetchall()
		if len(rows_coulmns) !=0:
			self.table_data_backup.delete(*self.table_data_backup.get_children())

			for row in rows_coulmns :
				self.table_data_backup.insert('',END,value=row)

		connection.commit()
		connection.close()



