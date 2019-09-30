from tkinter import*
from tkinter import messagebox
import getpass
import sqlite3

root = Tk()
root.title("BBDD")
root.config(width=300, height=300)

#------------------------------------------
# Barra menu
def infoLoad():
	messagebox.showinfo("Information loaded", "Information loaded successfully")

def infAdicional():
	messagebox.showinfo("Informacion", "Programa 2019 realizado por Oscar")

def avisoLicencia():
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU libre")

def salirAplicacion():
	#valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
	valor = messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?")

	#if valor=="yes":
	if valor == True:
		root.destroy()

def cerrarDocumento():
	valor = messagebox.askretrycancel("Continuar", "¿Quiere continuar en la aplicación?")
	if valor == False:
		root.destroy()

barraMenu = Menu(root)

root.config(menu=barraMenu, width=300, height=300)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramienta = Menu(barraMenu, tearoff=0)

archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infAdicional)


barraMenu.add_cascade(label="Archivo", menu= archivoMenu)
barraMenu.add_cascade(label="Edicion", menu= archivoEdicion)
barraMenu.add_cascade(label="Herramienta", menu= archivoHerramienta)
barraMenu.add_cascade(label="Ayuda", menu= archivoAyuda)
#-----------------------------------------------------------------

miFrame = Frame(root)
miFrame.pack(expand=False)
miFrame.config( width=300, height=300)
frameButton = Frame(root)
frameButton.pack()

name = StringVar()
lastname = StringVar()
phone = StringVar()
direction = StringVar()
email = StringVar()
password = StringVar()
Nombre = StringVar()




clearButton = Button(frameButton,text="Clear", command = lambda:Clear())
clearButton.grid(row=7, column=1, padx=10, pady=10,sticky='w')
closeButton = Button(frameButton,text="Close",command=lambda:salirAplicacion())
closeButton.grid(row=7, column=2, padx=10, pady=10,sticky='w')
erraseButton = Button(frameButton,text="Errase", command=lambda:dataErrase())
erraseButton.grid(row=7, column=3, padx=10, pady=10,sticky='w')
acepButton = Button(frameButton,text="Accept" , command=lambda:dataGet())
acepButton.grid(row=7, column=4, padx=10, pady=10,sticky='w')


nameLabel = Label(miFrame, text='Name')
nameLabel.grid(row=1, column=1, sticky='E', padx=5)
nameEntry = Entry(miFrame, width=20, textvariable=name)
nameEntry.grid(row=1, column=2, padx=30, pady=10,sticky='w')


lastnameLabel = Label(miFrame, text='Lastame')
lastnameLabel.grid(row=2, column=1, sticky='E', padx=5)
lastnameEntry = Entry(miFrame, width=20,textvariable=lastname)
lastnameEntry.grid(row=2, column=2, padx=30, pady=10,sticky='w')

phoneLabel = Label(miFrame, text='Phone')
phoneLabel.grid(row=3, column=1, sticky='E', padx=5)
phoneEntry = Entry(miFrame, width=20,textvariable=phone)
phoneEntry.grid(row=3, column=2, padx=30, pady=10,sticky='w')

directionLabel = Label(miFrame, text='Direction')
directionLabel.grid(row=4, column=1, sticky='E', padx=5)
directionEntry = Entry(miFrame, width=20,textvariable=direction)
directionEntry.grid(row=4, column=2, padx=30, pady=10,sticky='w')

emailLabel = Label(miFrame, text='Email')
emailLabel.grid(row=5, column=1, sticky='E', padx=5)
emailEntry = Entry(miFrame, width=20, textvariable=email)
emailEntry.grid(row=5, column=2, padx=30, pady=10,sticky='w')

passwordLabel = Label(miFrame, text='Password')
passwordLabel.grid(row=6, column=1, sticky='E', padx=5)
passwordEntry = Entry(miFrame, width=20,textvariable=password, show="*")
passwordEntry.grid(row=6, column=2, padx=30, pady=10,sticky='w')



def Clear():
	nameEntry.delete(0,END)
	lastnameEntry.delete(0,END)
	phoneEntry.delete(0,END)
	directionEntry.delete(0,END)
	emailEntry.delete(0,END)
	passwordEntry.delete(0,END)	
#print(name)
def dataGet():
	name1 = name.get()
	lastname1 = lastname.get()
	phone1 = phone.get()
	direction1 = direction.get()
	email1 = email.get()
	password1 = password.get()
	try:
	#	phone1 = int(phone1)
		data = [(
			name1, lastname1, phone1, direction1, email1, password1

			)]
		print(data)
		loadData(data)
	except Exception as e:
		messagebox.showwarning("ERROR", "No se puede crear elemento")


