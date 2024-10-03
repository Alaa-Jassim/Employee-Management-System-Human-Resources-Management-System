
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

class NodeData:
	""" The main class for creating the tree """
	def __init__(self,root):
		self.root = root
		self.root.geometry('1200x900+350+40')

		self.table_data = ttk.Treeview(self.root , 
			columns = ('Age','Submission_date','City','Section','Salary','Name','ID','Email','Image'))

		self.table_data['show'] = 'headings'
		self.table_data.heading('Image',text='الصورة')
		self.table_data.heading('Age',text='العمر')
		self.table_data.heading('Submission_date',text='تأريخ التسجيل')


		self.table_data.heading('City',text='المدينة')
		self.table_data.heading('Section',text='القسم')



		self.table_data.heading('Salary',text='الإجرة الشهرية')
		self.table_data.heading('Name',text='الإسم')
		self.table_data.heading('ID',text='رقم الهوية')
		self.table_data.heading('Email',text='البريد الإلكتروني')




		self.table_data.column('Image',width=220,anchor=CENTER)
		self.table_data.column('Age',width=60,anchor=CENTER)
		self.table_data.column('Submission_date',width=100,anchor=CENTER)
			

		self.table_data.column('City',width=190,anchor=CENTER)
		self.table_data.column('Section',width=190,anchor=CENTER)


		self.table_data.column('Salary',width=80,anchor=CENTER)
		self.table_data.column('Name',anchor=CENTER)
		self.table_data.column('ID',width=60,anchor=CENTER)
		self.table_data.column('Email',width=170,anchor=CENTER)

		


class TreeviewApp(NodeData):
	""" The class that is inherited from the main class and is the one for displaying data """
	def __init__(self,root):
		self.root = root 
		super().__init__(root)

		
	def show_treeview(self):

		self.scroll_x = Scrollbar(self.root,orient=HORIZONTAL,command=self.table_data.xview)
		self.scroll_y = Scrollbar(self.root , orient=VERTICAL,command=self.table_data.yview)
		self.table_data.place(x=19,y=708,width=1164,height=170)



		self.table_data.configure(xscrollcommand=self.scroll_x.set)
		self.scroll_x.pack(side=BOTTOM,fill=X)

		self.table_data.configure(yscrollcommand=self.scroll_y.set)
		self.scroll_y.pack(side=LEFT,fill=Y)



	def select_data(self):
		""" The function responsible for ,
		importing data from the database and displaying it in the tree """
		
		connection = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
		cursor = connection.cursor()

		cursor.execute(""" SELECT Age , DateRegistration , City , Section , Salary , Name , ID , Email , Image FROM Employees """)

		rows_coulmns = cursor.fetchall()
		if len(rows_coulmns) !=0:
			self.table_data.delete(*self.table_data.get_children())

			
			for row in rows_coulmns :
				self.table_data.insert('',END,value=row)

		connection.commit()







