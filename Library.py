from tkinter import *
from tkinter import messagebox
import sqlite3
window=Tk()
window.title("BOOK LIBRARY")
title=StringVar()
isbn=IntVar()
Author=StringVar()
price=IntVar()
id1=IntVar()
def database():
		
	unique=id1.get()	
	title1=title.get()
	isbn1=isbn.get()
	Author_name=Author.get()
	Price1=price.get()
			
	conn=sqlite3.connect('book4.db')
	
		
	with conn:
		cursor=conn.cursor()
	cursor.execute('Create table if not exists book_data8(U_id int,Title text,isbn int,Author text,Price int)')
	cursor.execute('insert into book_data8(U_id,Title,isbn,Author,Price)VALUES(?,?,?,?,?)',			         (unique,title1,isbn1,Author_name,Price1))	
	messagebox.showinfo("info added succesfully")	
	conn.commit()

def del1():
	unique=id1.get()	
	#title1=title.get()
	#isbn1=isbn.get()
	#Author_name=Author.get()
	#Price1=price.get()	
	conn=sqlite3.connect('book4.db')
	with conn:
		cursor=conn.cursor()	
	cursor=conn.cursor()	
	cursor.execute('delete from book_data8 where U_id=?',(unique,))
	messagebox.showinfo("info deleted succesfulwly")	
	conn.commit()
	
def view():
	conn=sqlite3.connect('book4.db')	
	with conn:
		cursor=conn.cursor()	
	cursor=conn.cursor()
	result=cursor.execute("select * from book_data8")
	#messagebox.showinfo("fetching student info")	
	list1.delete(0,list1.size())	
	for row in result.fetchall():
			list1.insert(END,row)
	conn.commit()

def clear():
	list1.delete(0,END)
	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)
	e4.delete(0,END)
	e5.delete(0,END)	
	#l2.destroy()
	#l3.destroy()
	#l4.destroy()

def update():
	title1=title.get()
	Author_name=Author.get()
	Price1=price.get()	
	isbn1=isbn.get()	
	unique=id1.get()	
	conn=sqlite3.connect('book4.db')	
	with conn:
		cursor=conn.cursor()	
	#cursor.execute("update book_data8 set Title='baba',Author='Amruta',Price=500 where isbn=789")	
	cursor.execute("update book_data8 SET Title=(?),Author=(?),Price=(?),isbn=(?) where U_id=(?)",(title1,Author_name,Price1,isbn1,unique))		
	#cursor.execute('select * from book_data8')	
	conn.commit()
def u_id():
	unique=id1.get()	
	conn=sqlite3.connect('book4.db')
	with conn:
		cursor=conn.cursor()	
	try:	
		result=cursor.execute('select * from book_data8 where isbn=?',(unique,))
		for row in result.fetchall():
			list1.insert(END,row)	
	except:
		messagebox.showinfo("Say Hello", "Hello World")
	conn.commit()	

def search():
	unique=id1.get()	
	conn=sqlite3.connect('book4.db')
	with conn:
		cursor=conn.cursor()	
	try:	
		result=cursor.execute('select * from book_data8 where U_id=?',(unique,))
		for row in result.fetchall():
			list1.insert(END,row)	
	except:
		messagebox.showinfo("Say Hello", "Hello World")
	conn.commit()
l1=Label(window,text="Title")
l1.grid(row=0,column=0)
e1=Entry(window,textvar=title)
e1.grid(row=0,column=1)
l2=Label(window,text="ISBN")
l2.grid(row=0,column=3)
e2=Entry(window,textvar=isbn)
e2.grid(row=0,column=4)
l3=Label(window,text="Author")
l3.grid(row=1,column=0)
e3=Entry(window,textvar=Author)
e3.grid(row=1,column=1)
l4=Label(window,text="Price")
l4.grid(row=1,column=3)
e4=Entry(window,textvar=price)
e4.grid(row=1,column=4)
l5=Label(window,text="UNIQUE ID")
l5.grid(row=2,column=0)
e5=Entry(window,textvar=id1)
e5.grid(row=2,column=1)
list1=Listbox(window,height=10,width=50)
list1.grid(row=7,column=3)
Button(window,text='Insert',command=database).grid(row=2,column=5)
Button(window,text='DELETE',command=del1).grid(row=3,column=5)
#Button(window,text='U_id',command
Button(window,text='VIEW',command=view).grid(row=8,column=3)
Button(window,text='Clear',command=clear).grid(row=8,column=4)
Button(window,text='SEARCH',command=search).grid(row=6,column=5)
Button(window,text='Update',command=update).grid(row=5,column=5)
sb=Scrollbar(window)
sb.grid(row=7,column=4,rowspan=10)
list1.configure(yscrollcommand=sb.set)
sb.configure(command=list1.yview)
window.mainloop() 



