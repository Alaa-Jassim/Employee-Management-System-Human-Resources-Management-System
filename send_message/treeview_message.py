



from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import sqlite3
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 
import os 
from management_destination.management_exe import manager_Sqlite3

class NodeTreeviewMessageEmployee:
	def __init__(self,master):
		self.master = master
		self.table_message = ttk.Treeview(self.master, 
			columns=("mesage","mail_received","API_Key","sent_mail"))


		self.table_message['show'] = 'headings'
		self.table_message.heading('mesage',text='الرسالة المرسلة')
		self.table_message.heading('mail_received',text='البريد المستلم')
		self.table_message.heading('API_Key',text='مفتاح API')
		self.table_message.heading('sent_mail',text='البريد المرسل')

		self.table_message.column('mesage',width=220,anchor=CENTER)
		self.table_message.column('mail_received',width=160,anchor=CENTER)
		self.table_message.column('API_Key',anchor=CENTER)
		self.table_message.column('sent_mail',anchor=CENTER)


class TreeviewMessageEmployee(NodeTreeviewMessageEmployee):
	def __init__(self,root):
		self.root = root
		self.variable_item = str()
		super().__init__(root)



	def ShowTreeviewMessage(self):
		""" The Function This is Show Treeview And Show ScroorBar In Window """
		self.scroll_y = Scrollbar(self.root , orient=VERTICAL,command=self.table_message.yview)
		self.table_message.place(x=20,y=205,width=1143,height=370)


		self.table_message.configure(yscrollcommand=self.scroll_y.set)
		self.scroll_y.pack(side=LEFT,fill=Y)
		# self.table_message.bind("<Button-3>", self.on_right_click)


	def select_data_message(self):
		self.connection = sqlite3.connect(manager_Sqlite3("database_send_message","DatabaseMessageEmployee.db"))
		self.cursor = self.connection.cursor()

		self.cursor.execute("""SELECT message , mail_received ,password , sent_email FROM  MessageEmployee""")
		self.result_message = self.cursor.fetchall() 

		if self.result_message :

			self.table_message.delete(*self.table_message.get_children())

			for self.row in self.result_message :
				self.table_message.insert('',END , value=self.row)

		self.connection.commit()