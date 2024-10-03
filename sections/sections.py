

from tkinter import *
from tkinter import filedialog
import csv
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image, ImageTk
from datetime import datetime
from threading import Thread
from attendance_departure.attendance_departure import AttendanceAndDeparture
from list_employee.style_list_employee import StyleListEmployee
from salary_employees.style_salary_employees import StyleSalaryEmployee
from send_message.style_sendmessage import StyleSendMessageEmployee
from insert_employee.save_data_employee import SaveDataInsertEmployee
from help.style_help import Help
from whoarewe.whoarewe import WhoAreWe
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 
from vacations.style_vacations import StyleVacations
import os, sys, shutil
import sqlite3
import time
from tkinter import filedialog
import csv
import docx
from setting.style_setting import StyleSettingApllication
from backup.backup import StyleBackUp


class Sections():
	def __init__(self, master=None, main_app=None):
		self.master = master
		self.main_app = main_app
		self.main_menubar = Menu(self.master,tearoff=False ,font=("bold",14))

		self.window_attendance_departure = Menu(self.main_menubar,tearoff = False)
		self.window_attendance_departure.add_command(label ='تسجيل الحضور والإنصراف', command=lambda:self.RunClassAttendanceAndDeparture())
		self.window_attendance_departure.add_command(label ="أقسام الموظفين",command=lambda:self.RunClassListEmployee())
		self.window_attendance_departure.add_command(label='رواتب الموظفين' ,command=lambda:self.RunClassSalaryEmployee())
		self.window_attendance_departure.add_command(label="إرسال الرسائل" ,command=lambda:self.RunClassSendMessageEmployee())
		self.window_attendance_departure.add_command(label="الإجازات" ,command=lambda:self.RunClassVacationsEmployee())
		self.window_attendance_departure.add_command(labe="حفظ بيانات الموظفين",command=lambda:self.RunClassSaveDataInsertEmployee())
		self.main_menubar.add_cascade(label ='الموظفين', menu = self.window_attendance_departure)


		
		self.window_setting = Menu(self.master , tearoff=0)
		self.window_setting.add_command(label="إعدادت اللغة",command=lambda:self.RunclassSettingApllication())
		self.window_setting.add_command(label="إنشاء نسخة إحتياطية", command=lambda:self.RunClassBackApplication())
		self.main_menubar.add_cascade(label="الإعدادات",menu=self.window_setting)




		self.window_help = Menu(self.master)
		self.window_help.add_command(label="الإتصال بنا",command=lambda:self.RunClassHelpEmployee())
		self.window_help.add_command(label="من نحن", command=lambda:self.RunClassWhoAreWeEmployee())
		self.main_menubar.add_cascade(label="مساعدة" ,menu=self.window_help)
		self.master.config(menu=self.main_menubar)




	
	def RunClassAttendanceAndDeparture(self):
		""" Run Window Attendance And Departure """
		self.class_attendance = AttendanceAndDeparture(self.master)



	def RunClassListEmployee(self):
		""" Run Window Class List Employee  """
		self.class_list_employee = StyleListEmployee(self.master)



	def RunClassSalaryEmployee(self):
		""" Run Window Class Salary Employee  """
		self.class_list_employee = StyleSalaryEmployee(self.master)



	def RunClassSendMessageEmployee(self):
		""" Run Window Class Send Message Employee  """
		self.class_message_employee = StyleSendMessageEmployee(self.master)



	def RunClassVacationsEmployee(self):
		""" Run Window Class Vecations Application """
		self.class_vacations = StyleVacations(self.master)




	def RunClassHelpEmployee(self):
		""" Run Window Class Vecations Application """
		self.class_help = Help(self.master)




	def RunClassWhoAreWeEmployee(self):
		""" Run Window Class WhoAreWe Application """
		self.class_whoarewe = WhoAreWe(self.master)
	


	def RunClassSaveDataInsertEmployee(self):
		"""Run class Save Data Insert Employee this is save Data in file docx."""
		self.class_save_data_insert = SaveDataInsertEmployee(self.master)
		self.class_save_data_insert.save_data()


	
	def RunclassSettingApllication(self):
		"""Run class Setting Applicatin"""
		self.class_setting_application = StyleSettingApllication(self.master, main_app=self.main_app)



	def RunClassBackApplication(self):
		""" RUn class Backup Application """
		self.class_backup = StyleBackUp(self.master)