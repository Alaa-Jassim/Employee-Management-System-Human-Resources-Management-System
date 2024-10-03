

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image , ImageTk
from datetime import datetime
import os , sys , shutil
import sqlite3
from threading import Thread
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 
from insert_employee.database import DataBase
from management_destination.management_exe import manager_Images

class Widgets:
	def __init__(self,master=None):
		self.master = master
		if self.master :
			self.run_window_insert_employee()

	def run_window_insert_employee(self):
		self.master.geometry('1200x900+350+40')
		self.master.resizable(width=False , height=False)
		self.master.iconbitmap(manager_Images("images_add_employee","title_app.ico"))
		self.master.title('إدارة شؤون الموظفين')

		self.class_database = DataBase(self.master)
	

		self.function_frame_title = Thread(target=self.add_frame_title(),args=(),)
		self.function_frame_title.start()

		


	def add_frame_title(self):
		
		self.title_frame = Frame(self.master , background='#E8E4FA' ,width=1165  , height=80)
		self.title_frame.place(x=18,y=4)

		
		self.title_app = Label(
			self.title_frame , background='#E8E4FA' ,
			width=30 , height=1 , 
			text='إضــافة موظــف',font=("Libre Baskerville, serif;",26))
		self.title_app.place(x=300,y=20)

		# ====================================================================================================================================
	

		self.add_search_frame()
		self.add_delete_frame()




	def add_search_frame(self):
			""" This function adds the search field for the employee """

			self.search_frame = Frame(
				self.master, width=1165 , height=80 , background='#d9ddf7',
				relief=SUNKEN , bd=2

				).place(x=18,y=88)



			self.label_search = Label(
				self.search_frame , text='الرجاء إدخال رقم التعريف الشخصي للموظف للبحث عنه بدقة',
				font=('Bold Oblique',18) , background='#d9ddf7'

				).place(x=675,y=113)
	# =======================================================================================================================================



	def add_delete_frame(self):
		""" This function adds the field to delete the employee from the employee """
		self.frame_delete =  Frame(
			self.master, width=1165 , height=80 , background='#E3E9EF',padx=10,pady=3,
			relief=RIDGE , bd=2

			).place(x=18,y=170)


		self.lable_delete = Label(
			self.frame_delete , text='الرجاء إدخال رقم التعريف الشخصي الخاص بك لتتمكن من حذف الموظف',
			font=('Bold Oblique',18) , background='#E3E9EF'

			).place(x=580,y=193)
	# =======================================================================================================================================



		

		# ============ Add Entry Search Employee =================================

		self.entry_employee_delete = Entry(
			self.master , background='#E6F2FC' , 
			width=26 , relief=SUNKEN , 
			bd=1 , justify='center',font=('Bold Oblique',18),
			textvariable=self.class_database.variable_delete_employee).place(x=220,y=192)
		# =========================================================================






		# ================= Add Enrty Delete Employee ==============================
		self.entry_employee_search = Entry(
		self.master , background='#E6F2FC' ,
		 width=33 , relief=SUNKEN , 
		 bd=1 , justify='center',
		 font=('Bold Oblique',18),
		 textvariable=self.class_database.variable_search_employee

		).place(x=200,y=110)

		# ===========================================================================






		# =============== Add Frame Information Data Employee =======================
		self.frame_information =  Frame(self.master, width=1165 , 
										height=350 ,background='#CCCCFF',
										padx=10,pady=3,
										relief=RIDGE , bd=2).place(x=18,y=250)
		# ===========================================================================







		# ================== Add Frame Buttons =====================================
		self.frame_buttons = Frame(
				self.master, width=1165 , 
				height=106 , background='#E9E0F6',
				padx=10,pady=3,
				relief=RIDGE , bd=2

				).place(x=18,y=600)
		# ==========================================================================






		""" Now Add Label Email And Add Entry Email Employee  """

		self.lable_email = Label(self.frame_information , text='البريد الإلكتروني'
							 ,font=('Bold Oblique',18) ,background='#CCCCFF'

							 ).place(x=820,y=291)


		self.entry_email = Entry(
			self.frame_information , width=22 ,font=('Bold Oblique',16) , relief=RAISED , bd=1 ,
			background='white',
			textvariable=self.class_database.var_email).place(x=538,y=292)

		# =============================================================================









	# 	""" Add Label ID And Add Entry ID Employee  """

		self.lable_id = Label(self.master , text='رقـم الهـوية'
							 ,font=('Bold Oblique',18) ,background='#CCCCFF'

							 ).place(x=850,y=360)

		self.entry_id = Entry(
			self.master , width=14 ,font=('Bold Oblique',16) , relief=RAISED , bd=1 ,
			background='white',justify='center',
			textvariable=self.class_database.var_id).place(x=640,y=360)
		# =============================================================================







	# 	""" Add Label Name And Add Entry Name Employee  """
		self.lable_name = Label(self.master , text='إسم الموظف'
							 ,font=('Bold Oblique',18) ,background='#CCCCFF'

							 ).place(x=850,y=433)


		self.entry_name = Entry(
			self.master , width=20 ,font=('Bold Oblique',16) , relief=RAISED , bd=1 ,
			background='white',
			textvariable=self.class_database.var_name).place(x=570,y=433)

		# =============================================================================









	# 	""" Add Label Salary And Add Entry Salary Employee  """
		self.label_salary = Label(self.master,text='الإجرة الشهرية',font=('Bold Oblique',18) ,background='#CCCCFF').place(x=845,y=510)


		self.entry_salary = Entry(
			self.master , width=15 ,font=('Bold Oblique',16) , relief=RAISED , bd=1 ,
			background='white',justify='center',
			textvariable=self.class_database.var_salary).place(x=633,y=510)
		# =============================================================================








	# 	""" Add Label Secton And Add Entry Section Employee  """
		self.lable_section = Label(self.master , text='الــقسم'
							 ,font=('Bold Oblique',18) ,background='#CCCCFF'

							 ).place(x=400,y=291)

		self.entry_section = Entry(
			self.master , width=22 ,font=('Bold Oblique',16) , relief=RAISED , bd=1 ,
			background='white',justify='center',
			textvariable=self.class_database.var_section).place(x=120,y=293)
		# =============================================================================









		""" Add Label City And Add Entry City Employee  """
		self.lable_city = Label(self.master , text='المــدينة'
							 ,font=('Bold Oblique',18) ,background='#CCCCFF'

							 ).place(x=400,y=360)

		self.entry_city = Entry(
			self.master , width=14 ,font=('Bold Oblique',16) , relief=RAISED , bd=1 ,
			background='white',justify='center',
			textvariable=self.class_database.var_city).place(x=216,y=360)
		# =============================================================================









		""" Add Label Currnet Data And Add Entry Currnet Data Employee  """
		self.lable_date = Label(self.master , text='تأريخ التسجيل'
							 ,font=('Bold Oblique',16) ,background='#CCCCFF'

							 ).place(x=370,y=433)

	

		self.year=datetime.datetime.now().year
		self.month=datetime.datetime.now().month
		self.day=datetime.datetime.now().day

		self.entry_date = DateEntry(self.master,selectmode='day',year=self.year,
			month=self.month,day=self.day,
			font=('Bold Oblique',16),
			justify='center',date_pattern="yyyy-mm-dd", foreground="black",
			headersforeground="black", selectforeground="black",width=18,
			textvariable=self.class_database.var_date_reg).place(x=110,y=433)
		# =============================================================================



		""" Add Label Age And Add Entry Age Employee  """
		self.lable_age = Label(self.master , text='الــعمر'
							 ,font=('Bold Oblique',16) ,background='#CCCCFF'

							 ).place(x=400,y=510)



		self.entry_age = Entry(
			self.master , width=16,
			font=('Bold Oblique',16) , relief=RAISED , 
			bd=1 ,background='white',justify='center',
			textvariable=self.class_database.var_age).place(x=170,y=510)
		# =============================================================================





	# 	""" ===================================== Now Create Buttons control DataBase =================================================================="""




		self.func_get_search = Thread(target=self.get_search(),args=())
		self.func_get_search.start()


		self.func_get_get_delete = Thread(target=self.get_delete(),args=())
		self.func_get_get_delete.start()



		self.func_insert = Thread(target=self.func_insert(),args=())
		self.func_insert.start()

		self.func_update = Thread(target=self.function_update(),args=())
		self.func_update.start()



		self.func_delete = Thread(target=self.func_delete(),args=(),)
		self.func_delete.start()



		self.func_empty_fields = Thread(target=self.func_empty_fields(),args=())
		self.func_empty_fields.start()


		self.func_show_data = Thread(target=self.func_show_data(),args=())
		self.func_show_data.start()



		self.add_image_employee = Thread(target=self.add_image_employee(),args=())
		self.add_image_employee.start()




	def get_search(self):
		self.image_search = Image.open(manager_Images("images_add_employee","search_data.png"))
		
		self.image_search = self.image_search.resize((35,35))
		self.insert_image_search = ImageTk.PhotoImage(self.image_search)


		self.button_search_employee = Button(
		self.master , background='#F7F7F9' , width=90 , height=30 , text='بــحث',font=('Bold Oblique',18) ,
		image=self.insert_image_search , compound='left',padx=20,relief=FLAT , bd=1,
		command=self.class_database.search_employee

		).place(x=40,y=106)




	def get_delete(self):
		self.delete_image = Image.open(manager_Images("images_add_employee","delete_employee.png")
)
		self.delete_image = self.delete_image.resize((35,35))
		self.insert_delete = ImageTk.PhotoImage(self.delete_image)


		self.button_delete_employee = Button(
			self.master , background='#F7F7F9' , width=120 , height=30 , text='حذف',font=('Bold Oblique',18) ,
			 padx=10,image=self.insert_delete , compound='left',relief=FLAT , bd=1,
			 command=self.class_database.delete_employee
			).place(x=40,y=188)




	def func_insert(self):
		''' create button insert data to sqlite3 '''
		self.image_insert = Image.open(manager_Images("images_add_employee","insert_data.png"))
		
		self.image_insert = self.image_insert.resize((30,30))
		self.image_save = ImageTk.PhotoImage(self.image_insert)

		#self.title_lable = Label(self.master , text='الــتحكم في بــيانات المــوظفين',fg='#ff3333',background='#aed5ef',font=('Bold Oblique',22)).place(x=1570,y=640)


		self.button_insert = Button(
			self.master , background='#F7F7F9' , width=145 , height=40 , text='إضــافة موظـف',font=('Bold Oblique',18),
			relief=FLAT , bd=1 ,image=self.image_save , compound='left',padx=20,
			command=self.class_database.check_data).place(x=976,y=630)



	def function_update(self):
		''' create button update data from sqlite3 '''

		self.image_update = Image.open(manager_Images("images_add_employee","update_data.png"))
	
		self.image_update = self.image_update.resize((36,36))
		self.insert_image_update = ImageTk.PhotoImage(self.image_update)

		self.button_update = Button(
			self.master , background='#F7F7F9' , width=145 , height=40 , text='تـحديث مــوظف',font=('Bold Oblique',18),
			relief=FLAT , bd=2 , image=self.insert_image_update,compound='left',padx=20,
			command=self.class_database.update_data

			).place(x=730,y=630)




	def func_delete(self):
		''' create button delete All data from sqlite3 '''
		self.image_delete = Image.open(manager_Images("images_add_employee","delete_data.png"))
		
		self.image_delete = self.image_delete.resize((36,36))
		self.insert_image_delete = ImageTk.PhotoImage(self.image_delete)

		self.button_delete = Button(
			self.master , background='#F7F7F9' ,width=145 , height=40 , text='حذف الموظفين',font=('Bold Oblique',18),
			relief=FLAT , bd=1 , image=self.insert_image_delete,compound='left',padx=20,
			command=self.class_database.delete_data


			).place(x=485,y=630) # empty fields


	def func_empty_fields(self):
		''' create button empty fields from data  '''
		self.image_empty = Image.open(manager_Images("images_add_employee","empty_data.png"))
		
		self.image_empty = self.image_empty.resize((36,36))
		self.insert_image_empty = ImageTk.PhotoImage(self.image_empty)

		self.button_delete = Button(
			self.master , background='#F7F7F9' , width=145 , height=40  , text='إفــراغ الحقول',font=('Bold Oblique',18),
			relief=FLAT , bd=1 ,image=self.insert_image_empty,
			command=self.class_database.clean_text
			,compound='left',padx=20).place(x=250,y=630)


	def func_show_data(self):
		''' create button Shoa All Data from sqlite3   '''
		self.image_show = Image.open(manager_Images("images_add_employee","show_data.png"))
		
		self.image_show = self.image_show.resize((30,30))
		self.insert_image_show = ImageTk.PhotoImage(self.image_show)

		self.button_delete = Button(
			self.master , background='#F7F7F9' , width=145 , height=40 , text='عــرض البيانات',font=('Bold Oblique',18),
			relief=FLAT , bd=1 , image=self.insert_image_show,compound='left',padx=20,
			command=self.class_database.show_data
			).place(x=30,y=630)




	def add_image_employee(self):
		self.image_ = Image.open(manager_Images("images_add_employee","image_empoyee.jpg"))
		
		self.image_ = self.image_.resize((170,160))
		self.insert_image = ImageTk.PhotoImage(self.image_)

		self.label_image = Label(self.master,image=self.insert_image).place(x=995,y=300)


		self.image_opne = Image.open(manager_Images("images_add_employee","open_file.png"))
		
		self.image_opne = self.image_opne.resize((30,30))
		self.insert_image_open = ImageTk.PhotoImage(self.image_opne)



		self.button_choice = Button(self.master , text='اختيار ملف',font=('Bold Oblique',18),
			background="#F7F7F9",
			relief=GROOVE,bd=2,
			width=130,height=30, image=self.insert_image_open , compound='left',
			padx=20 ,command=self.class_database.addimage).place(x=995,y=470)


