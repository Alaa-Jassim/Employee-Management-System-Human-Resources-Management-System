



from tkinter import *
from tkinter import filedialog
import csv
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image , ImageTk
from datetime import datetime
from threading import Thread
import webbrowser
from babel.dates import format_date, parse_date, get_day_names 
from babel.numbers import * 
import os
from management_destination.management_exe import manager_Images

class Help:
	def __init__(self,master):
		self.master = Toplevel()
		self.master.geometry("1000x400+450+100")
		self.master.title("الإتصال بنا")
		self.master.resizable(width=False,height=False)
		self.master.iconbitmap(manager_Images("images_help","contact_app.ico"))
		self.master.configure(bg='white')

		self.title_app = Label(self.master,background="#E8E4FA",text='الإتصال بنا' , font=("bold",18))
		self.title_app.pack(fill=X)

		self.account_facebook()
		self.account_twitter()
		self.account_youtube()
		self.account_telegram()


	def account_facebook(self):
		self.image_facebook = Image.open(manager_Images("images_help","image_facebook.png"))
		self.image_facebook = self.image_facebook.resize((160,170))
		self.insert_image = ImageTk.PhotoImage(self.image_facebook)

		self.label_insert_image_facebook = Label(self.master,image=self.insert_image,bg='white')
		self.label_insert_image_facebook.place(x=10,y=40)



		self.button_facebook = Button(self.master,text="الإتصال الآن" , width=10 , height=1,bg='#E8E4FA',
			font=("bold",17),bd=1,command=self.connect_facebook)
		self.button_facebook.place(x=20,y=200)





	def account_twitter(self):
		self.image_twitter = Image.open(manager_Images("images_help","image_twitter.png"))
		self.image_twitter = self.image_twitter.resize((160,170))
		self.insert_image_twitter = ImageTk.PhotoImage(self.image_twitter)

		self.label_insert_image_twitter = Label(self.master,image=self.insert_image_twitter,bg='white')
		self.label_insert_image_twitter.place(x=270,y=40)



		self.button_twitter = Button(self.master,text="الإتصال الآن" , width=10 , height=1,bg='#E8E4FA',
			font=("bold",17),bd=1,command=self.connect_twitter)
		self.button_twitter.place(x=270,y=200)



	def account_youtube(self):
		self.image_youtube = Image.open(manager_Images("images_help","image_youtube.png"))
		self.image_youtube = self.image_youtube.resize((150,150))
		self.insert_image_youtube = ImageTk.PhotoImage(self.image_youtube)

		self.label_insert_image_youtube = Label(self.master,image=self.insert_image_youtube,bg='white')
		self.label_insert_image_youtube.place(x=530,y=50)


		self.button_youtube = Button(self.master,text="الإتصال الآن" , width=10 , height=1,bg='#E8E4FA',
			font=("bold",17),bd=1,command=self.connect_youtube)
		self.button_youtube.place(x=540,y=200)




	def account_telegram(self):
		self.image_telegram = Image.open(manager_Images("images_help","image_telegram.png"))
		self.image_telegram = self.image_telegram.resize((160,170))
		self.insert_image_telegram = ImageTk.PhotoImage(self.image_telegram)

		self.label_insert_image_telegram = Label(self.master,image=self.insert_image_telegram,bg='white')
		self.label_insert_image_telegram.place(x=800,y=40)




		self.button_telegram = Button(self.master,text="الإتصال الآن" , width=10 , height=1,bg='#E8E4FA',
			font=("bold",17),bd=1,command=self.connect_telegram)
		self.button_telegram.place(x=810,y=200)


	def connect_facebook(self):
		self.facebook = webbrowser.open("https://www.facebook.com/alaa.jassim.mohammed/")



	def connect_youtube(self):
		self.youtube = webbrowser.open("https://www.youtube.com/channel/UCcpTl7FtFATtGs8TVfZpPtg")



	def connect_twitter(self):
		self.twitter = webbrowser.open("https://twitter.com/ajm0o?t=FJU-kueejivy0G-KZPOBkQ&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;s=09")



	def connect_telegram(self):
		self.telegram = webbrowser.open("https://t.me/ajm0o")
