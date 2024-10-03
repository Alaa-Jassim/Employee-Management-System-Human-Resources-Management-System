


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
from backup.treeview_backup import TreeviewBackUp
import sqlite3
from datetime import datetime

sys.path.append('../')
from management_destination.management_exe import manager_Images, manager_Sqlite3



class BackUp():
    def __init__(self, root):
        self.root = root

        self.path_database_app = ''
        self.save_location_path = ''

        self.var_selected_path_database = StringVar()
        self.var_path_save_database = StringVar()
        self.create_database()
    
    
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
            self.insert_data_backup()





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
            self.entry_select_path.delete(0, END)
            self.entry_select_path.insert(0, self.path_database_app)

    def check_path_save_data(self):
        self.save_location_path = self.backup_path = filedialog.asksaveasfilename(
                                     filetypes=[("All files", "*.*")],  title="اختر مكان حفظ النسخة الاحتياطية",
                                     parent=self.root)

        self.entry_backup.delete(0,END)
        self.entry_backup.insert(0, self.save_location_path)



    def create_backup(self):
        """Create Back-Up."""

        if (self.save_location_path.split('/')[-1]) != 'resources':
            messagebox.showerror('خطأ', 'يجب ان يكون إسم النسخة الإحتياطية resources لا يحق لك إستخدام إسم آخر', parent=self.root)

        else:
            shutil.copytree(self.path_database_app, self.save_location_path)
            messagebox.showinfo("نجاح", f"تم حفظ النسخة الاحتياطية في: {self.save_location_path}", parent=self.root)


    def create_restory(self):
        """Create Restory."""
        if self.var_path_save_database.get() == '':
            messagebox.showerror('خطأ', 'لإسترداد البيانات يجب تحديد مسار حفظ البيانات', parent=self.root)

        elif self.var_selected_path_database.get() == '':
            messagebox.showerror('خطأ', "يجب ان تقوم بتحديد مسار قاعدة البيانات لأسترداداها", parent=self.root)


        elif (self.save_location_path.split('/')[-1]) != 'resources':
            messagebox.showerror('خطأ', 'الرجاء قم بحفظ ملف الموارد بإسمه resources لا يمكنك إستخدام إسم آخر', parent=self.root)

        else:
            shutil.copytree(self.path_database_app, self.save_location_path)
            messagebox.showinfo("نجاح", f"تم إسترداد النسخة الإحتياطية بنجاح: {self.save_location_path}", parent=self.root)


    def create_database(self):
        self.connection_backup = sqlite3.connect(manager_Sqlite3("database_backup", "Backup.db"))
        self.cursor_backup = self.connection_backup.cursor()

        self.SQL_QUERY = """ CREATE TABLE IF NOT EXISTS Backup 
        (Backup TEXT NOT NULL,
        Backup_history DATE NOT NULL)""";

        self.cursor_backup.execute(self.SQL_QUERY)
        self.connection_backup.commit()


    def insert_data_backup(self):
        self.now = datetime.now()
        self.datetime = self.now.strftime("%Y-%m-%d")



        self.connection_insert = sqlite3.connect(manager_Sqlite3("database_backup", "Backup.db"))
        self.cursor_insert = self.connection_insert.cursor()

        self.SQL_INSERT_DATA = """ INSERT INTO Backup (Backup, Backup_history) VALUES (?,?)""";
        self.DATA_INSERT = (self.save_location_path, self.datetime)

        self.cursor_insert.execute(self.SQL_INSERT_DATA, self.DATA_INSERT)

        self.connection_insert.commit()
        self.class_treeview_backup.select_data_backup()


    def delete_data(self):
        """ Function Delete Al Data """

        self.connection_delete = sqlite3.connect(manager_Sqlite3("database_backup", "Backup.db"))
        self.cursor_delete = self.connection_delete.cursor()

        self.messageDeleteAll = messagebox.askquestion('هل توافق على هذا الإجراء',"عند موافقتك على هذا الإجراء سيتم حذف جميع النسخ الإحتياطية من قاعدة البيانات", parent=self.root)
        if self.messageDeleteAll == 'yes':
            self.cursor_delete.execute('DELETE FROM Backup')
            self.class_treeview_backup.table_data_backup.delete(*self.class_treeview_backup.table_data_backup.get_children())

            for self.row in self.cursor_delete.fetchall() :
                self.class_treeview_backup.table_data_backup.insert('',END,value=self.row)

        self.connection_delete.commit()
        self.connection_delete.close()