def loadData(arg):
	a = list()
	n=0
	for i in arg:
		for j in i:
			j = str(j)
			if j!="":	
				if len(j) >= 3:
					a.append(j)
			else:
				n+=1
		if n>0:
			messagebox.showwarning("Dato no valido", "Alguno de los datos ingresados no son validos, recuerda no dejar espacios en blanco")
		else:
			try:
				int(i[2])
				if len(i) == len(a):
					name=i[0]
					lastname=i[1]
					phone=i[2]
					direction=i[3]
					email=i[4]
					password=i[5]
					try:
						crearBBDD()
						fillBBDD(name, lastname, phone, direction, email, password)
					except sqlite3.OperationalError:
						fillBBDD(name, lastname, phone, direction, email, password)
						infoLoad()
				else:
					messagebox.showwarning("ERROR", "Los datos deben tener al menos tres caracteres")

			except Exception as e:
				messagebox.showwarning("Dato no valido", "Numero de telefono no valido")

"""		if len(i) == len(a):
			name=i[0]
			lastname=i[1]
			phone=i[2]
			direction=i[3]
			email=i[4]
			password=i[5]
			try:
				crearBBDD()
				fillBBDD(name, lastname, phone, direction, email, password)
			except sqlite3.OperationalError:
				fillBBDD(name, lastname, phone, direction, email, password)
				infoLoad()
			
"""
def checkData(datos):
	pass

	#for i in data:
	#	print(i)
	#print(data)
	

def crearBBDD():
	miConeccion = sqlite3.connect("Usuarios")
	miCursor = miConeccion.cursor()

	miCursor.execute('''
		CREATE TABLE USUARIOS (
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		NAME VARCHAR (50),
		LASTNAME VARCHAR (50),
		PHONE INTEGER UNIQUE,
		DIRECTION VARCHAR (50),
		EMAIL VARCHAR (50),
		PASSWORD VARCHAR (50)
		)
		''')
	miConeccion.commit()
	miConeccion.close()



def fillBBDD(name, lastname, phone, direction, email, password):
	myConnection = sqlite3.connect("Usuarios")
	myCursor = myConnection.cursor()

	data = [
			(name, lastname, phone, direction, email, password)
			]
	print(data)
	myCursor.executemany("INSERT INTO USUARIOS VALUES (NULL,?,?,?,?,?,?)", data)
	myConnection.commit()
	myConnection.close()


def dataErrase():
	name1 = name.get()
	lastname1 = lastname.get()
	phone1 = phone.get()
	direction1 = direction.get()
	email1 = email.get()
	password1 = password.get()
	print("name :" , name1, lastname1, phone1, direction1, email1, password1)
	myConnection = sqlite3.connect("Usuarios")
	myCursor = myConnection.cursor()
	if name1 != "":
		y=myCursor.execute("DELETE FROM USUARIOS WHERE NAME = ?", (name1,))
		print(y)
		messagebox.showinfo("Operacion exitosa", "Dato borrado exitosamente")
	elif lastname != "": 
		myCursor.execute("DELETE FROM USUARIOS WHERE LASTNAME = ?", (lastname1,))
		messagebox.showinfo("Operacion exitosa", "Dato borrado exitosamente")
		print("hola", lastname1)
	elif phone1 != "" : 
		myCursor.execute("DELETE FROM USUARIOS WHERE PHONE = ?", (phone1,))
		messagebox.showinfo("Operacion exitosa", "Dato borrado exitosamente")
	elif direction1 != "" : 
		myCursor.execute("DELETE FROM USUARIOS WHERE DIRECTION = ?", (direction1,))
		messagebox.showinfo("Operacion exitosa", "Dato borrado exitosamente")
	elif email1 != "" : 
		myCursor.execute("DELETE FROM USUARIOS WHERE EMAIL = ?", (email1,))
		messagebox.showinfo("Operacion exitosa", "Dato borrado exitosamente")
	elif password1 != "" : 
		myCursor.execute("DELETE FROM USUARIOS WHERE PASSWORD = ?", (password1,))
		messagebox.showinfo("Operacion exitosa", "Dato borrado exitosamente")
	else:
		messagebox.showinfo("No Element", "Elemento no encontrado")
	myConnection.commit()
	myConnection.close()	






#fillBBDD(name, lastname, phone, direction, email, password)
#fillBBDD("Les", "Car", 3245, "Call", "cas@", "23ea")
root.mainloop()