




from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image , ImageTk
from datetime import datetime
import os , sys
from list_employee.database_list_employee import DataBaseListEmployee
from list_employee.treeview_list_employee import TreeviewListEmployee
from list_employee.save_data_list_employee import SaveDataListEmployee
import sqlite3
from tkinter import filedialog
import csv
import docx
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 
from management_destination.management_exe import manager_Images


class StyleListEmployee:
	def __init__(self,master):
		self.master = Toplevel()
		self.master.geometry("1180x600+300+100")
		self.master.resizable(width=False,height=False)
		self.master.configure(background='#EAF2F8')
		self.master.title("أقسام الموظفين")
		self.master.iconbitmap(manager_Images("images_list","sections_em.ico"))


		self.class_database = DataBaseListEmployee(self.master)
		self.class_treeview = TreeviewListEmployee(self.master)
		self.class_save_data_list_employee = SaveDataListEmployee(self.master)

	

		self.lable_title = Label(self.master,background='#E8E4FA',
								text="أقسام الموظفين",
								width=71,
								font=("Libre Baskerville, serif;",20))

		self.lable_title.place(x=20,y=4)



		self.frame_search_section = Frame(self.master ,background='#EBF5FB',
		relief=RIDGE , bd=2 , width=1143,height=90).place(x=20,y=43)

		self.add_label_id()
		self.add_label_section()
		self.add_label_name()
		self.add_buttin_show()



	def ShowTreeview(self):
		""" The Function This is Show Treeview And Show ScroorBar In Window """
		self.scroll_y = Scrollbar(self.root , orient=VERTICAL,command=self.table_data_salary.yview)
		self.table_data_salary.place(x=21,y=133,width=1143,height=445)


		self.table_data_salary.configure(yscrollcommand=self.scroll_y.set)
		self.scroll_y.pack(side=LEFT,fill=Y)







	def add_label_id(self):
		self.label_id = Label(self.master ,
		 					text="الرقم الوظيفي",
							font=("bold",20),
							background='#EBF5FB' ,
							width=8 )
		self.label_id.place(x=1020,y=63)
		self.entry_id = Entry(self.master , width=16 , font=('Bold Oblique',14),
			relief=RIDGE , bd=1,justify='center',textvariable=self.class_database.var_id_list).place(x=834,y=71)





	def add_label_section(self):
		self.label_section = Label(self.master ,
		 					text="القسم",
							font=("bold",20),
							background='#EBF5FB' ,
							width=8 )
		self.label_section.place(x=775,y=65)


		self.entry_sections = Entry(self.master , width=20 , font=('Bold Oblique',14),relief=RIDGE ,
		 bd=1,justify='center',textvariable=self.class_database.var_section_list).place(x=575,y=71)
		

	





	def add_label_name(self):
		self.label_name = Label(self.master ,
			 					text="إسم الموظف",
								font=("bold",20),
								background='#EBF5FB' ,
								width=8 )
		self.label_name.place(x=420,y=65)
		self.entry_name = Entry(self.master , width=20 , font=('Bold Oblique',14),
			relief=RIDGE , bd=1,justify='center',textvariable=self.class_database.var_name_list).place(x=185,y=71)





	def add_buttin_show(self):
		self.image_search = Image.open(manager_Images("images_list","sections_em.ico"))
		self.image_search = self.image_search.resize((35,35))
		self.insert_image_search = ImageTk.PhotoImage(self.image_search)

		self.button_show = Button(self.master , 
								text="عرض" , 
								background='#F7F7F9',
								width=80 , 
								height=30 ,
								font=('Bold Oblique',18),
								compound='left',padx=20,relief=FLAT , bd=1,
								image=self.insert_image_search,command=self.class_database.get_data_list
								)

		self.button_show.place(x=35,y=65)