class StyleBackUp(BackUp):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = Toplevel()
        self.root.geometry("1180x600+360+95")
        self.root.resizable(width=False,height=False)
        self.root.configure(background='#EAF2F8')
        self.root.title("النسخ الإحتياطي")
        self.root.iconbitmap(manager_Images("images_backup","icon_window.ico"))

        self.class_treeview_backup = TreeviewBackUp(self.root)
        self.class_treeview_backup.show_treeview_backup()
        self.class_treeview_backup.select_data_backup()
       


        self.add_title()
        self.add_frame_select_data()
        self.add_button_select()


        #=============================================
        self.add_frame_backup_data()
        self.add_button_backup()
        #=============================================
        self.add_frame_buttons()

        

    def add_title(self):
    	""" Add Title Label """
    	self.title_label_backup = Label(self.root,
    		text="إنشاء نسخة إحتياطية للبيانات" ,font=("bold",20),
    		background='#d9ddf7' ,)
    	self.title_label_backup.pack(fill=X)


    def add_frame_select_data(self):
        self.frame_select_data = Frame(self.root,background='#E5E1F4', relief=RIDGE, bd=2, width=1176, height=80)
        self.frame_select_data.place(x=1, y=40)

        self.entry_select_path = Entry(self.frame_select_data,
                                  width=50,
                                  font=("bold",16),
                                  justify=CENTER,
                                  relief=RAISED,
                                  textvariable=self.var_selected_path_database
                                  )

        self.entry_select_path.place(x=220,y=27)
        self.entry_select_path.delete(0, END)
        self.entry_select_path.insert(0, self.path_database_app)


        


    def add_button_select(self):
        """ Add Button Select Path Data """
        self.label_path_data = Label(self.frame_select_data ,
            text="الرجاء قم بتحديد ملف قاعدة البيانات" ,
            font=("bold",20),
            background='#E5E1F4',
            width=20)

        self.label_path_data.place(x=830,y=22)

        self.choice_image = Image.open(manager_Images("images_backup","select_data.png"))
        self.choice_image = self.choice_image.resize((33,33))
        self.insert_choice_image = ImageTk.PhotoImage(self.choice_image)


        self.button_choice_path = Button(self.frame_select_data, background='#F7F7F9', width=130, height=30, text='إختيار ملف',
                                  font=('Bold Oblique', 18),
                                  image=self.insert_choice_image, compound='left', padx=20, relief=FLAT, bd=1,
                                  command=self.check_path_database_app
                                  )

        self.button_choice_path.place(x=30, y=22)



    #====================================================================================================
    def add_frame_backup_data(self):
        self.frame_backup_data = Frame(self.root,background='#E5E1F4', relief=RIDGE, bd=2, width=1176, height=80)
        self.frame_backup_data.place(x=1, y=119)

        self.entry_backup = Entry(self.frame_backup_data,
                                  width=44,
                                  font=("bold",16),
                                  justify=CENTER,
                                  relief=RAISED,
                                  textvariable=self.var_path_save_database
                                  )
        self.entry_backup.place(x=197,y=22)
        self.entry_backup.delete(0,END)
        self.entry_backup.insert(0, self.save_location_path)


    def add_button_backup(self):
        """ Add Button Select Path Data """
        self.label_path_data = Label(self.frame_backup_data ,
            text="الرجاء قم بتحديد مكان حفظ النسخة الإحتياطية" ,
            font=("bold",20),
            background='#E5E1F4',
            width=25)

        self.label_path_data.place(x=745,y=20)



        self.selected_image = Image.open(manager_Images("images_backup","choice_path.png"))
        self.selected_image = self.selected_image.resize((33,33))
        self.insert_selected_image = ImageTk.PhotoImage(self.selected_image)


        self.button_selected_path = Button(self.frame_backup_data, background='#F7F7F9', width=120, height=30, text='إختيار المسار',
                                  font=('Bold Oblique', 18),
                                  image=self.insert_selected_image, compound='left', padx=20, relief=FLAT, bd=1,
                                  command=self.check_path_save_data

                                  )

        self.button_selected_path.place(x=20, y=16)


    #=================================================================================================================

    def add_frame_buttons(self):
        self.frame_buttons = Frame(self.root,background='#E5E1F4', relief=RIDGE, bd=2, width=1176, height=80)
        self.frame_buttons.place(x=1, y=516)


        self.backup_image = Image.open(manager_Images("images_backup","backup_data.png"))
        self.backup_image = self.backup_image.resize((33,33))
        self.insert_backup_image = ImageTk.PhotoImage(self.backup_image)


        self.button_backup = Button(self.frame_buttons, background='#F7F7F9', width=188, height=30, text='إنشاء نسخة إحتياطية',
                                  font=('Bold Oblique', 18),
                                  image=self.insert_backup_image, compound='left', padx=20, relief=FLAT, bd=1,
                                  command=self.check_backup
                                  )

        self.button_backup.place(x=920, y=20)

        #=======================================================================================================


        self.restore_image = Image.open(manager_Images("images_backup","restore_backup.png"))
        self.restore_image = self.restore_image.resize((33,33))
        self.insert_restore_image = ImageTk.PhotoImage(self.restore_image)

        self.button_restore_backup = Button(self.frame_buttons, background='#F7F7F9', width=230, height=30, text='استرداد النسخة الإحتياطية',
                                  font=('Bold Oblique', 18),
                                  image=self.insert_restore_image, compound='left', padx=20, relief=FLAT, bd=1,
                                  command=self.create_restory
                                  )

        self.button_restore_backup.place(x=590, y=20)

        #=======================================================================================================


    
        self.delete_image = Image.open(manager_Images("images_backup","delete_database.png"))
        self.delete_image = self.delete_image.resize((33,33))
        self.insert_delete_image = ImageTk.PhotoImage(self.delete_image)


        self.button_delete = Button(self.frame_buttons, background='#F7F7F9', width=200, height=30, text='حذف النسخ الإحتياطية',
                                  font=('Bold Oblique', 18),
                                  image=self.insert_delete_image, compound='left', padx=20, relief=FLAT, bd=1,
                                  command=self.delete_data
                                  
                                  )
        self.button_delete.place(x=280, y=20)


  