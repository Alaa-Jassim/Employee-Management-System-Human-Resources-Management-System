



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


class NodeTreeviewListEmployee:
	def __init__(self,root):
		self.root = root

		
		self.table_data_list = ttk.Treeview(self.root,
			columns = ('Name','Section','ID'))



		self.table_data_list['show'] = 'headings'
		self.table_data_list.heading('Name',text='إسم الموظف')
		self.table_data_list.heading('Section',text='القسم')
		self.table_data_list.heading('ID',text='الرقم الوظيفي')


		
		self.table_data_list.column('Name',width=220,anchor=CENTER)
		self.table_data_list.column('Section',width=160,anchor=CENTER)
		self.table_data_list.column('ID',anchor=CENTER)

		self.table_data_list.column('Name',anchor=CENTER)
		self.table_data_list.column('Section',anchor=CENTER)
		self.table_data_list.column('ID',anchor=CENTER)




class TreeviewListEmployee(NodeTreeviewListEmployee):
	def __init__(self,root):
		self.root = root
		super().__init__(root)



	def ShowTreeview(self):
		""" The Function This is Show Treeview And Show ScroorBar In Window """
		self.scroll_y = Scrollbar(self.root , orient=VERTICAL,command=self.table_data_list.yview)
		self.table_data_list.place(x=21,y=133,width=1143,height=445)


		self.table_data_list.configure(yscrollcommand=self.scroll_y.set)
		self.scroll_y.pack(side=LEFT,fill=Y)


	def select_data_list(self):
		""" The function responsible for ,
		importing data from the database and displaying it in the tree """
		

		connection = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
		cursor = connection.cursor()

		cursor.execute("""SELECT Name ,Section , ID FROM Employees """)

		rows_coulmns = cursor.fetchall()

		if (rows_coulmns):
			self.table_data_list.delete(*self.table_data_list.get_children())

			for row in rows_coulmns :
				self.table_data_list.insert('',END,value=row)

		connection.commit()





