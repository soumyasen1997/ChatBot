from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
import math
import sqlite3
import pickle
import numpy as np
import random

global account_number


#login windows
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("1200x750")
    Label(login_screen, text="Please enter details below to login to BankBot", font=("Calibri", 24)).pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
    Label(login_screen, text="Username * ", font=("Calibri", 18)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ", font=("Calibri", 18)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1,font=("Calibri", 18), command = login_verify).pack()



#login verification  
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    if (username1=='arka' and password1=='12345'):
    	account_number = 98794567
    	login_sucess(account_number)
    elif (username1=='rounak' and password1=='12345'):
    	account_number = 87094567
    	login_sucess(account_number)
    else:
    	wrong_credentials()
 

#exit of login fail screen 
def delete_login_fail():
    details_recog_screen.destroy()

#login screen remove on successful login
def login_success_destroy():
    login_screen.destroy()

#exit of main screen
def exit():
	main_screen.destroy()

#wrong details on login
def wrong_credentials():
	global details_recog_screen
	details_recog_screen = Toplevel(login_screen)
	details_recog_screen.title("Wrong Details")
	details_recog_screen.geometry("250x150")
	Label(details_recog_screen, text="Enter Valid Details ").pack()
	Button(details_recog_screen, text="OK", command=delete_login_fail).pack()


#login success and bankbot interface
def login_sucess(account_number):
	login_success_destroy()
	conn=sqlite3.connect('bank-query-sf.db')
	c=conn.cursor()
	endl="\n"
	alpha=[]

	#for ticket raise
	for i in range(26):
		alpha.append(chr(65+i))
	for i in range(26):
		alpha.append(chr(97+i))

	window = Toplevel(main_screen)
	window.iconbitmap('logo.ico')
	window.title('BankBot')

	text1 = tk.Text(window, height=20, width=30)
	photo = tk.PhotoImage(file='./logo1.png')
	text1.tag_configure('bold', foreground='blue', font=('Arial', 20, 'bold', 'italic'), justify='center')
	text1.tag_configure('bold0', foreground='black', font=('Tempus Sans ITC', 14, 'bold', 'italic'), justify='center')
	text1.tag_configure('bold00', foreground='black', font=('Tempus Sans ITC',9, 'bold', 'italic'))
	text1.image_create(tk.END, image=photo)
	text1.insert(tk.END,'\n\nBankBot\n', 'bold')
	text1.insert(tk.END,'- A Virtual Assistant on \nBank-System made by \nArtifical Intelligence', 'bold0')
	text1.insert(tk.END,'\n\n\n\n  Soumya         Debomit          Akanksha', 'bold00')
	text1.pack(side=tk.LEFT)

	messages = Text(window)
	messages.pack(fill='both', expand=True)

	input_user = StringVar()
	input_field = Entry(window, text=input_user)
	input_field.pack(side=BOTTOM, fill=X)

	interpreter=Interpreter.load('./models/nlu/default/Bankbot_model')

	messages.tag_configure('bold1', foreground='black', font=('Arial', 16, 'bold', 'italic'), justify='left')
	messages.tag_configure('bold2', foreground='red',font=('Arial', 14, 'bold', 'italic'))
	messages.tag_configure('bold3', foreground='red',font=('Arial', 14, 'bold', 'italic'), justify='right')

	tfidf = pickle.load(open("feature.pkl", "rb"))


	#similarity check between query and data stored in training dataset vector
	def cosine(a,b):
		c=0
		for i in range(len(a)):
			c=c+(a[i]*b[i])
		cosi=c/float((sum(a)*sum(b))**0.5)
		return cosi

	#reply part
	def Enter_pressed(event):
		intent='NA'
		intent_conf=0.0
		entity='NA'
		entity_conf=0.0
		input_get = input_field.get()
		#print(input_get)
		messages.insert(INSERT, '%s\n' % input_get, 'bold1')
		input_get=input_get.split(" ")
		sent=" ".join([ii.lower() for ii in input_get])
		query=interpreter.parse(sent)

		if(query['intent_ranking']!=[]):
			if 'name' in query['intent_ranking'][0]:
				intent=query['intent_ranking'][0]['name']
			if 'confidence' in query['intent_ranking'][0]:
				intent_conf=query['intent_ranking'][0]['confidence']


		if(query['entities']!=[]):
			if 'value' in query['entities'][0]:
				entity=query['entities'][0]['value']
			if 'confidence' in query['entities'][0]:
				entity_conf=query['entities'][0]['confidence']

		#print(intent,entity)

		if(intent=='NA' or intent_conf<0.3):
			reply="Ohh Huhh, I didn't understand.I am still learning."
		else:
			vec=tfidf.transform([sent])
			vec=vec.toarray()
			vec=vec[0]
			if(sum(vec)==0):
				reply="Ohh Huhh, I didn't understand. Ask me account related, card related or loan related query."
			else:
				filen=intent+"-vectors.txt"
				index=-1
				lines=np.loadtxt(filen,delimiter=' ')
				#lines=fin.readlines()
				max_cos=0.0
				#print(len(lines))
				for line in lines:
					
					ind=line[0]
					vec1=line[1:]
					#print(len(vec)) **
					#print(len(vec1))
					cos=cosine(vec,vec1)
					if(cos>=max_cos):
						max_cos = cos
						index=ind
				if(index==-1):
					reply="Ohh Huhh, I didn't understand. I am still learning."
				else:
					qqq='SELECT * FROM {}'.format(intent)
					c.execute(qqq)
					rows=c.fetchall()
					reply=rows[int(index)][2]
					#print(reply)

		#when Bot can't give answer directly
		if(reply == 'Not Available'):
			ticket = 'skybits_'+str(int(10000*random.random()))+"_"+random.choice(alpha)+random.choice(alpha)+random.choice(alpha)
			ans = "\tWe have raised your issue to the bank. Your ticket number is "+ticket+". "+intent+" authority will get back to you soon."
			messages.insert(INSERT, '%s\n' % endl)
			messages.insert(INSERT, '%s\n' % ans, 'bold2')
			messages.insert(INSERT, '%s\n' % endl)
			return "break"

		#when ans has to be fetched from database
		elif (reply == 'fetch'):
			if intent == "account_balance_enquiry":
				qq = rows[int(index)][3]+str(account_number)
				#print(qq)
				c.execute(qq)
				ans=c.fetchall()[0][0]
				ans = "Your bank account balance is "+str(ans)+' rupees'
				print(endl)
				messages.insert(INSERT, '%s\n' % endl)
				#print(reply)
				messages.insert(INSERT, '%s\n' % ans, 'bold3')
				print(endl)
				messages.insert(INSERT, '%s\n' % endl)
				return "break"

			elif intent == "account_transaction_details":
				qq = rows[int(index)][3] +str(account_number)
				#print("hhhhh")
				print(qq)
				c.execute(qq)
				if entity == 'withdrawal':
					ans='Your last withdrawal amount is '+str(c.fetchall()[0][0])+' rupees'
					print(endl)
					messages.insert(INSERT, '%s\n' % endl)
					#print(reply)
					messages.insert(INSERT, '%s\n' % ans, 'bold3')
					print(endl)
					messages.insert(INSERT, '%s\n' % endl)
					return "break"

				elif entity == 'deposit':
					ans='You deposited '+str(c.fetchall()[0][0])+' rupees in your account last time'
					print(endl)
					messages.insert(INSERT, '%s\n' % endl)
					print(reply)
					messages.insert(INSERT, '%s\n' % ans, 'bold3')
					print(endl)
					messages.insert(INSERT, '%s\n' % endl)
					return "break"
		
		#when Bot can give answer directly
		else:
			print(endl)
			messages.insert(INSERT, '%s\n' % endl)
			#print(reply)
			messages.insert('end', '\t\t\t%s\n' % reply, 'bold2')
			print(endl)
			messages.insert(INSERT, '%s\n' % endl)
			return "break"


	input_field.bind("<Return>", Enter_pressed)
	window.mainloop()



  
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1200x750")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 20)).pack()
    Label(text="").pack()
    Button(text="Login", height="3", width="30", font=("Calibri", 22),command = login).pack()
    Label(text="").pack()
    Button(text="Logout & Exit", height="3", width="30", font=("Calibri", 22), command = exit).pack()
    photo = tk.PhotoImage(file='./logo1.png')
    Label(text="\n\n").pack()
    Label(main_screen, image=photo).pack()
    main_screen.mainloop()

main_account_screen()

