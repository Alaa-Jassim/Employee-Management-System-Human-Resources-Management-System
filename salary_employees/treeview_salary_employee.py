




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


class NodeTreeviewSalaryEmployee:
	def __init__(self,root):
		self.root = root
		self.table_data_salary = ttk.Treeview(self.root,
			columns = ('Name','Email','Section','Salary','ID'))


		self.table_data_salary['show'] = 'headings'
		self.table_data_salary.heading('Name',text='إسم الموظف')
		self.table_data_salary.heading('Email',text='البريد الإلكتروني')
		self.table_data_salary.heading('Section',text='القسم')
		self.table_data_salary.heading('Salary',text='الإجرة الشهرية')
		self.table_data_salary.heading('ID',text='الرقم الوظيفي')



		self.table_data_salary.column('Name',width=220,anchor=CENTER)
		self.table_data_salary.column('Email',width=160,anchor=CENTER)
		self.table_data_salary.column('Section',anchor=CENTER)

		self.table_data_salary.column('Salary',anchor=CENTER)
		self.table_data_salary.column('ID',anchor=CENTER)


class TreeviewSalaryEmployee(NodeTreeviewSalaryEmployee):
	def __init__(self,root):
		self.root = root
		super().__init__(root)


	def ShowTreeview(self):
		""" The Function This is Show Treeview And Show ScroorBar In Window """
		self.scroll_y = Scrollbar(self.root , orient=VERTICAL,command=self.table_data_salary.yview)
		self.table_data_salary.place(x=21,y=133,width=1143,height=445)


		self.table_data_salary.configure(yscrollcommand=self.scroll_y.set)
		self.scroll_y.pack(side=LEFT,fill=Y)



	def select_data_list(self):
		""" The function responsible for ,
		importing data from the database and displaying it in the tree """

		connection = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
		cursor = connection.cursor()

		cursor.execute("""SELECT Name ,Email , Section , Salary , ID FROM Employees """)

		rows_coulmns = cursor.fetchall()

		if (rows_coulmns):
			self.table_data_salary.delete(*self.table_data_salary.get_children())

			for row in rows_coulmns :
				self.table_data_salary.insert('',END,value=row)

		connection.commit()

