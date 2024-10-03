

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image , ImageTk
from datetime import datetime
import os , sys
import docx
from datetime import datetime
import os , sys , shutil
import sqlite3
from threading import Thread
from tkinter import filedialog
from salary_employees.database_salary import DatabaseSalaryEmployees
from salary_employees.save_data_salary_employee import SaveDataSalaryEmployee
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 
from management_destination.management_exe import manager_Images


class StyleSalaryEmployee:
	def __init__(self,master):
		self.master = Toplevel()
		self.master.geometry("1180x600+300+100")
		self.master.resizable(width=False,height=False)
		self.master.configure(background='#EAF2F8')
		self.master.title("رواتب الموظفين")
		self.master.iconbitmap(manager_Images("images_salary","icon_app.ico"))


		self.lable_title = Label(self.master,background='#E8E4FA',
								text="رواتب الموظفين",
								width=71,
								font=("Libre Baskerville, serif;",20))

		self.lable_title.place(x=20,y=4)





		self.class_database_salary = DatabaseSalaryEmployees(self.master)
		self.class_save_data_salary_employee = SaveDataSalaryEmployee(self.master)




		self.frame_search_salary = Frame(self.master ,background='#d9ddf7',
		relief=RIDGE , bd=2 , width=1143,height=90).place(x=20,y=43)

		self.add_label_search_salary()
		self.add_button_salary()



	def add_label_search_salary(self):

		self.label_salary = Label(self.master,
			text="إدخل الرقم الوظيفي أو البريد الإلكتروني للبحث" ,
			width=28,
			font=("Libre Baskerville, serif;",19),background='#d9ddf7')

		self.label_salary.place(x=734,y=69)


		self.entry_name_or_id = Entry(self.master , width=46 , font=('Bold Oblique',14),relief=RIDGE ,
		 bd=1,justify='center',textvariable=self.class_database_salary.var_email_or_id_salary).place(x=220,y=71)
		




	def add_button_salary(self):
		self.image_salary = Image.open(manager_Images("images_salary","salary_icon.png"))
		self.image_salary = self.image_salary.resize((35,35))
		self.insert_image_salary = ImageTk.PhotoImage(self.image_salary)

		self.button_show = Button(self.master , 
								text="عرض" , 
								background='#F7F7F9',
								width=100 , 
								height=33 ,
								font=('Bold Oblique',18),
								compound='left',padx=20,relief=FLAT , bd=1,
								image=self.insert_image_salary,command=self.class_database_salary.get_data_salary
								)

		self.button_show.place(x=40,y=63)

