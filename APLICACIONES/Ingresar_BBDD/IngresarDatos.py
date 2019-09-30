from tkinter import*
from tkinter import messagebox
import sqlite3 as sql
#-----------------------Funciones 

def conexionBBDD():
	miConexion = sql.connect("Usuarios")
	miCursor = miConexion.cursor()
	try:
		miCursor.execute('''
			CREATE TABLE DATOSUSUARIOS (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NAME VARCHAR (50),
			LASTNAME VARCHAR (50),
			PHONE INTEGER UNIQUE,
			DIRECTION VARCHAR (50),
			EMAIL VARCHAR (50),
			PASSWORD VARCHAR (50),
			COMENTARIOS VARCHAR (100)
			)
			''')
		print('c')
		messagebox.showinfo("BBDD", "Base de datos creada con éxito")
	except:
		messagebox.showwarning("¡Atención!","La Base de datos ya está crada")
		
def salirAplicacion():
	valor = messagebox.askquestion("Salir","¿Desea salir de la aplicación?")
	if valor =="yes":
		root.destroy()

def borrarCampos():
	#nameEntry.delete(0,END)
	#lastnameEntry.delete(0,END)
	#phoneEntry.delete(0,END)
	#directionEntry.delete(0,END)
	#emailEntry.delete(0,END)
	#passwordEntry.delete(0,END)
	name.set("")
	lastname.set("")
	phone.set("")
	direction.set("")
	email.set("")
	password.set("")
	textoComentario.delete(1.0, END)
	#idEntry.delete(0,END)

def Crear():
	miConexion = sql.connect("Usuarios")
	miCursor = miConexion.cursor()

	miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'"+ name.get()+
		"','"+lastname.get()+
		"','"+phone.get()+
		"','"+direction.get()+
		"','"+email.get()+
		"','"+password.get()+
		"','"+textoComentario.get(1.0,END)+"')")
	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro Insetado con éxito")
	borrarCampos()

def Leer():
	miConexion = sql.connect("Usuarios")
	miCursor = miConexion.cursor()
	borrarCampos()

	miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID =" + id.get())

	elUsuario = miCursor.fetchall()
	print(elUsuario)
	for usuario in elUsuario:
		id.set(usuario[0])
		name.set(usuario[1])
		lastname.set(usuario[2])
		phone.set(usuario[3])
		direction.set(usuario[4])		
		email.set(usuario[5])
		password.set(usuario[6])
		textoComentario.insert(1.0,usuario[7])
	miConexion.commit()

def Actualizar():
	miConexion = sql.connect("Usuarios")
	miCursor = miConexion.cursor()
	miCursor.execute("UPDATE DATOSUSUARIOS SET NAME = '"+ name.get()+
		"',LASTNAME='"+lastname.get()+
		"',PHONE='"+phone.get()+
		"',DIRECTION='"+direction.get()+
		"',EMAIL='"+email.get()+
		"',PASSWORD='"+password.get()+
		"',COMENTARIOS='"+textoComentario.get(1.0,END) + 
		"' WHERE ID =" + id.get())

	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro actualizado con éxito")
	borrarCampos()

def Eliminar():
	miConexion = sql.connect("Usuarios")
	miCursor = miConexion.cursor()
	miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + id.get())
	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro borrado exitosamente")
	borrarCampos()

#------------------ Interface
root = Tk()
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300,height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar Campos",command=borrarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear",command=Crear)
crudMenu.add_command(label="Leer", command=Leer)
crudMenu.add_command(label="Actualizar", command=Actualizar)
crudMenu.add_command(label="Borrar", command=Eliminar)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="Crud", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# -----------Comienzo de Campos ----------------------

miFrame = Frame(root)
miFrame.pack()
frameButton = Frame(root)
frameButton.pack()

name = StringVar()
lastname = StringVar()
phone = StringVar()
direction = StringVar()
email = StringVar()
password = StringVar()
id = StringVar()

nameLabel = Label(miFrame, text='Name')
nameLabel.grid(row=1, column=1, sticky='E', padx=5)
nameEntry = Entry(miFrame, width=20, textvariable=name)
nameEntry.grid(row=1, column=2, padx=30, pady=10,sticky='w')
nameEntry.config(fg="red",justify="right")

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

idLabel = Label(miFrame, text='id')
idLabel.grid(row=7, column=1, sticky='E', padx=5)
idEntry = Entry(miFrame, width=20,textvariable=id)
idEntry.grid(row=7, column=2, padx=30, pady=10,sticky='w')

textoComentario = Text(miFrame, width=20, height=5)
textoComentario.grid(row=8, column=2, padx=20,pady=5)
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=8,column=3,sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)


# ---------------------------Botones
createButton = Button(frameButton,text="Create",command=Crear)
createButton.grid(row=1, column=1, padx=10, pady=10,sticky='w')
readButton = Button(frameButton,text="Read", command=Leer)
readButton.grid(row=1, column=2, padx=10, pady=10,sticky='w')
deleteButton = Button(frameButton,text="Delate", command=Eliminar)
deleteButton.grid(row=1, column=3, padx=10, pady=10,sticky='w')
updateButton = Button(frameButton,text="Update", command=Actualizar)
updateButton.grid(row=1, column=4, padx=10, pady=10,sticky='w')



root.mainloop()