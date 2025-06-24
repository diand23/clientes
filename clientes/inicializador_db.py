import sqlite3
import os

# Ruta al script SQL (está en la misma carpeta que este script)
sql_script_path = os.path.join(os.path.dirname(__file__), "Script.sql")

# Ruta absoluta a la base de datos donde se guardará (puedes personalizarla)
db_path = os.path.join(os.path.dirname(__file__), "datos_clientes.db")

# Conexión a la base de datos
conexion = sqlite3.connect(db_path)
cursor = conexion.cursor()

# Leer y ejecutar el script SQL
with open(sql_script_path, "r", encoding="utf-8") as archivo_sql:
    script_sql = archivo_sql.read()
    cursor.executescript(script_sql)

# Confirmar y cerrar
conexion.commit()
print("Base de datos inicializada correctamente.")
cursor.close()
conexion.close()