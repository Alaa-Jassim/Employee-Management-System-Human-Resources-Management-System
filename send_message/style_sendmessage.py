
from tkinter import *
from tkinter import ttk
import sqlite3
import smtplib, ssl
from email.message import EmailMessage
from threading import Thread
from PIL import Image , ImageTk
from send_message.database_message import DatabaseMessageEmployee 
from send_message.treeview_message import TreeviewMessageEmployee
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 
import os 
from management_destination.management_exe import manager_Images


class StyleSendMessageEmployee:
	def __init__(self,master):
		self.master = Toplevel()
		self.master.geometry("1180x600+300+100")
		self.master.title("إرسال رسالة")
		self.master.iconbitmap(manager_Images("images_message","icon_app_message.ico"))
		self.master.resizable(width=False,height=False)


		self.class_database_message = DatabaseMessageEmployee(self.master)
	


		self.function_title_label = Thread(target=self.add_title_label(),args=())
		self.function_title_label.start()

		self.function_frame_info = Thread(target=self.add_frame_info(),args=())
		self.function_frame_info.start()

		self.function_send = Thread(target=self.add_label_email_send(),args=())
		self.function_send.start()



		self.function_recipient = Thread(target=self.add_label_email_recipient(),args=())
		self.function_recipient.start()

		self.function_api_key = Thread(target=self.add_label_api_key(),args=())
		self.function_api_key.start()



		self.function_message_password = Thread(target=self.add_label_message_recipient(),args=())
		self.function_message_password.start()

		self.function_button = Thread(target=self.add_button_send(),args=())
		self.function_button.start()
		


		self.function_delete = Thread(target=self.add_button_delete(),args=())
		self.function_delete.start()




	def add_title_label(self):
		""" Add Label Title Window Message Employee """
		self.lable_title = Label(self.master,background='#E8E4FA',
								text="إرسال رسالة عبر البريد الإلكتروني",
								width=71,
								font=("Libre Baskerville, serif;",20))

		self.lable_title.place(x=20,y=4)


	def add_frame_info(self):
		self.frame_info = LabelFrame(self.master,

			width=1144,height=160 , bg='#F9EBEA',relief=GROOVE)
		self.frame_info.place(x=20,y=45)



	def add_label_email_send(self):
		self.label_send = Label(self.master,
			text=("البريد المرسل") , font=("Libre Baskerville, serif;",18),
			background="#F9EBEA",width=10)

		self.label_send.place(x=1010,y=75)

		self.entry_send_email = Entry(self.master,
			width=33,font=('Bold Oblique',15),relief=RIDGE , bd=1,justify='center',textvariable=self.class_database_message.var_sent_email)
		self.entry_send_email.place(x=650,y=77)

		


	def add_label_email_recipient(self):
		self.label_recipient = Label(self.master,
			text=("البريد المستلم") , font=("Libre Baskerville, serif;",18),
			background="#F9EBEA",width=10)

		self.label_recipient.place(x=500,y=75)

		self.entry_recipient_email = Entry(self.master,
			width=33,font=('Bold Oblique',15),relief=RIDGE , bd=1,justify='center',
			textvariable=self.class_database_message.var_mail_received)
		self.entry_recipient_email.place(x=145,y=77)




	def add_label_api_key(self):
		self.label_api_key = Label(self.master,
			text=("مفتاح الإرسال") , font=("Libre Baskerville, serif;",18),
			background="#F9EBEA",width=10)

		self.label_api_key.place(x=1010,y=140)

		self.entry_api_key = Entry(self.master,
			width=33,font=('Bold Oblique',15),relief=RIDGE , bd=1,justify='center',
			textvariable=self.class_database_message.var_api_key)
		self.entry_api_key.place(x=650,y=142)




	def add_label_message_recipient(self):
		self.label_message_recipient = Label(self.master,
			text=("أكتب الرسالة") , font=("Libre Baskerville, serif;",18),
			background="#F9EBEA",width=10)
		self.label_message_recipient.place(x=500,y=142)



		self.entry_message_recipient= Entry(self.master,
			width=33,font=('Bold Oblique',15),relief=RIDGE , bd=1,justify='center',
			textvariable=self.class_database_message.var_message)
		self.entry_message_recipient.place(x=145,y=142)


	def add_button_send(self):
		self.image_send = Image.open(manager_Images("images_message","send_icon.png"))
		self.image_send = self.image_send.resize((30,30))
		self.insert_send_image = ImageTk.PhotoImage(self.image_send)

		self.button_send = Button(self.master,
			text="إرسال" ,background='#F7F7F9',
			width=65 ,height=30 ,
			font=('Bold Oblique',16),
			compound='left',padx=20,relief=FLAT , bd=1,
			image=self.insert_send_image,command=self.class_database_message.check_data_message_employee)

		self.button_send.place(x=26,y=71)



	def add_button_delete(self):
		self.image_delete = Image.open(manager_Images("images_message","delete_data.png"))
		self.image_delete = self.image_delete.resize((30,30))
		self.insert_delete_image = ImageTk.PhotoImage(self.image_delete)

		self.button_send = Button(self.master,
			text="حــذف" ,background='#F7F7F9',
			width=65 ,height=30 ,
			font=('Bold Oblique',16),
			compound='left',padx=20,relief=FLAT , bd=1,
			image=self.insert_delete_image,command=self.class_database_message.deleteAlldataMessage)

		self.button_send.place(x=26,y=135)






