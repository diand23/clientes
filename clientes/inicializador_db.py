import sqlite3

# Ruta al archivo SQL (ajustada según tu estructura)
sql_script_path = "Script.sql"

# Ruta de la base de datos
db_path = "datos_clientes.db"

# Conexión a la base de datos (se crea si no existe)
conexion = sqlite3.connect(db_path)
cursor = conexion.cursor()

# Leer y ejecutar el script SQL
with open(sql_script_path, "r", encoding="utf-8") as archivo_sql:
    script_sql = archivo_sql.read()
    cursor.executescript(script_sql)

conexion.commit()
cursor.close()
conexion.close()

print("Base de datos inicializada correctamente.")
