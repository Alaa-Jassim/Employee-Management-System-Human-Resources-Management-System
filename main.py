
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image , ImageTk
from datetime import datetime
import os , sys , shutil
import sqlite3
import time
import threading
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 
from insert_employee.widegts_app import Widgets
from sections.sections import Sections
from login_app.style_sign_up import StyleSignUp
from management_destination.management_exe import copy_resources_folder,manager_Sqlite3, manager_Images, get_resources_path
from login_app.database_login import DatabaseLogin

class StyleLoginApp:
    def __init__(self,master):
        self.master = master 
        self.master.geometry('925x500+500+200')
        self.master.resizable(width=False , height=False)
        self.master.configure(background='#fff')
        self.master.title('تسجيل الدخول')

        self.master.iconbitmap(manager_Images("images_login","title_icon.ico"))
        self.class_database_login = DatabaseLogin(self.master)
        self.class_database_login.create_table()
        self.username = StringVar()
        self.password = StringVar()


        self.add_logo()
        self.add_labels_info()
        self.add_button()
        self.add_button_sign_up()


    def add_logo(self):
        self.cut_image = Image.open(manager_Images("images_login","login.png"))
        self.cut_image = self.cut_image.resize((450,450))
        self.image_logo = ImageTk.PhotoImage(self.cut_image)
        self.label_logo = Label(
            self.master , image=self.image_logo , borderwidth=0 ,bg='white'

            ).place(x=50,y=20)

    def on_entry_user(self,e):
        self.entry_user.delete(0,'end')

    def on_leave_user(self,e):
        self.name = self.entry_user.get()
        if self.name == '':
            self.entry_user.insert(0,"مستخدم إسم")


    def on_entry_pass(self,e):
        self.entry_password.delete(0,'end')

    def on_leave_pass(self,e):
        self.name_pass = self.entry_password.get()
        if self.name_pass == '':
            self.entry_password.insert(0,"مرور كلمة")



    def add_labels_info(self):

        
        self.main_frame = Frame(
            self.master , borderwidth=0 , background='black' , width=350,height=350,bg='white'

            ).place(x=550,y=90)

        self.heading_label = Label(self.master,
            text="الدخول تسجيل",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23 ,"bold"))
        self.heading_label.place(x=670,y=105)


        #======================================================================================================
        self.entry_user = Entry(
            self.main_frame , width=25 ,fg="black" , border=0 , bg="white" ,
             font=("Microsoft YaHei UI Light",11),textvariable=self.username)

        self.entry_user.place(x=590,y=180)
        self.entry_user.insert(0, "المستخدم إسم")
        self.entry_user.bind('<FocusIn>',self.on_entry_user)
        self.entry_user.bind('<FocusOut>',self.on_leave_user)


        self.farme_user_desgin = Frame(self.main_frame,
            width=295,height=2,bg="black")
        self.farme_user_desgin.place(x=590,y=205)

        #======================================================================================================

        self.entry_password = Entry(
            self.main_frame , width=25 ,fg="black" , border=0 , bg="white" , 
            font=("Microsoft YaHei UI Light",11),textvariable=self.password)
        self.entry_password.bind('<FocusIn>',self.on_entry_pass)
        self.entry_password.bind('<FocusOut>',self.on_leave_pass)


        self.entry_password.place(x=590,y=290)
        self.entry_password.insert(0, "المرور كلمة")


        self.farme_password_desgin = Frame(self.main_frame,
            width=295,height=2,bg="black")
        self.farme_password_desgin.place(x=590,y=315)

        #======================================================================================================



    def check_username_sign_in(self):
        """ Checking username if not exists in Table SQlite3 """
        self.connection_username = sqlite3.connect(manager_Sqlite3("database_login", "database_login.db"))
        self.cursor_username = self.connection_username.cursor()

        self.SQL_QUERY_CHECK_USERNAME = """SELECT Username, Password FROM Login WHERE Username = ?""";
        self.DATA_QUERY_CHECK_USERNAME = (self.username.get(),)

        self.cursor_username.execute(self.SQL_QUERY_CHECK_USERNAME, self.DATA_QUERY_CHECK_USERNAME)

        if len(self.cursor_username.fetchall()):
            return True 
        return False 

        self.connection_username.commit() ; self.connection_username.close()



    def check_password_sign_in(self):
        """ Checking username if not exists in Table SQlite3 """
        self.connection_password = sqlite3.connect(manager_Sqlite3("database_login", "database_login.db"))
        self.cursor_password = self.connection_password.cursor()

        self.SQL_QUERY_CHECK_PASSWORD = """SELECT Password FROM Login WHERE Password = ? """;
        self.DATA_QUERY_CHECK_PASSWORD = (self.password.get(),)

        self.cursor_password.execute(self.SQL_QUERY_CHECK_PASSWORD, self.DATA_QUERY_CHECK_PASSWORD)

        if len(self.cursor_password.fetchall()):
            return True 
        return False 

        self.connection_password.commit() ; self.connection_password.close()



    def add_button(self):
        """ Open Window Login Account """
        
        self.button_login = Button(self.main_frame,
            font=('bold',13) , bg="#57a1f8" , fg='white' ,pady=7 ,border=0,
            width=32,text="تسجيل الدخول" ,command=self.open_window_app)
        self.button_login.place(x=590,y=335)



    def add_button_sign_up(self):
        self.label_not_account = Label(self.main_frame,
            text="؟ حساب لديك ليس",fg="black",bg="white",font=("Microsoft YaHei UI Light",11))
        self.label_not_account.place(x=796,y=400)


        self.button_sign_up = Button(self.main_frame,
            bg='white' ,cursor="hand2" ,fg="#57a1f8",border=0,width=6,
            text="تسجيل" ,font=("Microsoft YaHei UI Light",12),command=self.open_window_sign_up)
        self.button_sign_up.place(x=740,y=398)
    

    def open_window_sign_up(self):
        """open window Sign-Up"""
        self.master.destroy()
        self.window = Tk()
        self.class_window_sign_up = StyleSignUp(self.window)
        self.window.mainloop()


    def open_window_app(self):
        if (self.check_username_sign_in()) == False and (self.check_password_sign_in()) == True:
            self.messagebox_username_error = messagebox.showerror("خطأ","إسم المستخدم غير صحيح", parent=self.master)

        elif (self.check_password_sign_in()) == False and (self.check_username_sign_in()) == True :
            self.messagebox_password_error = messagebox.showerror("خطأ","كلمة المرور غير صحيحة", parent=self.master)

        elif (self.check_username_sign_in()) == False and (self.check_password_sign_in()) == False:
            self.messagebox_error_data = messagebox.showerror("خطأ", "إسم المستخدم وكلمة المرور غير مسجلة في قاعدة البيانات", parent=self.master)

        else:
            if (self.check_username_sign_in()) and (self.check_password_sign_in()):
                self.message_login_successfuly = messagebox.askquestion("البيانات صحيحة","هل توافق على تسجيل الدخول؟",parent=self.master)

                if self.message_login_successfuly in ("yes","Yes"):

                    self.master.destroy()
                    application = Tk()
                    main_class_appliaction = Main(application)
                    application.mainloop()
                else:
                    self.messagebox_cancel = messagebox.showinfo("شكراً لك", "هل تريد أن تتراجع عن هذا الأمر؟", parent=self.master)
     
class Main:
    def __init__(self, root):
        self.root = root
        self.class_widgets = Widgets(self.root)
        self.class_sections = Sections(self.root)
    


if __name__ == "__main__":
    app = Tk()
    copy_resources_folder()
    main_class = StyleLoginApp(app)
    app.mainloop()
