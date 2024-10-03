


from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image , ImageTk
from datetime import datetime
import os , sys , shutil
import sqlite3
import time
from threading import Thread

from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import *
from management_destination.management_exe import copy_resources_folder,manager_Sqlite3


class NodeDataAttendanceAndDeparture:
	def __init__(self,root):
		self.root = root
		self.root.geometry("1180x800+300+100")


		self.table_data = ttk.Treeview(self.root,
			columns = ('Email','Notes','date_ansraf','date_7dor','Name','time_ansraf','time_7dor','ID'))



		self.table_data['show'] = 'headings'
		self.table_data.heading('Email',text='البريد الإلكتروني')
		self.table_data.heading('Notes',text='ملاحضات')
		self.table_data.heading('date_ansraf',text='تاريخ الإنصراف')


		self.table_data.heading('date_7dor',text='تاريخ الحضور')
		self.table_data.heading('Name',text='إسم الموظف')
		self.table_data.heading('time_ansraf',text='وقت الإنصراف')
		self.table_data.heading('time_7dor',text='وقت الحضور')
		self.table_data.heading('ID',text='رقم الهوية')
		

		
		self.table_data.column('Email',width=220,anchor=CENTER)
		self.table_data.column('Notes',width=160,anchor=CENTER)
		self.table_data.column('date_ansraf',anchor=CENTER)
		self.table_data.column('date_7dor',anchor=CENTER)
		self.table_data.column('Name',anchor=CENTER)
		self.table_data.column('time_7dor',anchor=CENTER)
		self.table_data.column('time_ansraf',anchor=CENTER)

		self.table_data.column('ID',anchor=CENTER)





class TreeviewShowAttendanceAndDeparture(NodeDataAttendanceAndDeparture):
	def __init__(self,root):
		self.root = root
		super().__init__(root)

	
		self.var_email = StringVar()
		self.var_notes = StringVar()
		self.var_date_insraf = StringVar()
		self.var_date_7dor = StringVar()
		self.var_name = StringVar()
		self.var_time_insraf = StringVar()
		self.var_time_7dor = StringVar()
		self.var_id = StringVar()



	def ShowTreeview(self):
		""" The Function This is Show Treeview And Show ScroorBar In Window """
		self.scroll_x = Scrollbar(self.root,orient=HORIZONTAL,command=self.table_data.xview)
		self.scroll_y = Scrollbar(self.root , orient=VERTICAL,command=self.table_data.yview)


		self.table_data.place(x=21,y=535,width=1142,height=245)
		
		self.table_data.configure(xscrollcommand=self.scroll_x.set)
		self.scroll_x.pack(side=BOTTOM,fill=X)

		self.table_data.configure(yscrollcommand=self.scroll_y.set)
		self.scroll_y.pack(side=LEFT,fill=Y)



	def select_data_ttendance_departure(self):
		""" The function responsible for ,
		importing data from the database and displaying it in the tree """
		
		connection = sqlite3.connect(manager_Sqlite3("database_attendance_departure","DataBaseAttendanceDeparture.db"))
		cursor = connection.cursor()

		cursor.execute(""" SELECT Email  , Notes , date_ansraf , date_7dor , Name, time_ansraf , time_7dor ,ID FROM AttendanceDeparture""")

		rows_coulmns = cursor.fetchall()

		if len(rows_coulmns) !=0:
			self.table_data.delete(*self.table_data.get_children())

			
			for row in rows_coulmns :
				self.table_data.insert('',END,value=row)

		connection.commit()





			