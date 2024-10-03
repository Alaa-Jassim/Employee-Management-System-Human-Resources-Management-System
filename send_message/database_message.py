



from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from threading import Thread
from PIL import Image , ImageTk
import sqlite3
import smtplib, ssl
from email.message import EmailMessage
import urllib.request
from send_message.treeview_message import TreeviewMessageEmployee
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 
import os , sys , shutil 
from queue import Queue
import socket
import smtplib
from concurrent.futures import ThreadPoolExecutor
from management_destination.management_exe import manager_Sqlite3, manager_Images

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class DatabaseMessageEmployee:
	def __init__(self,root):
		self.root = root
		self.var_sent_email = StringVar()
		self.var_api_key = StringVar()
		self.var_mail_received = StringVar()
		self.var_message = StringVar()
		self.result_connection = list()
		self.result_message = list()
		self.variable_item = StringVar()


		self.create_database_message()


		self.class_treeview_message = TreeviewMessageEmployee(self.root)
		self.class_treeview_message.ShowTreeviewMessage()
		self.class_treeview_message.select_data_message()
		self.class_treeview_message.table_message.bind('<ButtonRelease-1>',self.get_cursor)

		self.class_treeview_message.table_message.bind("<Button-3>", self.on_right_click)

		self.run_func_select = Thread(target=self.class_treeview_message.select_data_message(), args=())
		self.run_func_select.start()


		self.result_internt = Thread(target=self.check_internet_connection , args=("https://www.google.com",self.result_connection))
		self.result_internt.start()

	
	def check_data_message_employee(self):
		
		if "".join(self.result_connection) == "Offline":
			self.message_info = messagebox.showerror("خطأ" ,"الرجاء التحقق من شبكة الإنترنت وإعادة المحاولة ..." , parent=self.root)


		if self.var_sent_email.get() == '':
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل البريد المرسل فارغا" , parent=self.root)

		elif self.var_api_key.get() == '':
			messagebox.showerror("خطأ" , "خطأ لا يمكن ترك حقل مفتاح الإرسال فارغاً" , parent=self.root)

		elif self.var_mail_received.get() == '':
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل البريد المستلم فارغا" , parent=self.root)

		elif self.var_message.get() == '':
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل الرسالة فارغاً" , parent=self.root)

	
		elif self.check_email_sent() == False :
			messagebox.showerror("خطأ" , "البريد الإلكتروني المرسل غير مسجل في قاعدة البيانات الأساسية" , parent=self.root)

		elif self.check_email_received() == False :
			messagebox.showerror("خطأ" , "البريد الإلكتروني المستلم غير مسجل في قاعدة البيانات الأساسية" , parent=self.root)

		elif self.check_sendgrid_api_key() == False:
			self.message_error_api_key = messagebox.showerror("خطأ", "الرجاء التحقق من صحة مفتاح الإرسال", parent=self.root)
		else:
			self.run_fucn_send_message =Thread(target=self.SentToGmail, args=(),).start()
			self.message_send_successfuly =  messagebox.showinfo("المعلومات صحيحة", "تم إرسال الرسالة بنجاح.", parent=self.root)

			self.message_save = messagebox.askquestion("المعلومات صحيحة", "هل توافقنا على تسجيل هذه البيانات في قاعدة البيانات؟", parent=self.root)
			if self.message_save == "yes":
				self.insert_data()
			#self.run_fucn_send_message =Thread(target=self.SentToGmail, args=(),).start()





	def check_email_exists(self):
		""" check email if Exists in Table Employee """
		self.connection_email_exists = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
		self.cursor_email_exists = self.connection_email_exists.cursor()

		self.cursor_email_exists.execute(""" SELECT * FROM Employees WHERE Email=?""",(self.var_sent_email.get(),))
		if self.cursor_email_exists.fetchone():
			return True 
		return False 

		self.connection_email_exists.commit()



	def create_database_message(self):
		self.connection_message = sqlite3.connect(manager_Sqlite3("database_send_message","DatabaseMessageEmployee.db"))
		self.cursor_message = self.connection_message.cursor()

		self.QUERY = """ CREATE TABLE IF NOT EXISTS MessageEmployee 
		(message TEXT NOT NULL , mail_received TEXT NOT NULL ,
		password TEXT NOT NULL , sent_email TEXT NOT NULL);"""

		self.cursor_message.execute(self.QUERY)

		self.connection_message.commit()



	def insert_data(self):

		self.connection_insert = sqlite3.connect(manager_Sqlite3("database_send_message","DatabaseMessageEmployee.db"))
		self.cursor_insert = self.connection_insert.cursor()


		self.QUERY_INSERT = ''

		self.cursor_insert.execute("""INSERT INTO MessageEmployee VALUES (?,?,?,?)""",
		(self.var_message.get() , self.var_mail_received.get() , self.var_api_key.get() , self.var_sent_email.get()))

		self.connection_insert.commit()
		self.run_func_select = Thread(target=self.class_treeview_message.select_data_message(), args=())
		self.run_func_select.start()

		self.connection_insert.close()



	def get_cursor(self,ev):
		try :

			self.cursor_row = self.class_treeview_message.table_message.focus()
			self.contents = self.class_treeview_message.table_message.item(self.cursor_row)
			self.row = self.contents['values']



			self.var_message.set(self.row[0]) ; self.var_mail_received.set(self.row[1]) 
			self.var_api_key.set(self.row[2]) ; self.var_sent_email.set(self.row[3])

		except :
			pass

	def check_email_sent(self):
		
		self.check_email = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
		self.cursor_email = self.check_email.cursor()

		self.cursor_email.execute(""" SELECT * FROM Employees WHERE Email=?""",(self.var_sent_email.get(),))
		if self.cursor_email.fetchone() :
			return True
		return False


		self.check_email.commit() 


	def check_email_received(self):
		self.check_received = sqlite3.connect(manager_Sqlite3("database_employees","DataBaseEmployees.db"))
		self.cursor_received = self.check_received.cursor()

		self.cursor_email.execute(""" SELECT * FROM Employees WHERE Email=?""",(self.var_mail_received.get(),))
		if self.cursor_email.fetchone() :
			return True
		return False

		self.check_received.commit()




	def check_internet_connection(self,url , result_connection):
		""" Check WI-Fi Internet """
		try :
			urllib.request.urlopen(url)
			self.result_connection.append("Online")
		except Exception :
			self.result_connection.append("Offline")


	def check_sendgrid_api_key(self):
		self.sg = SendGridAPIClient(self.var_api_key.get())
		self.response = self.sg.client.user.profile.get()

		if self.response.status_code == 200:
			return True 
		return False


	def SentToGmail(self):
		""" Send Message To Gmail """
		self.api_key = self.var_api_key.get()
		self.sender_email = self.var_sent_email.get()
		self.email_received = self.var_mail_received.get()
		self.message_email = self.var_message.get()


		self.message = Mail(
        	from_email=self.sender_email,
        	to_emails=self.email_received,
        	subject=f'Hello Mr.: {self.email_received}',
        	plain_text_content=self.message_email
    		)

		try:
			self.sg = SendGridAPIClient(self.api_key)
			self.response = self.sg.send(self.message)
			print(f"Email sent! Status code: {self.response.status_code}")
		
		except Exception as e:
			print(f"Error: {e}")




	def clean_data_message(self):
		self.var_message.set('') ; self.var_mail_received.set('') ;
		self.var_password.set('') ; self.var_sent_email.set('')


	def deleteAlldataMessage(self):
		self.connection_delete_msg = sqlite3.connect(manager_Sqlite3("database_send_message","DatabaseMessageEmployee.db"))
		self.cursor_delete_msg = self.connection_delete_msg.cursor()

		self.message_question = messagebox.askquestion("هل توافق على هذا الإجراء ؟" ,"سيتم حذف قاعدة البيانات بالكامل" , parent=self.root)
		if self.message_question == 'yes':
			self.cursor_delete_msg.execute("""DELETE FROM MessageEmployee """)
			self.class_treeview_message.table_message.delete(*self.class_treeview_message.table_message.get_children())

		for self.row in self.cursor_delete_msg.fetchall():
			self.class_treeview_message.table_message.insert('',END , value=self.row)



		self.connection_delete_msg.commit()
		self.connection_delete_msg.close()


	def slect_item(self):
		self.connection_select = sqlite3.connect(manager_Sqlite3("database_send_message","DatabaseMessageEmployee.db"))
		self.cursor_select = self.connection_select.cursor()

		self.cursor_select.execute("""SELECT message , mail_received ,password , sent_email FROM  MessageEmployee""")

		if self.cursor_select.fetchall():
			self.class_treeview_message.table_message.delete(*self.class_treeview_message.table_message.get_children())

			for self.row in self.cursor_select.fetchall() :
				self.class_treeview_message.table_message.insert('',END , value=self.row)


		self.connection_select.commit()





	def delete_item(self):
		self.connection_delete_item = sqlite3.connect(manager_Sqlite3("database_send_message","DatabaseMessageEmployee.db"))
		self.cursor_delete_item = self.connection_delete_item.cursor()

		self.cursor_delete_item.execute(""" SELECT * FROM MessageEmployee""")
		if not (self.cursor_delete_item.fetchall()):
			messagebox.showerror("خطأ","الرجاء قم بتحديد البيانات المراد حذفها" , parent=self.root)
		else:
			self.message_delete = messagebox.askquestion("هل توافقنا على هذا الإجراء؟" , "سيتم حذف البيانات المحددة من قاعدة البيانات" , parent=self.root)
			if self.message_delete == "yes":
				self.cursor_delete_item.execute(""" DELETE FROM MessageEmployee WHERE mail_received=? """,(self.var_mail_received.get(),))
				self.slect_item()

		self.connection_delete_item.commit()
		self.class_treeview_message.select_data_message()
		

	def on_right_click(self,event):
		self.item = self.class_treeview_message.table_message.identify_row(event.y_root)
		self.menu = Menu(self.class_treeview_message.table_message, tearoff=0)
		self.menu.add_command(label="حذف الرسالة المحددة", command=self.delete_item)
		self.menu.post(event.x_root, event.y_root)



