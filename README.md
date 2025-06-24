# 🧩 Generación de un CRM

Un **CRM** te ayuda a organizar y centralizar la información de tus clientes, mejorar la 
comunicación, automatizar tareas, analizar datos para tomar mejores decisiones y aumentar las 
ventas ofreciendo un mejor servicio. Para su creación mostraré lo necesario para que se ejecute 
correctamente las funcionalidades.

### Generar BBDD

El primer paso ha sido la creación de la *BBDD* en **SQLLite Studio**, donde se ha indicado en 
la creación de las tablas *usuaios* y *facturas* los campos obligatorios y los opcionales a 
rellenar. Además, se ha indicado que el *Id_cliente*  de la tabla *usuarios* se añada 
automáticamen, para evitar posibles errores al añadir nuevos usuarios.

### 📁 CRM de Clientes

En segundo lugar, pasaremos a generar las funcionalidades requeridas de este CRM, las cuales 
aparecen en **clientes.py**, aplicando las intalaciones y conexiones necesarias para conectar la 
*BBDD*.

Este proyecto presenta la siguiente estructura de archivos:

```
Clientes/
|
├── clientes/
│   └── __init__.py
│   ├── clientes.py
|   ├── Script.sql
|   ├── inicializador_db.py
|   └── clientes.db
├── data/
│   └── datos_clientes.py
├── setup.py
├── requirements.txt
└── README.md
```

### Crear el entorno virtual

Lo esencial es trabajar en un entorno virtual para no sobrecargar de librerías nuestro
sistema, debido a que algunas librerías no son compatibles entre sí y pueden generar
conflictos si se instalan juntas. Por tanto, generamos un entorno virtual en la
carpeta donde se tiene el proyecto con el siguiente código:

```powershell
python -m venv venv
```

Esto creará una carpeta llamada `venv` que contiene el entorno virtual.

---

Una vez creado, se activará con:

```powershell
.\venv\Scripts\Activate.ps1
```

En consecuencia, se debería ver algo como esto en tu línea de comandos:

```powershell
(venv) PS C:\Users\merlo\OneDrive\Desktop\clientes>
```
En este espacio probaremos que nuestro **CRM** funciona.

### 📦 Indicaciones de uso

Para utilizar correctamente el sistema, es importante entender que al realizar consultas de 
información de usuarios (por ejemplo, buscando por nombre o correo electrónico), se obtienen los 
datos deseados sin problemas.

Sin embargo, cuando se agregan nuevos registros, como nuevos usuarios o nuevas facturas de 
clientes, no basta con insertar la información en la base de datos. Es necesario ejecutar un 
*commit* para que esos cambios se confirmen y se guarden de forma permanente.

Solo después de realizar este *commit*, la base de datos se actualiza realmente y los nuevos 
usuarios o facturas estarán disponibles para futuras consultas y aparecerán reflejados en el 
sistema.




