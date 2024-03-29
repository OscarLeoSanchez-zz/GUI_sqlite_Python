import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()
"""
miCursor.execute('''

	CREATE TABLE PRODUCTOS (
	CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
	NOMBRE_ARTICULO VARCHAR(50),
	PRECIO INTEGER,
	SECCION VARCHAR(20)
	)
	''')
productos = [
	("AR01", "pelota", 20, "jugueteria"),
	("AR02", "pantalon", 15,"confeccion"),
	("AR03", "destornillador", 25,"ferreteria"),
	("AR04", "jarron", 45,"ceramica"),
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)
"""
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05','tren',15,'jugueteria')")

#AUTOMATIZAR INCREMENTO
"""
miCursor.execute('''

	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
	PRECIO INTEGER,
	SECCION VARCHAR(20)
	)
	''')"""
productos = [
	("pelotas", 20, "jugueteria")
#	("pantalon", 15,"confeccion"),
#	("destornillador", 25,"ferreteria"),
#	("jarron", 45,"ceramica"),
#	("camisa", 25,"confeccion")
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)


miConexion.commit()
miConexion.close()