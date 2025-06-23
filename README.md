# clientes

Instalar la librería, para conectar la base de datos con python
pip install mysql-connector-python

Entiendo. Vamos paso a paso para crear y activar correctamente un **entorno virtual** en Windows y evitar errores.

---

### ✅ 1. Crear el entorno virtual

En la carpeta donde tengas tu proyecto (`C:\Users\merlo\OneDrive\Desktop\clientes`), abre PowerShell y ejecuta:

```powershell
python -m venv venv
```

Esto creará una carpeta llamada `venv` que contiene el entorno virtual.

---

### ✅ 2. Activar el entorno virtual

Una vez creado, actívalo con:

```powershell
.\venv\Scripts\Activate.ps1
```

Después de eso, deberías ver algo como esto en tu línea de comandos:

```powershell
(venv) PS C:\Users\merlo\OneDrive\Desktop\clientes>
```

---

### ⚠️ Si te da un error de permisos (ExecutionPolicy):

Windows puede bloquear la ejecución de scripts por seguridad. Si ves algo como:

```
execution of scripts is disabled on this system
```

Solución temporal (solo para esta sesión de PowerShell):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

Y luego vuelve a ejecutar:

```powershell
.\venv\Scripts\Activate.ps1
```

---

### ✅ 3. Instalar dependencias dentro del entorno

Ahora que estás dentro del entorno virtual, instala el módulo necesario:

```powershell
pip install mysql-connector-python
```

---

### ✅ 4. Ejecutar tu script

Con el entorno activado:

```powershell
python clientes\clientes.py
```

---

¿Quieres que te genere un `requirements.txt` para guardar tus dependencias o un `setup.sh` para automatizar todo esto?
