



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
from attendance_departure.treeview_attendance_departure import TreeviewShowAttendanceAndDeparture
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 
from attendance_departure.save_data_attendance_departure import SaveDataAttendanceDeparture
from management_destination.management_exe import copy_resources_folder,manager_Sqlite3


class DataBaseAttendanceDeparture():
	def __init__(self,master):
		self.master = master
		self.var_email = StringVar()
		self.var_notes = StringVar()
		self.var_date_insraf = StringVar()
		self.var_date_7dor = StringVar()
		self.var_name = StringVar()
		self.var_time_insraf = StringVar()
		self.var_time_7dor = StringVar()
		self.var_id = StringVar()

		self.variable_search_employee = StringVar()
		self.variable_delete_employee = StringVar()

		self.filter_next = StringVar()
		self.filter_last = StringVar()

		self.date_employee = str(datetime.datetime.now().date())

		self.class_save_data = SaveDataAttendanceDeparture(self.master)



		self.create_database()

		self.class_treeview = TreeviewShowAttendanceAndDeparture(self.master)
		self.class_treeview.ShowTreeview()

		self.class_treeview.table_data.bind('<ButtonRelease-1>',self.get_cursor)
		
		self.run_func = Thread(target=self.class_treeview.select_data_ttendance_departure(),args=()).start()
		

	def create_database(self):
		""" Create DataBase Attendance And Departure """

		self.connection = sqlite3.connect(manager_Sqlite3("database_attendance_departure","DataBaseAttendanceDeparture.db"))
		self.cursor = self.connection.cursor()




		self.cursor.execute(
				""" CREATE TABLE IF NOT EXISTS AttendanceDeparture
				(Email  ,Notes , date_ansraf TEXT NOT NULL ,date_7dor TEXT NOT NULL ,
				Name TEXT NOT NULL , time_ansraf TEXT NOT NULL ,
				time_7dor TEXT NOT NULL , ID TEXT NOT NULL , DateTimeEmployee TEXT NOT NULL)

				"""
				)


		self.connection.commit()
		self.connection.close()


	def check_data_attendance(self):
		""" Check The Data Of employees """
		if self.var_email.get() == '':
			messagebox.showerror("خطأ","لا يمكن ترك حقل البريد الإلكتروني فارغاً" , parent=self.master)


		elif self.var_notes.get() == '':
			messagebox.showerror("خطأ","لا يمكن ترك حقل الملاحضات فارغاَ" , parent=self.master)


		elif self.var_date_insraf.get() == '':
			messagebox.showerror('خطـأ','لا يمكن ترك حقل تاريخ الانصراف فارغاً' , parent=self.master)


		elif self.var_date_7dor.get() == '':
			messagebox.showerror('خـطأ','لا يمكن ترك حقل تاريخ الحضور فارغاً' , parent=self.master)


		elif self.var_name.get() == '':
			messagebox.showerror("خطأ","لا يمكن ترك حقل إسم الموظف فارغاً" , parent=self.master)



		elif self.var_time_insraf.get() == '':
			messagebox.showerror("خطأ","لا يمكن ترك حقل وقت الانصراف فارغاً", parent=self.master)

		elif self.var_time_7dor.get() == '':
			messagebox.showerror('خطـأ','لا يمكن ترك حقل وقت الحضور فارغاً', parent=self.master)



		elif self.var_id.get() == '':
			messagebox.showerror('خـطأ','لا يمكن ترك حقل إسم الموظف فارغاً', parent=self.master)

		else :
			if self.check_employee_email() == False :
				messagebox.showerror('خطـأ','البريد الإلكتروني مسجل مسبقا', parent=self.master)

			elif self.check_employee_id() == False :
				messagebox.showerror('خطـأ','الرقم الوظيفي مسجل مسبقا', parent=self.master)
			
			elif self.check_email_exists() == False:
				messagebox.showerror("خطأ",
						 "لا يوجد موظف يحمل هذا البريد الإلكتروني في قاعدة البيانات الأساسية",
						 parent=self.master)
			
			elif self.check_id_exists() == False:
				messagebox.showerror("خطأ",
						 "لا يوجد موظف يحمل هذا الرقم الوظيفي في قاعدة البيانات الأساسية",
						 parent=self.master)

			else :
				self.messageTrue = messagebox.askquestion('البيانات صحيحة','هل توفقنا على إضافة البيانات في قاعدة البيانات؟', parent=self.master)
				if self.messageTrue == 'yes':
					self.insert_attendance_departure()
	

	def check_email_exists(self):
		"""check email if exists in Table Employees"""
		self.connection_email_exists = sqlite3.connect(manager_Sqlite3("database_attendance_departure","DataBaseAttendanceDeparture.db"))
		self.cursor_email_exists = self.connection_email_exists.cursor()

		self.cursor_email_exists.execute("""SELECT * FROM Employees WHERE Email=?""",(self.var_email.get(),))

		if self.cursor_email_exists.fetchall():
			return True 
		return False 
	
		self.connection_email_exists.commit()
	


	def check_id_exists(self):
		"""check ID if exists in Table Employees"""
		self.connection_id_exists = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
		self.curosr_id_exists = self.connection_id_exists.cursor()

		self.curosr_id_exists.execute("""SELECT * FROM Employees WHERE ID=?""",(self.var_id.get(),))

		if self.curosr_id_exists.fetchall():
			return True 
		return False 
	
		self.connection_id_exists.commit()
			


	
	def check_employee_id(self):
		self.connection_id = sqlite3.connect(manager_Sqlite3("database_attendance_departure","DataBaseAttendanceDeparture.db"))
		self.cursor_id = self.connection_id.cursor()

		self.cursor_id.execute('SELECT * FROM AttendanceDeparture WHERE ID =? ',(self.var_id.get(),))
		if self.cursor_id.fetchall() :
				return False 
		return True

		self.connection_id.commit()




	def check_employee_email(self):
		self.connection_email = sqlite3.connect(manager_Sqlite3("database_attendance_departure","DataBaseAttendanceDeparture.db"))
		self.cursor_email = self.connection_email.cursor()

		self.cursor_email.execute('SELECT * FROM AttendanceDeparture WHERE Email=?',(self.var_email.get(),))
		if self.cursor_email.fetchall() :
				return False 
		return True

		connection_email.commit()







	def insert_attendance_departure(self):
		""" Save Data Employee In SQlite3 """

		self.connection_data = sqlite3.connect(manager_Sqlite3("database_attendance_departure","DataBaseAttendanceDeparture.db"))
		self.cursor_data = self.connection_data.cursor()

	

		self.cursor_data.execute(""" INSERT INTO AttendanceDeparture VALUES (?,?,?,?,?,?,?,?,?)""",
			(self.var_email.get() , self.var_notes.get(),self.var_date_insraf.get(),self.var_date_7dor.get(),self.var_name.get(),self.var_time_insraf.get()
				,self.var_time_7dor.get(),self.var_id.get(),self.date_employee))



		self.connection_data.commit()
		self.run_func = Thread(target=self.class_treeview.select_data_ttendance_departure(),args=()).start()
		self.clean_text()
		self.connection_data.close()











	def get_cursor(self,ev):

		try :
			self.cursor_row = self.class_treeview.table_data.focus()
			self.contents = self.class_treeview.table_data.item(self.cursor_row)
			self.row = self.contents['values']



			self.var_email.set(self.row[0]) ; self.var_notes.set(self.row[1]) ; self.var_date_insraf.set(self.row[2]);
			self.var_date_7dor.set(self.row[3]) ; self.var_name.set(self.row[4]) ; self.var_time_insraf.set(self.row[5]);
			self.var_time_7dor.set(self.row[6]) ; self.var_id.set(self.row[7]);

			self.filename = self.row[8] # The Image Employee
			self.image_user = Image.open(self.filename,mode="r")
			self.image_user = self.image_user.resize((170,160))

			self.img_show = ImageTk.PhotoImage(self.image_user)
			self.lb_user = Label(self.master,image=self.img_show)
			self.lb_user.place(x=995,y=302)
			

		except Exception as error :
			pass


	def update_data(self):
		""" The Function Is Update Data AttendanceDeparture """
		self.connection_update = sqlite3.connect(manager_Sqlite3("database_attendance_departure","DataBaseAttendanceDeparture.db"))
		self.cursor_update = self.connection_update.cursor()


		self.cursor_update.execute("SELECT Email, ID FROM AttendanceDeparture WHERE ID = ?", (self.var_id.get(),))
		current_data = self.cursor_update.fetchone()

		if current_data:
			current_email, current_id = current_data

			if (self.var_email.get() == current_email and self.var_id.get() == current_id):
				self.SQL_QUERY_UPDATE = """ 

				UPDATE AttendanceDeparture
				SET Notes = ?,
				date_ansraf = ?,
				date_7dor = ?,
				Name = ?,
				time_ansraf = ?,
				time_7dor = ?
				WHERE ID = ? AND Email = ?"""

				self.DATA_EMPLOYEE = (
					self.var_notes.get(),
					self.var_date_insraf.get(),
					self.var_date_7dor.get(),

					self.var_name.get(),
					self.var_time_insraf.get(),
					self.var_time_7dor.get(),
					self.var_id.get(),
					self.var_email.get())

				self.cursor_update.execute(self.SQL_QUERY_UPDATE, self.DATA_EMPLOYEE)
				self.connection_update.commit()
				self.message_update = messagebox.askquestion("البيانات صحيحة" , "تم تحديث البيانات", parent=self.master)
				self.run_func = Thread(target=self.class_treeview.select_data_ttendance_departure(),args=()).start()
			else:
				self.message_error_one = messagebox.showerror("خطأ" , "لا يمكن تغيير البريد الإلكتروني أو رقم الموظف",parent=self.master)
		else:
			self.message_error_two = messagebox.showerror("خطأ" , "لم يتم العثور على الموظف المحدد",parent=self.master)
		self.connection_update.close()
		self.clean_text()


	
	def clean_text(self):
		""" The Function Clean Data From Text Box """
		self.var_email.set('') ; self.var_notes.set('') ; self.var_date_insraf.set('')
		self.var_date_7dor.set('') ; self.var_name.set('') ; self.var_time_insraf.set('')
		self.var_time_7dor.set('') ; self.var_id.set('') 



	def delete_data(self):
		""" Function Delete Al Data from Table AttendanceDeparture"""

		self.connection_delete = sqlite3.connect(manager_Sqlite3("database_attendance_departure","DataBaseAttendanceDeparture.db"))
		self.cursor_delete = self.connection_delete.cursor()

		self.messageDeleteAll = messagebox.askquestion('هل توافق على هذا الإجراء','عند موافقتك سيتم حذف قاعدة البيانات بالكامل', parent=self.master)
		if self.messageDeleteAll == 'yes':
			self.cursor_delete.execute('DELETE FROM AttendanceDeparture')
			self.class_treeview.table_data.delete(*self.class_treeview.table_data.get_children())

			for self.row in self.cursor_delete.fetchall() :
				self.class_treeview.table_data.insert('',END,value=self.row)

		self.connection_delete.commit()
		self.connection_delete.close()





	def search_employee(self):
		""" The Function Search Data  from Table AttendanceDeparture """

		self.connection_search = sqlite3.connect(manager_Sqlite3("database_attendance_departure","DataBaseAttendanceDeparture.db"))
		self.cursor_search = self.connection_search.cursor()

		self.cursor_search.execute('SELECT * FROM AttendanceDeparture WHERE ID =?',(self.variable_search_employee.get(),))
		self.result_search = self.cursor_search.fetchall()

		if not self.result_search:
			messagebox.showerror("خطا" , "ليست هناك نتائج بحث الرجاء إعادة المحاولة والتحقق من رقم الموظف"  , parent=self.master)
		else :
			self.cursor_search.execute('SELECT * FROM AttendanceDeparture WHERE ID =?',(self.variable_search_employee.get(),))
			self.class_treeview.table_data.delete(*self.class_treeview.table_data.get_children())

			for self.row in self.result_search :
				self.class_treeview.table_data.insert('',END,value=self.row)
		self.connection_search.commit()
		self.connection_search.close()


	def clean_data(self):
		""" The Function Clean Data From Text Box Table AttendanceDeparture"""
		self.var_email.set('') ; self.var_notes.set('') ; self.var_date_insraf.set('')
		self.var_date_7dor.set('') ; self.var_name.set('') ; self.var_time_insraf.set('')
		self.var_time_7dor.set('') ; self.var_id.set('')



	def show_data(self):
		self.connection_show = sqlite3.connect(manager_Sqlite3("database_attendance_departure","DataBaseAttendanceDeparture.db"))
		self.cursor_show = self.connection_show.cursor()

		self.cursor_show.execute('SELECT * FROM AttendanceDeparture')
		if self.cursor_show.fetchall():
			self.run_func = Thread(target=self.class_treeview.select_data_ttendance_departure(),args=()).start()

		self.connection_show.commit()
		self.connection_show.close() 


	def filters_data_employee(self):
		self.connection_filter = sqlite3.connect(manager_Sqlite3("database_attendance_departure","DataBaseAttendanceDeparture.db"))
		self.cursor_filter = self.connection_filter.cursor()


		self.cursor_filter.execute(""" SELECT Email , Notes , date_ansraf ,
									date_7dor , Name , time_ansraf , time_7dor ,
									ID FROM AttendanceDeparture WHERE DateTimeEmployee
									BETWEEN ? AND ?"""

									,(self.filter_next.get(),self.filter_last.get()))

		self.result_data = (self.cursor_filter.fetchall())
		if not self.result_data :
			messagebox.showerror("خطأ" , "ليست هناك نتائج بحث الرجاء إعادة المحاولة" , parent=self.master)

		self.class_treeview.table_data.delete(*self.class_treeview.table_data.get_children())
		for self.i in self.result_data :
			self.class_treeview.table_data.insert('',END,value=self.i)

		self.connection_filter.commit()
		




	@staticmethod
	def delete_employee_attendace(variable_delete_employee):
		""" Delete One Employee From Table Attendance And Departure """
	
		connection_delete = sqlite3.connect(manager_Sqlite3("database_attendance_departure","DataBaseAttendanceDeparture.db"))
		cursor_delete = connection_delete.cursor()


		cursor_delete.execute('DELETE  FROM AttendanceDeparture WHERE ID =?',(variable_delete_employee.get(),))

		connection_delete.commit()
		connection_delete.commit()



	@staticmethod
	def update_employee_attendace(var_email ,var_name , var_id):
		""" The Function Is Update Data With Employee """

		connection_update = sqlite3.connect(manager_Sqlite3("database_attendance_departure","DataBaseAttendanceDeparture.db"))
		cursor_update = connection_update.cursor()

		cursor_update.execute("SELECT Email , Notes , date_ansraf , date_7dor , Name , time_ansraf , time_7dor ,ID FROM AttendanceDeparture")
		

		
		for (value_email , value_notes ,value_date_insraf , value_date_7dor ,value_name  , value_date_insraf ,value_time_7dor , valeu_id) in cursor_update.fetchall():
			
			cursor_update.execute("""UPDATE AttendanceDeparture SET Email=? ,Notes=? , date_ansraf=?, date_7dor=?,Name=?,time_ansraf=? ,time_7dor=? WHERE ID=? """
				,(var_email.get() , value_notes ,value_date_insraf , value_date_7dor ,var_name.get()  , value_date_insraf ,value_time_7dor , var_id.get()))


		connection_update.commit()
		
		
