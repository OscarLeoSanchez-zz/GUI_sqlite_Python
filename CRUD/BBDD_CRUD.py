import sqlite3

#miConexion = sqlite3.connect("GestionProductos")
#miCursor = miConexion.cursor()

# Lectura o Read R
"""
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'confeccion'")
productos = miCursor.fetchall()
print(productos)
"""
# Actualizar UPDATE U
#miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE NOMBRE_ARTICULO = 'pelota' ")

# Borrar ERRASE (se selecciona un criterio)
#miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 5")


#miConexion.commit()
#miConexion.close()

def funcion():
	a=0
	if a==0:
		return a , 1
def carsos(arg, dato):
	funcion()
	if arg==0 and dato ==1:
		print("Right")
funcion()