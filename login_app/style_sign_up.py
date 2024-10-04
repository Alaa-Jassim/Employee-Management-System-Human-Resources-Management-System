
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from datetime import datetime
from PIL import Image
import sqlite3
from PIL import Image , ImageTk
from tkinter import filedialog
from threading import Thread
import threading
from babel.dates import format_date, parse_date, get_day_names 
from babel.numbers import * 
import os , sys
from login_app.database_login import DatabaseLogin
from management_destination.management_exe import manager_Images


class StyleSignUp(object):
    def __init__(self,master):
        self.master = master
        self.master.geometry('925x500+500+200')
        self.master.resizable(width=False , height=False)
        self.master.configure(background='#fff')
        self.master.title('إنشاء حساب')
        self.master.iconbitmap(manager_Images("images_login","title_new_account.ico"))

        self.class_database_login = DatabaseLogin(self.master)


        self.add_logo_sign_up()
        self.add_labels_info_sign_up()
        self.add_button_create_account()

    def add_logo_sign_up(self):
         self.cut_image_sing_up = Image.open(manager_Images("images_login","sing_up.png"))
         self.cut_image_sing_up = self.cut_image_sing_up.resize((350,350))
         self.image_logo_sing_up = ImageTk.PhotoImage(self.cut_image_sing_up)

         self.label_logo_new = Label(
              self.master , image=self.image_logo_sing_up , border=0 ,bg='white')
         self.label_logo_new.place(x=50,y=90)
        
    

    def click_username_entry(self,value):
         self.input_username_sign_up.delete(0,END)
    

    def click_username_leave(self, value):
         self.value_username = self.input_username_sign_up.get()
         if self.value_username == '':
              self.input_username_sign_up.insert(0,"المستخدم إسم")
    

    def click_password_entry(self, value):
         self.input_password_sign_up.delete(0,END)
    

    def click_password_leave(self, value):
         self.value_password = self.input_password_sign_up.get()
         if self.value_password == '':
              self.input_password_sign_up.insert(0,"المرور كلمة")
    

    def click_password_confirm_entry(self, value):
         self.input_confirm_password.delete(0,END)
    

    def click_password_confirm_leave(self, value):
         self.value_password_confirm = self.input_confirm_password.get()
         if self.value_password_confirm == '':
              self.input_confirm_password.insert(0,"المرور كلمة تأكيد")
    
    
    def add_labels_info_sign_up(self):
         self.main_frame_sign_up = Frame(
			self.master , borderwidth=0 , background='black' , width=350,height=350,bg='#fff'
			).place(x=480,y=50)
         
         self.heading_label_sign_up = Label(self.main_frame_sign_up,
									 text="حساب إنشاء",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23 ,"bold"))
         self.heading_label_sign_up.place(x=580,y=70)

         #=======================================================================================
         
         self.input_username_sign_up = Entry(self.main_frame_sign_up ,font=("Microsoft YaHei UI Light",11 ,"bold"),bg='white',
									  fg='black',border=0 ,width=25,
                                               textvariable=self.class_database_login.var_username)
         
         self.input_username_sign_up.place(x=496,y=140)
         self.input_username_sign_up.insert(0, "المستخدم إسم")
         self.input_username_sign_up.bind('<FocusIn>',self.click_username_entry)
         self.input_username_sign_up.bind('<FocusOut>',self.click_username_leave)
         self.farme_user_desgin_sign_up = Frame(self.main_frame_sign_up,
										 width=295,height=2,bg="black")
         self.farme_user_desgin_sign_up.place(x=496,y=165)
         
         #===================================================================================
         self.input_password_sign_up = Entry(self.main_frame_sign_up ,font=("Microsoft YaHei UI Light",11 ,"bold"),bg='white',
									  fg='black',border=0 ,width=25,
                                               textvariable=self.class_database_login.var_password)
         
         self.input_password_sign_up.place(x=496,y=240)
         self.input_password_sign_up.insert(0, "المرور كلمة")
         self.input_password_sign_up.bind('<FocusIn>',self.click_password_entry)
         self.input_password_sign_up.bind('<FocusOut>',self.click_password_leave)
         self.farme_pass_desgin_sign_up = Frame(self.main_frame_sign_up,
										 width=295,height=2,bg="black")
         self.farme_pass_desgin_sign_up.place(x=496,y=265)
         
         #=====================================================================================
         self.farme_pass_confirm_desgin_sign_up = Frame(self.main_frame_sign_up,
												 width=295,height=2,bg="black")
         self.farme_pass_confirm_desgin_sign_up.place(x=496,y=380)
         
         self.input_confirm_password = Entry(self.main_frame_sign_up ,font=("Microsoft YaHei UI Light",11 ,"bold"),bg='white',
									  fg='black',border=0 ,width=25,
                                               textvariable=self.class_database_login.var_confirm_password)
         self.input_confirm_password.place(x=496,y=353)
         self.input_confirm_password.insert(0,"المرور كلمة تأكيد")
         self.input_confirm_password.bind('<FocusIn>',self.click_password_confirm_entry)
         self.input_confirm_password.bind('<FocusOut>',self.click_password_confirm_leave)
         
    
    def add_button_create_account(self):
        self.button_create_account = Button(self.main_frame_sign_up,
									  font=('bold',13) , bg="#57a1f8" , fg='white' ,pady=7 ,border=0,
									  width=32,text="إنشاء الحساب" ,
                                               command=self.class_database_login.check_data_login)
        self.button_create_account.place(x=498,y=397)
        
    
    def open_window_login(self):
          if self.check_table_sqlite() == True:
            self.master.destroy()
            self.window_sing_in = Tk()
            self.class_window_login = StyleLoginApp(self.window_sing_in)
            self.window_sing_in.mainloop()
		
	