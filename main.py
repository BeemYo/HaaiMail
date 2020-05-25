from tkinter import *
from tkinter import filedialog
import sys
import smtplib

Saved = False
saveLocation = None
global email, password, to

def start():
	global emailV, passwordV
	emailV = email.get("1.0", "end-1c")
	passwordV = password.get("1.0", "end-1c")
	login.destroy()
	Init()

def darkTheme():
	global root, buttonF, to, subject
	root.config(background="#2d2d2d")
	buttonF.config(background="#2d2d2d")
	
	to.config(background="#1d1d1d", fg="white", insertbackground="white")
	
	subject.config(background="#1d1d1d", fg="white", insertbackground="white")

	text.config(background="#1d1d1d", fg="white", insertbackground="white")

def lightTheme():
	global root, buttonF, to, subject, text
	root.config(background="#e5e5e5")
	buttonF.config(background="#e5e5e5")
	
	to.config(background="#f7f5f4", fg="black", insertbackground="black")
	
	subject.config(background="#f7f5f4", fg="black", insertbackground="black")

	text.config(background="#f7f5f4", fg="black", insertbackground="black")

def save():
    global text, Saved, saveLocation

    t = text.get("1.0", "end-1c")

    if Saved:
        file = open(saveLocation, "w+")
        file.write(t)
        file.close()
    else:
        Saved = True

        pla = sys.platform
        if pla == "linux":
            saveLocation = filedialog.asksaveasfilename(title="Select save location", initialdir="~/Documents")
        else:
            saveLocation = filedialog.asksaveasfilename(title="Select save location", initialdir="/")
        file = open(saveLocation, "w+")
        file.write(t)
        file.close()

def open_():
    global text, Saved, saveLocation
    Saved = True
    pla = sys.platform
    if pla == 'linux':
        saveLocation = filedialog.askopenfilename(initialdir="~/Documents", title="Select file to open")
    else:
        saveLocation = filedialog.askopenfilename(initialdir="/", title="Select file to open")
    
    text.delete("1.0", "end-1c")
    file1 = open(saveLocation, "r")
    text.insert("1.0", file1.read())
    file1.close()

def send():
	
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	msg = "Subject:"+subject.get("1.0", "end-1c")+"\n\n"+text.get("1.0", "end-1c")

	server.login(emailV, passwordV)
	server.sendmail(emailV, to.get("1.0", "end-1c"), msg)
	server.quit()

def loginInit():
	global login, email, password, emailT, passwordT, log
	login = Tk()
	login.title("Login")

	emailT = Label(login)
	emailT.config(text="Email:")
	emailT.grid(column=0, row=0)
	passwordT = Label(login)
	passwordT.config(text="Password:")
	passwordT.grid(column=0, row=1)

	email = Text(login)
	email.grid(column=1, row=0, sticky="nsew")
	email.config(height=1)
	password = Text(login)
	password.config(height=1)
	password.grid(column=1, row=1, sticky="nsew")

	login.columnconfigure(1, weight=100)

	log = Button(login)
	log.config(text="login", command=start)
	log.grid()

	login.mainloop()

def Init():
	global root, buttonF, to, Preferences, subject, text
	root = Tk()
	root.title("Haai Mail")
	root.config()

	buttonF = Frame(root)
	buttonF.grid()

	sendButton = Button(buttonF)
	sendButton.config(text="Send", command=send)
	sendButton.grid(row=0, column=0)

	saveButton = Button(buttonF)
	saveButton.config(text="Save", command=save)
	saveButton.grid(row=0, column=1)

	openButton = Button(buttonF)
	openButton.config(text="Open", command=open_)
	openButton.grid(row=0, column=2)

	Preferences = Menubutton(buttonF, text="Preferences")
	Preferences.grid(row=0, column=3)

	Preferences.menu = Menu(Preferences, tearoff=0)
	Preferences['menu'] = Preferences.menu

	Preferences.menu.add_checkbutton(label="Dark Theme", command=darkTheme)
	Preferences.menu.add_checkbutton(label="Light Theme", command=lightTheme)

	to = Text(root)
	to.config(fg="white", insertbackground="white", height="1")
	to.grid(row=1, column=0, sticky="nsew")

	subject = Text(root)
	subject.config(height="1")
	subject.grid(row=2, column=0, sticky="nsew")

	text = Text(root)
	text.grid(row=3, column=0, sticky="nsew")


	root.columnconfigure(0, weight=100)
	root.columnconfigure(3, weight=100)

	lightTheme()
	root.mainloop()

loginInit()
