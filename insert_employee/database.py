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
import io
import time

from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 
from management_destination.management_exe import copy_resources_folder,manager_Sqlite3
from insert_employee.show_data import TreeviewApp
from attendance_departure.database_attendance import DataBaseAttendanceDeparture




class DataBase(Thread):
	def __init__(self,master):
		self.master = master
		super().__init__()

		self.image_employee = ""
		self.filename = ''
		self.var_age = StringVar()
		self.var_date_reg = StringVar()
		self.var_city = StringVar()
		self.var_section = StringVar()
		self.var_salary = StringVar()
		self.var_name = StringVar()
		self.var_id = StringVar()
		self.var_email = StringVar()
		self.variable_search_employee = StringVar()
		self.variable_delete_employee = StringVar()



		self.var_email = StringVar()
		self.var_notes = StringVar()
		self.var_date_insraf = StringVar()
		self.var_date_7dor = StringVar()
		self.var_name = StringVar()
		self.var_time_insraf = StringVar()
		self.var_time_7dor = StringVar()
		self.var_id = StringVar()

		self.create_database()
		self.class_treeview = TreeviewApp(self.master)
		self.class_treeview.show_treeview()
		self.class_treeview.table_data.bind('<ButtonRelease-1>',self.get_cursor)

		self.class_treeview.select_data()

	def addimage(self):
		""" Add Image Employee And Save In SQlite3 """
		try :
			self.filename = filedialog.askopenfilename(title='أختار الصورة',)
		
			with Image.open(self.filename) as self.employee_image :
				self.employee_image = self.employee_image.resize((170,160))
				self.insert_employee_image = ImageTk.PhotoImage(self.employee_image)

				self.label_insert_image = Label(self.master,image=self.insert_employee_image)
				self.label_insert_image.place(x=995, y=300)
		except Exception as error :
			pass
	


	
	def create_database(self):
		""" Create DataBase Employees """

		self.connection = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
		self.cursor = self.connection.cursor()


		self.cursor.execute(
				""" CREATE TABLE IF NOT EXISTS Employees
				(Age TEXT NOT NULL ,DateRegistration TEXT NOT NULL ,
				City TEXT NOT NULL , Section TEXT NOT NULL ,
				Salary TEXT NOT NULL , Name TEXT NOT NULL ,
				ID TEXT NOT NULL PRIMARY KEY , Email TEXT NOT NULL ,
				Image TEXT NOT NULL )

				"""
				)

		self.connection.commit()

		

	def check_data(self):
		""" The Function Check all Data """
		if not os.path.exists(self.filename):
			messagebox.showerror('خـطأ','يجب أختـيار صورة للموظـف' , parent=self.master)

		elif self.var_email.get() == '':
			messagebox.showerror('خـطأ','لا يمكن ترك حقل البريد الإلكتروني فارغاً' , parent=self.master)
		elif self.var_id.get() == '':
			messagebox.showerror('خطـأ','لا يمكن ترك حقل رقم الهوية فارغاً' , parent=self.master)

		elif self.var_name.get() == '':
			messagebox.showerror('خـطأ','لا يمكن ترك حقل الإسم فارغاً' , parent=self.master)
		elif self.var_salary.get() == '':
			messagebox.showerror("خطأ","لا يمكن ترك حقل  الإجرة الشهرية فارغاً" , parent=self.master)

		elif self.var_section.get() == '':
			messagebox.showerror('خطـأ','لا يمكن ترك حقل القسم فارغاً' , parent=self.master)

		elif self.var_city.get() == '':
			messagebox.showerror('خـطأ','لا يمكن ترك حقل المدينة فارغاً' , parent=self.master)

		elif self.var_date_reg.get() == '':
			messagebox.showerror('خطـأ','لا يمكن ترك حقل الإقامة الحالية فارغاً' , parent=self.master)

		elif self.var_age.get() == '':
			messagebox.showerror('خـطأ','لا يمكن ترك حقل السن فارغاً', parent=self.master)
		
		else:
			if self.check_employee_email() == False :
				messagebox.showerror('خطـأ','البريد الإلكتروني مسجل مسبقا', parent=self.master)

			elif self.check_employee_id() == False :
					messagebox.showerror('خطـأ','الرقم الوظيفي مسجل مسبقا' , parent=self.master)
			
			else:
				self.messageTrue = messagebox.askquestion('البيانات صحيحة','هل توفقنا على إضافة البيانات في قاعدة البيانات؟' , parent=self.master)
				if self.messageTrue == 'yes':
					self.insert_employee() ; self.remove_image_employee()
					


	def remove_image_employee(self):
		"""Remove Image from Frame Image Employee After Add New Employee """
		if os.path.exists(self.filename):
			self.label_insert_image.config(image=None)
		else:
			pass 

					

	def check_employee_id(self):
		self.connection_id = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
		self.cursor_id = self.connection_id.cursor()

		self.cursor_id.execute('SELECT * FROM Employees WHERE ID =? ',(self.var_id.get(),))
		if self.cursor_id.fetchall() :
				return False 
		return True

		self.connection_id.commit()




	def check_employee_email(self):
		self.connection_email = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
		self.cursor_email = self.connection_email.cursor()

		self.cursor_email.execute('SELECT * FROM Employees WHERE Email=?',(self.var_email.get(),))
		if self.cursor_email.fetchall() :
				return False 
		return True

		connection_email.commit()



	def insert_employee(self):
		""" Save Data Employee In SQlite3 """

		self.connection_data = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
		self.cursor_data = self.connection_data.cursor()
		
		self.cursor_data.execute(""" INSERT INTO Employees VALUES (?,?,?,?,?,?,?,?,?)""",
			(self.var_age.get(),self.var_date_reg.get(),self.var_city.get(),self.var_section.get(),self.var_salary.get(),self.var_name.get(),
				self.var_id.get(),self.var_email.get(),self.filename,))




		self.connection_data.commit()
		self.run_func = Thread(target=self.class_treeview.select_data(),args=()).start()
		self.clean_text()

		self.connection_data.close()

		



	def clean_text(self):
		""" The Function Clean Data From Text Box """
		self.var_age.set('') ; self.var_date_reg.set('') ; self.var_city.set('')
		self.var_section.set('') ; self.var_salary.set('') ; self.var_id.set('')
		self.var_email.set('') ; self.var_name.set('') ; self.filename = ''



	def get_cursor(self,ev):

		try :
			self.cursor_row = self.class_treeview.table_data.focus()
			self.contents = self.class_treeview.table_data.item(self.cursor_row)
			self.row = self.contents['values']



			self.var_age.set(self.row[0]) ; self.var_date_reg.set(self.row[1]) ; self.var_city.set(self.row[2]);
			self.var_section.set(self.row[3]) ; self.var_salary.set(self.row[4]) ; self.var_name.set(self.row[5]);
			self.var_id.set(self.row[6]) ; self.var_email.set(self.row[7]);

			self.filename = self.row[8] # The Image Employee

			self.image_user = Image.open(self.filename,mode="r")
			self.image_user = self.image_user.resize((170,160))

			self.img_show = ImageTk.PhotoImage(self.image_user)
			self.lb_user = Label(self.master,image=self.img_show)
			self.lb_user.place(x=995,y=302)
			

		except Exception as error :
			pass


	def update_data(self):
		""" The Function Is Update Data With Employee """

		self.connection_update = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
		self.cursor_update = self.connection_update.cursor()

		self.cursor_update.execute("""UPDATE Employees SET Age=? ,DateRegistration=? , City=?, Section=?,Salary=?,Name=?,Email=? ,Image=? WHERE ID=? """

			,(self.var_age.get(),self.var_date_reg.get(),self.var_city.get(),self.var_section.get(),self.var_salary.get(),self.var_name.get(),self.var_email.get(),self.filename,self.var_id.get()))

		self.cursor_update.execute("SELECT * FROM Employees")
		self.class_treeview.table_data.delete(*self.class_treeview.table_data.get_children())
		DataBaseAttendanceDeparture.update_employee_attendace(self.var_email,self.var_name,self.var_id)
		
		

		for self.row in self.cursor_update.fetchall():
			self.class_treeview.table_data.insert('',END,value=self.row)

		self.connection_update.commit()
		self.clean_text()
	

	

	def clean_data(self):
		""" The Function Clean Data From Text Box If Clicked To Button Clean Data"""
		self.var_age.set('') ; self.var_date_reg.set('') ; self.var_city.set('')
		self.var_section.set('') ; self.var_salary.set('') ; self.var_id.set('')
		self.var_email.set('') ; self.var_name.set('')

	def delete_data(self):
		""" Function Delete Al Data from SQlite3"""

		self.connection_delete = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
		self.cursor_delete = self.connection_delete.cursor()

		self.messageDeleteAll = messagebox.askquestion('هل توافق على هذا الإجراء','عند موافقتك سيتم حذف قاعدة البيانات بالكامل' , parent=self.master)
		if self.messageDeleteAll == 'yes':
			self.cursor_delete.execute('DELETE FROM Employees')
			self.class_treeview.table_data.delete(*self.class_treeview.table_data.get_children())
			DataBaseAttendanceDeparture.delete_employee_attendace(self.variable_delete_employee)

			for self.row in self.cursor_delete.fetchall() :
				self.class_treeview.table_data.insert('',END,value=self.row)

		self.connection_delete.commit()
		self.connection_delete.close()



	def search_employee(self):
		""" The Function Search Data Employees from DataBase """

		self.connection_search = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
		self.cursor_search = self.connection_search.cursor()

		self.cursor_search.execute('SELECT * FROM Employees WHERE ID =?',(self.variable_search_employee.get(),))
		self.result_search = self.cursor_search.fetchall()

		if not self.result_search:
			messagebox.showerror('خطأ لاتوجد نتائج بحث!','الجاء إعادة المحاولة والتأكد من رقم الموظف' , parent=self.master)
		else :
			self.class_treeview.table_data.delete(*self.class_treeview.table_data.get_children())

			for self.row in self.result_search :
				self.class_treeview.table_data.insert('',END,value=self.row)
		self.connection_search.commit()
		self.connection_search.close()


	def delete_employee(self):
		""" The Function Is Delete One Employee data from database And from table Treeview"""

		self.connection_delete_employee = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
		self.cursor_delete_employee = self.connection_delete_employee.cursor()

		self.cursor_delete_employee.execute('SELECT * FROM Employees WHERE ID =?',(self.variable_delete_employee.get(),))
		if not self.cursor_delete_employee.fetchall():
			messagebox.showerror('خطأ! رقم غير موجود','الرجاء التحقق من رقم الموظف وإعادة المحاولة', parent=self.master)
		else :
			self.message_employee_delete = messagebox.askquestion('هل توافق على هذا الإجراء ؟','هل توافق على هذا الإجراء ؟ سيتم حذف الموظف المحدد', parent=self.master)
			if self.message_employee_delete == 'yes':
				self.cursor_delete_employee.execute('DELETE  FROM Employees WHERE ID =?',(self.variable_delete_employee.get(),))
				
				DataBaseAttendanceDeparture.delete_employee_attendace(self.variable_delete_employee)
				

			
		self.connection_delete_employee.commit()
		self.run_func = Thread(target=self.class_treeview.select_data(),args=()).start()
		self.connection_delete_employee.close()




	def show_data(self):
		self.connection_show = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
		self.cursor_show = self.connection_show.cursor()

		self.cursor_show.execute('SELECT * FROM Employees')
		if self.cursor_show.fetchall():
			self.run_func = Thread(target=self.class_treeview.select_data(),args=()).start()

		self.connection_show.commit()
		self.connection_show.close()



	def chengae_add_employee(self, file_name):
		connection_data = sqlite3.connect(manager_section_add_employee(file_name))
		cursor_data = connection_data.cursor()
		
		cursor_data.execute(""" INSERT OR IGNORE INTO Employees VALUES (?,?,?,?,?,?,?,?,?)""",
			(self.var_age.get(),self.var_date_reg.get(),self.var_city.get(),self.var_section.get(),self.var_salary.get(),self.var_name.get(),
				self.var_id.get(),self.var_email.get(),self.filename,))




		connection_data.commit()
		connection_data.close()