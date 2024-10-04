



from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from traceback import print_tb

from pefile import set_format
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
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 
from treeview_backup import TreeviewBackUp 

class DatabaseBackUp:
	def __init__(self, root):
		self.root = root

		self.path_database_app = ''
		self.save_location_path = ''

		self.var_selected_path_database = StringVar()
		self.var_path_save_database = StringVar()

		self.class_treeview_backup = TreeviewBackUp(self.root)
		self.class_treeview_backup.show_treeview_backup()


	def check_backup(self):
		"""check path backup!"""
		if (self.var_selected_path_database.get()) == '' or (not os.path.isdir(self.var_selected_path_database.get())):
			messagebox.showerror("خطأ",
                                 "الرجاء قم بتحديد مجلد الموارد بشكل صحيح",
                                 parent=self.root)

		elif (self.var_path_save_database.get()) == '':
			messagebox.showerror("خطأ",
                                 "الرجاء قم بإختيار مكان لحفظ النسخة الإحتياطية",
                                 parent=self.root)
		else:
			self.create_backup()



	def check_path_database_app(self):
		self.path_database_app = filedialog.askdirectory(title="اختر مكان النسخ الاحتياطي")
		if (self.path_database_app.split('/')[-1]) != "resources" or (not os.path.isdir(self.path_database_app)):
			messagebox_error_path_resources_app = messagebox.showerror("خطأ",
                                                                       f"المجلد الذي قمت بإختياره غير صحيح الرجاء قم بإختيار مجلد الموارد عادةً يكون بإسم : (resources)",
                                                                       parent=self.root)

		else:
			messagebox_successfully_path_resources_app = messagebox.showinfo("إختيارك صحيح",
                                                                             f"المجلد الذي إخترته صحيح : {self.path_database_app.split('/')[-1]}",
                                                                             parent=self.root)
			

	def check_path_save_data(self):
		self.save_location_path = self.backup_path = filedialog.asksaveasfilename(
                                     filetypes=[("All files", "*.*")],  title="اختر مكان حفظ النسخة الاحتياطية", parent=self.root)


	def create_backup(self):
		"""Create Back-Up."""
		if (self.save_location_path.split('/')[-1]) != 'resources':
			messagebox.showerror('خطأ', 'يجب ان يكون إسم النسخة الإحتياطية resources لا يحق لك إستخدام إسم آخر', parent=self.root)

		else:
			shutil.copytree(self.path_database_app, self.self.save_location_path)
			messagebox.showinfo("نجاح", f"تم حفظ النسخة الاحتياطية في: {self.save_location_path}", parent=self.root)


