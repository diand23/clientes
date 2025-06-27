"""LIBRERIAS"""
import sqlite3
from datetime import datetime
import re
from pathlib import Path

"""CONEXIÓN A LA BASE DE DATOS"""
# Conexión a archivo SQLite (se crea si no existe)
# Carpeta donde está el script
BASE_DIR = Path(__file__).resolve().parent

# Ruta relativa a la base de datos
db_path = BASE_DIR / 'data' / 'datos_clientes.db'

# Crear carpeta 'data' si no existe
db_path.parent.mkdir(parents=True, exist_ok=True)
conexion = sqlite3.connect(db_path)

# Para que los resultados sean diccionarios
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()

"""Verificación de conexión"""
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()
print("Tablas en la base de datos:", tablas)

"""FUNCIONES """
# == Menú principal ==
def menu_principal():
    ''''Se crea un bucle infinito para mostrar el menú principal y 
    permitir al usuario seleccionar opciones.'''
    while True:
        print("\n=== SISTEMA CRM ===")
        print("1. Registrar nuevo usuario")
        print("2. Buscar usuario")
        print("3. Crear factura para ususrio")
        print("4. Mostrar todos los usuarios")
        print("5. Mostrar facturas de un usuario")
        print("6. Resumen financiero por usuario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            buscar_usuario()
        elif opcion == "3":
            crear_factura()
        elif opcion == "4":
            mostrar_todos_usuarios()
        elif opcion == "5":
            mostrar_facturas_usuario()
        elif opcion == "6":
            resumen_financiero_usuario()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

# == 1. Regitrar Usuario ==
def registrar_usuario():
    def email_valido(email):
        return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

    def email_existe(email):
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        return cursor.fetchone() is not None
    
    print("\n=== REGISTRO DE NUEVO USUARIO ===")
    nombre = input("Ingrese nombre: ").strip()
    apellidos = input("Ingrese apellidos: ").strip()
    email = input("Ingrese email: ").strip()
    telefono = input("Ingrese teléfono (opcional): ").strip() or None
    direccion = input("Ingrese dirección (opcional): ").strip() or None

    if not (nombre and apellidos and email):
        print("Todos los campos obligatorios deben estar completos.")
        return
    if not email_valido(email):
        print("Email no tiene un formato válido.")
        return
    if email_existe(email):
        print("Ese email ya está registrado.")
        return
    
    cursor.execute("""
        INSERT INTO usuarios (nombre, apellidos, email, telefono, direccion)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, apellidos, email, telefono, direccion))
    conexion.commit()

    id_cliente = cursor.lastrowid
    print("\n Usuario registrado exitosamente!")
    print(f"ID asignado: USR{id_cliente:03}")
    print("Fecha de registro: " + datetime.today().strftime('%d/%m/%Y'))

# == 2. Buscar Usuario ==
def buscar_usuario():
    print("\n=== BUSCAR USUARIO ===")
    print("1. Buscar por email\n2. Buscar por nombre\n")
    metodo = input("Seleccione método de búsqueda: ").strip()

    if metodo == "1":
        email = input("Ingrese email: ").strip()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))

    elif metodo == "2":
        nombre = input("Ingrese nombre: ").strip()
        cursor.execute("SELECT * FROM usuarios WHERE nombre LIKE ?", (f"%{nombre}%",))
    else:
        print("Opción inválida.")
        return

    usuario = cursor.fetchone()
    if usuario:
        print("\n--- USUARIO ENCONTRADO ---")
        print(f"ID: USR{usuario['id_cliente']:03}")
        print(f"Nombre: {usuario['nombre']} {usuario['apellidos']}")
        print(f"Email: {usuario['email']}")
        print(f"Teléfono: {usuario['telefono'] or 'No especificado'}")
        print(f"Dirección: {usuario['direccion'] or 'No especificada'}")
        print(f"Fecha de registro: {usuario['fecha_registro']}")
    else:
        print("Usuario no encontrado.")

# == 3. Crear Factura para Usuario ==
def crear_factura():
    print("\n=== CREAR FACTURA ===")
    email = input("Ingrese email del usuario: ").strip()
    cursor.execute("SELECT id_cliente, nombre, apellidos FROM usuarios WHERE email = ?", (email,))
    usuario = cursor.fetchone()

    if not usuario:
        print("Usuario no encontrado.")
        return
    else:
        print(f"\nUsuario encontrado: {usuario['nombre']} {usuario['apellidos']}")
        descripcion = input("Ingrese descripción del servicio/producto: ").strip()
        try:
            monto = float(input("Ingrese monto: "))
            if monto <= 0:
                raise ValueError
        except ValueError:
            print("Monto inválido. Debe ser un número positivo.")
            return
    print("Seleccione estado:")
    print("1. Pendiente\n2. Pagada\n3. Cancelada")
    estado_opcion = input("Estado: ")
    estados = {"1": "Pendiente", "2": "Pagada", "3": "Cancelada"}
    estado = estados.get(estado_opcion)

    if not estado:
        print("Estado inválido.")
        return

    cursor.execute("""
        INSERT INTO facturas (id_cliente, descripcion, monto, estado)
        VALUES (?, ?, ?, ?)
    """, (usuario['id_cliente'], descripcion, monto, estado))
    conexion.commit()
    numero = cursor.lastrowid

    print("\nFactura creada exitosamente!")
    print(f"Número de factura: FAC{numero:03}")
    print("Fecha de emisión: " + datetime.today().strftime('%d/%m/%Y %H:%M'))
    print(f"Cliente: {usuario['nombre']} {usuario['apellidos']}")
    print(f"Descripción: {descripcion}")
    print(f"Monto: ${monto:.2f}")
    print(f"Estado: {estado}")

# == 4. Lista de Usuarios ==
def mostrar_todos_usuarios():
    print("\n=== Lista DE USUARIOS ===")
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    if usuarios:
        for i, usuario in enumerate(usuarios, start=1):
            print(f"\nUsuario #{i}:")
            print(f"ID: USR{usuario['id_cliente']:03}")
            print(f"Nombre: {usuario['nombre']} {usuario['apellidos']}")
            print(f"Email: {usuario['email']}")
            print(f"Teléfono: {usuario['telefono'] if usuario['telefono'] else 'No especificado'}")
            # Mostrar fecha en formato dd/mm/yyyy
            fecha = usuario['fecha_registro']
            fecha_formateada = fecha.strftime('%d/%m/%Y') if isinstance(fecha, datetime) else str(fecha)
            print(f"Fecha de registro: {fecha_formateada}")    
    else:
        print("\nNo hay usuarios registrados.")

    print(f"\nTotal de usuarios registrados: {len(usuarios)}")
  
# == 5. Usuarios ==
def mostrar_facturas_usuario():
    print("\n=== FACTURAS POR USUARIO ===")
    email = input("Ingrese email del usuario: ").strip()
    cursor.execute("SELECT id_cliente, nombre, apellidos FROM usuarios WHERE email = ?", (email,))
    usuario = cursor.fetchone()

    if not usuario:
        print("Usuario no encontrado.")
        return
    cursor.execute("SELECT * FROM facturas WHERE id_cliente = ?", (usuario["id_cliente"],))
    facturas = cursor.fetchall()
    print(f"\n--- FACTURAS DE {usuario['nombre']} {usuario['apellidos']} ---")
    total_facturado = 0
    pendientes = 0
    for i, fac in enumerate(facturas, 1):
        print(f"\nFactura #{i}:")
        print(f"Número: FAC{fac['numero_factura']:03}")
        print(f"Fecha: {fac['fecha_emision']}")
        print(f"Descripción: {fac['descripcion']}")
        print(f"Monto: ${fac['monto']:.2f}")
        print(f"Estado: {fac['estado']}")
        total_facturado += fac["monto"]
        if fac["estado"] == "Pendiente":
            pendientes += fac["monto"]
    print(f"\nTotal de facturas: {len(facturas)}")
    print(f"Monto total facturado: ${total_facturado:.2f}")
    print(f"Monto pendiente: ${pendientes:.2f}")

# == 6. Resumen Financiero por Usuario ==
def resumen_financiero_usuario():
    print("\n=== RESUMEN FINANCIERO ===")
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    total_facturas = 0
    total_ingresos = 0
    total_pendientes = 0

    for usuario in usuarios:
        cursor.execute("SELECT estado, monto FROM facturas WHERE id_cliente = ?", (usuario["id_cliente"],))
        facturas = cursor.fetchall()
        total_usuario = sum(f["monto"] for f in facturas)
        pagadas = sum(f["monto"] for f in facturas if f["estado"] == "Pagada")
        pendientes = sum(f["monto"] for f in facturas if f["estado"] == "Pendiente")

        print(f"\nUsuario: {usuario['nombre']} {usuario['apellidos']} ({usuario['email']})")
        print(f"- Total facturas: {len(facturas)}")
        print(f"- Monto total: ${total_usuario:.2f}")
        print(f"- Facturas pagadas: ${pagadas:.2f}")
        print(f"- Facturas pendientes: ${pendientes:.2f}")

        total_facturas += len(facturas)
        total_ingresos += pagadas
        total_pendientes += pendientes

    print("\n--- RESUMEN GENERAL ---")
    print(f"Total usuarios: {len(usuarios)}")
    print(f"Total facturas emitidas: {total_facturas}")
    print(f"Ingresos totales: ${total_ingresos + total_pendientes:.2f}")
    print(f"Ingresos recibidos: ${total_ingresos:.2f}")
    print(f"Ingresos pendientes: ${total_pendientes:.2f}")

# == Menú principal ==
def menu_principal():
    ''''Se crea un bucle infinito para mostrar el menú principal y 
    permitir al usuario seleccionar opciones.'''
    while True:
        print("\n=== SISTEMA CRM ===")
        print("1. Registrar nuevo usuario")
        print("2. Buscar usuario")
        print("3. Crear factura para usuario")
        print("4. Mostrar todos los usuarios")
        print("5. Mostrar facturas de un usuario")
        print("6. Resumen financiero por usuario")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            buscar_usuario()
        elif opcion == "3":
            crear_factura()
        elif opcion == "4":
            mostrar_todos_usuarios()
        elif opcion == "5":
            mostrar_facturas_usuario()
        elif opcion == "6":
            resumen_financiero_usuario()
        elif opcion == "7":
            break
        else:
            print("Opción inválida.")

menu_principal()
cursor.close()
conexion.close()
