
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
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 
from setting.database_setting import DataBaseSetting
from language.text_manager import get_language, get_translation, save_language
from insert_employee.widegts_app import Widgets
from management_destination.management_exe import manager_Images


class StyleSettingApllication():
    def __init__(self, root=None, main_app=None):

        self.root = Toplevel(root)
        self.root.geometry("1180x600+360+95")
        self.root.resizable(width=False,height=False)
        self.root.configure(background='#EAF2F8')

        self.main_app = main_app

        self.language = get_language()
        self.text = get_translation(self.language)


    

        self.class_database_setting = DataBaseSetting(self.root)

        self.style_combobox = ttk.Style()
        self.style_combobox.configure("TCombobox", padding=5, anchor="center")

        self.add_title()
        self.add_combobox()
        self.add_button()

    def add_title(self):
        """ Add Title Label """
        self.title_label_setting = Label(self.root,
            text="تغيير اللغة" ,font=("bold",20),
            background='#d9ddf7' ,)
        self.title_label_setting.pack(fill=X)



    def add_combobox(self):
        """ Add combobox selected language """
        self.frame_combobox = Frame(self.root,

            background='#E5E1F4', relief=RIDGE , bd=2 , width=1176,height=80
            )
        self.frame_combobox.place(x=1,y=40)

        self.label_setting = Label(self.frame_combobox,
            text="الرجاء إختيار اللغة" , 
            font=("bold",20),
            width=12,
            background='#E5E1F4',)

        self.label_setting.place(x=970,y=22)
        self.combobox_language = ttk.Combobox(self.frame_combobox ,
            width=33 , height=12 , 
            font=("bold",15),
            textvariable=self.class_database_setting.var_language
            )

        self.combobox_language["values"] = ("arabic","english") 
        self.combobox_language['justify'] = CENTER

        self.combobox_language.option_add('*TCombobox*Listbox.Justify', 'center')
        self.combobox_language.place(x=540,y=22)


    def add_button(self):
        """ Add Button Save Changed """

        self.label_button = Label(self.frame_combobox ,
            text="الرجاء قم بحفظ التغيرات" ,
            font=("bold",20),
            background='#E5E1F4',
            width=16)

        self.label_button.place(x=240,y=22)

        self.save_image = Image.open(manager_Images("images_language","save_change.png"))
        self.save_image = self.save_image.resize((35,35))

        self.insert_save_image = ImageTk.PhotoImage(self.save_image)




        self.button_save = Button(self.frame_combobox , background='#F7F7F9' , width=150 , height=30 , text='حفظ التغيرات',font=('Bold Oblique',18) ,
        image=self.insert_save_image , compound='left',padx=20,relief=FLAT , bd=1,
        command=self.show_language
        )
        self.button_save.place(x=35,y=22)


    def show_language(self):

       # try:
        self.language = self.class_database_setting.var_language.get()
        if self.language :
            save_language(self.language)
            self.text = get_translation(self.language)

            self.qusetion = messagebox.askquestion("Info",self.text["insert employee"]["message successfully insert employee"],parent=self.root)
            if self.qusetion in ("yes", "Yes"):
                self.update_section_insert_employee()


        else:
            self.message_language = messagebox.showerror("Information",self.text["insert employee"]["error choice langugae"],parent=self.root)

        # except Exception :
        #     self.message_error =  messagebox.showerror("Information",self.text["insert employee"]["error select language"],parent=self.root)

    

    def update_section_insert_employee(self):
        """ This is a function update Widgets Section insert Employee """
        if self.main_app and self.main_app.class_widgets:
            if self.language:
                self.text = get_translation(self.language)
                self.main_app.class_widgets.title_app.config(text=self.text["insert employee"]["title insert employee"])
                #self.main_app.class_widgets.label_search.config(text=self.text["insert employee"]["search label insert employee"])
            else:
                print("Error: main_app or class_style is not set properly.")

        # if self.language:
        #     self.text = get_translation(self.language)
        #     self.main_app.class_widgets.title_app.config(text=self.text["insert employee"]["title insert employee"])
            





        