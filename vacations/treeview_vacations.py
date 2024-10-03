

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


class NodeTreeviewVacations:
	def __init__(self,root):
		self.root = root
		self.table_vacations = ttk.Treeview(self.root,
			columns = ("coincidence_day" , "number_days_vacation" , "Section" , "Name",
				"date_coincidence" , "type_coincidence" , "ID" , "Email"))



		self.table_vacations['show'] = 'headings'
		self.table_vacations.heading('coincidence_day',text='المصادف يوم')
		self.table_vacations.heading('number_days_vacation',text='عدد أيام الإجازة')
		self.table_vacations.heading('Section',text='القسم الوظيفي')


		self.table_vacations.heading('Name',text='إسم الموظف')
		self.table_vacations.heading('date_coincidence',text='تأريخ الإجازة')
		self.table_vacations.heading('type_coincidence',text='نوع الإجازة')
		self.table_vacations.heading('ID',text='الرقم الوظيفي')
		self.table_vacations.heading('Email',text='البريد الإلكتروني')
		

		
		self.table_vacations.column('coincidence_day',width=220,anchor=CENTER)
		self.table_vacations.column('number_days_vacation',width=160,anchor=CENTER)
		self.table_vacations.column('Section',anchor=CENTER)
		self.table_vacations.column('Name',anchor=CENTER)
		self.table_vacations.column('date_coincidence',anchor=CENTER)
		self.table_vacations.column('type_coincidence',anchor=CENTER)
		self.table_vacations.column('ID',anchor=CENTER)
		self.table_vacations.column('Email',anchor=CENTER)


class TreeviewVacations(NodeTreeviewVacations):
	def __init__(self,root):
		self.root = root
		super().__init__(root)



	def ShowTreeview(self):
		""" The Function This is Show Treeview And Show ScroorBar In Window """
		self.scroll_x = Scrollbar(self.root,orient=HORIZONTAL,command=self.table_vacations.xview)
		self.scroll_y = Scrollbar(self.root , orient=VERTICAL,command=self.table_vacations.yview)


		self.table_vacations.place(x=21,y=476,width=1155,height=305)
		
		self.table_vacations.configure(xscrollcommand=self.scroll_x.set)
		self.scroll_x.pack(side=BOTTOM,fill=X)

		self.table_vacations.configure(yscrollcommand=self.scroll_y.set)
		self.scroll_y.pack(side=LEFT,fill=Y)


	
	def select_data_vacations(self):
		""" The function responsible for ,
		importing data from the database and displaying it in the tree """

		connection = sqlite3.connect(manager_Sqlite3("database_vacations","database_vacations.db"))
		cursor = connection.cursor()

		cursor.execute(""" SELECT coincidence_day  , number_days_vacation , Section , Name , date_coincidence, type_coincidence  ,ID , Email FROM VacationsEmployee""")

		rows_coulmns = cursor.fetchall()

		if len(rows_coulmns) !=0:

			self.table_vacations.delete(*self.table_vacations.get_children())

			
			for row in rows_coulmns :
				self.table_vacations.insert('',END,value=row)

		connection.commit()



