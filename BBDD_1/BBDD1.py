import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

#Crear cursor o puntero
miCursor = miConexion.cursor()
#Ejecutar la consulta o query
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#Insertar datos
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES') ")
#Insertar varios productos o registros por medio de tuplas
"""
variosProductos = [

	("Camiseta", 10, "Deportes"),
	("Jarron", 10, "Cerámica"),
	("Camión", 10, "Juguetería")
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
"""
#Leer base de datos
miCursor.execute("SELECT * FROM PRODUCTOS ")

#Visualizar productos
variosProdustos = miCursor.fetchall()
#print(variosProdustos)

for producto in variosProdustos:
	print("Nombre Producto ", producto[0], "Seccion ", producto[2] )

#Verificar cambios o confirmar cambios
miConexion.commit()

miConexion.close()