

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image , ImageTk
from tkinter import filedialog
from datetime import datetime
import os , sys , shutil
import sqlite3
from threading import Thread
from list_employee.treeview_list_employee import TreeviewListEmployee
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 
from management_destination.management_exe import copy_resources_folder,manager_Sqlite3


class DataBaseListEmployee:
	def __init__(self,root):
		self.root = root


		self.var_id_list = StringVar()
		self.var_section_list = StringVar()
		self.var_name_list = StringVar()


		self.class_treeview = TreeviewListEmployee(self.root)
		self.class_treeview.ShowTreeview()
		self.run_func = Thread(target=self.class_treeview.select_data_list(),args=()).start()
		self.class_treeview.table_data_list.bind('<ButtonRelease-1>',self.get_cursor)


	def get_cursor(self,ev):
		try :
	
			self.cursor_row = self.class_treeview.table_data_list.focus()
			self.contents = self.class_treeview.table_data_list.item(self.cursor_row)
			self.row = self.contents['values']

			self.var_name_list.set(self.row[0]) ; self.var_section_list.set(self.row[1]) ; self.var_id_list.set(self.row[2]);
		except :
			pass



	def get_data_list(self):
	
		if self.var_id_list.get() == '':
			messagebox.showerror('خـطأ','لا يمكن ترك حقل إسم الموظف فارغاً' , parent=self.root)
		elif self.var_section_list.get() == '':
			messagebox.showerror('خـطأ','لا يمكن ترك حقل القسم  فارغا' , parent=self.root)

		elif self.var_name_list.get() == '':
			messagebox.showerror("خطأ","لا يمكن ترك حقل إسم الموظف فارغاً", parent=self.root)
		else :

			self.connection_data_list = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
			self.cursor_data_list = self.connection_data_list.cursor()

			self.cursor_data_list.execute("""SELECT Name , Section , ID  FROM Employees WHERE ID=?  """
				,(self.var_id_list.get(),))

			self.result_list = self.cursor_data_list.fetchall()
			if not self.result_list :
				messagebox.showerror("خطأ" , "ليست هناك نتائج بحث الرجاء إعادة المحاولة والتحقق من رقم الموظف" , parent=self.root)
			else :
				self.class_treeview.table_data_list.delete(*self.class_treeview.table_data_list.get_children())
				for self.row_date in self.result_list :
					self.class_treeview.table_data_list.insert('',END,value=self.row_date)
		

			self.connection_data_list.commit()



