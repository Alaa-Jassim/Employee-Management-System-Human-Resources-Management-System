

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
from salary_employees.treeview_salary_employee import TreeviewSalaryEmployee
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 
from management_destination.management_exe import copy_resources_folder, manager_Sqlite3

class DatabaseSalaryEmployees:
	def __init__(self,root):
		self.root = root
		self.var_email_or_id_salary = StringVar()
		self.var_id_salary = StringVar()



		self.class_treeview_salary = TreeviewSalaryEmployee(self.root)
		self.class_treeview_salary.ShowTreeview()
		self.class_treeview_salary.select_data_list()


	def get_data_salary(self):
		if self.var_email_or_id_salary.get() == '':
			messagebox.showerror('خـطأ','لا يمكن ترك الحقل فارغا' , parent=self.root)
		else :
			self.connection_data_salary = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
			self.cursor_data_salary = self.connection_data_salary.cursor()

			self.cursor_data_salary.execute("""SELECT Name , Email , Section , Salary , ID  FROM Employees WHERE ID=? """
				,(self.var_email_or_id_salary.get(),))

			self.result_list = self.cursor_data_salary.fetchall()
			if not self.result_list :
				messagebox.showerror("خطأ" , "ليست هناك نتائج بحث الرجاء إعادة المحاولة والتحقق من رقم الموظف" , parent=self.root)
			else :
				self.class_treeview_salary.table_data_salary.delete(*self.class_treeview_salary.table_data_salary.get_children())
				for self.row_date in self.result_list :
					self.class_treeview_salary.table_data_salary.insert('',END,value=self.row_date)
		
			self.connection_data_salary.commit()


