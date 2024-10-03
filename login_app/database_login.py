

from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from datetime import datetime
from PIL import Image
import sqlite3
from PIL import Image , ImageTk
from tkinter import filedialog
from threading import Thread
import threading
from babel.dates import format_date, parse_date, get_day_names 
from babel.numbers import * 
import os , sys
import sqlite3
import re 
from management_destination.management_exe import copy_resources_folder,manager_Sqlite3

class DatabaseLogin:
	def __init__(self, root):
		self.root = root
		self.var_username = StringVar()
		self.var_password = StringVar()
		self.var_confirm_password = StringVar()

		self.create_table()


	def check_data_login(self):
		""" check all data if is correct or not correct """

		if (self.var_username.get()) == '' or (self.var_username.get()) == "المستخدم إسم" :
			messagebox.showerror("خطأ", "لا يمكن ترك حقل إسم المستخدم فارغاً", parent=self.root)

		elif (self.var_password.get()) == '' or (self.var_password.get()) == "المرور كلمة" :
			messagebox.showerror("خطأ", "لا يمكن ترك حقل كلمة المرور فارغاً", parent=self.root)

		elif (self.var_confirm_password.get()) == '' or (self.var_confirm_password.get()) == "المرور كلمة تأكيد" :
			messagebox.showerror("خطأ", "لا يمكن ترك حقل تأكيد كلمة المرور فارغاً", parent=self.root)

		elif (self.var_password.get()) != (self.var_confirm_password.get()) :
			messagebox.showerror("خطأ", "كلمة المرور غير متطابقة الرجاء إعادة المحاولة", parent=self.root)

		elif self.check_username_exists() == False :
			messagebox_user_exists = messagebox.showerror("خطأ", "إسم المستخدم مسجل مسبقاً, الرجاء إختيار إسم مستخدم آخر", parent=self.root)

		else:
			self.confirm_password_value = self.var_confirm_password.get()
			self.messagebox_successfuly = messagebox.askquestion("المعلومات صحيحة", 
				"هل توافق على حفظ هذه البيانات؟",
				parent=self.root)

			if self.messagebox_successfuly in ("yes","Yes"):
				self.insert_data()
				self.messagebox_save = messagebox.showinfo("تم بنجاح", "تم تسجيل البيانات بنجاح يمكنك الآن تسجيل الدخول", parent=self.root)

			else:
				self.messagebox_cancel = messagebox.showinfo("شكراً لك", "هل تريد أن تتراجع عن هذا الأمر؟", parent=self.root)

				if self.messagebox_cancel in ("ok","Ok"):
					self.messagebox_thanks = messagebox.showinfo("شكراً لك", "تم بنجاح يمكنك الآن إنشاء حساب بمعلومات جديدة", parent=self.root)
					self.message_restart = messagebox.showinfo("تم إنشاء الحساب بنجاح", "الرجاء أعد تشغيل التطبيق لكي تتتمكن من تسجيل الدخول", parent=self.root)



	def create_table(self):
		""" create table SQlite3  """
		self.connection_login = sqlite3.connect(manager_Sqlite3("database_login","database_login.db"))
		self.cursor_login = self.connection_login.cursor()

		self.SQL_TABLE = """CREATE TABLE IF NOT EXISTS Login 
		(Username TEXT NOT NULL ,
		 Password TEXT NOT NULL,
		 Confirm_Password TEXT NOT NULL)""";

		self.cursor_login.execute(self.SQL_TABLE)

	
		self.connection_login.commit()
		self.connection_login.close()
		

	


	def insert_data(self):
		""" insert data to table SQlite3 """
		self.connection_save = sqlite3.connect(manager_Sqlite3("database_login","database_login.db"))
		self.cursor_save = self.connection_save.cursor()

		self.SQL_QUERY_INSERT = """ INSERT INTO Login (Username, Password, Confirm_Password) VALUES (?,?,?)""";

		self.SQL_DATA = (self.var_username.get(),
						self.var_password.get(),
						self.confirm_password_value)

		self.cursor_save.execute(self.SQL_QUERY_INSERT,self.SQL_DATA)

		
		self.connection_save.commit()
		self.connection_save.close()





	def check_username_exists(self):
		""" This is a function check username in Table SQlite3 """
		''' 
		except sqlite3.OperationalError :
			pass 
		'''

		self.connection_exists_username = sqlite3.connect(manager_Sqlite3("database_login","database_login.db"))
		self.cursor_exists_username = self.connection_exists_username.cursor()

		self.SQL_QUERY_USERNAME = """ SELECT Username FROM Login WHERE Username =?""";

		self.cursor_exists_username.execute(self.SQL_QUERY_USERNAME,(self.var_username.get(),))
		if len(self.cursor_exists_username.fetchall()) >=1 :
			return False 
		return True 

		self.connection_exists_username.commit()
		self.connection_exists_username.close()


	

