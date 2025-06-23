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





Gracias por el detalle. Aunque antes funcionaba, ahora estás viendo este error:

```
ModuleNotFoundError: No module named 'mysql'
```

Esto indica que **el entorno actual donde estás ejecutando `clientes.py` no tiene instalado `mysql-connector-python`**, aunque tú lo creas instalado.

---

### ✅ Solución Paso a Paso

#### 1. Asegúrate de estar dentro del entorno virtual

En PowerShell, deberías ver algo como esto al inicio del prompt:

```powershell
(venv) PS C:\Users\merlo\OneDrive\Desktop\clientes>
```

Si **no** ves el `(venv)`, actívalo:

```powershell
.\venv\Scripts\Activate.ps1
```

---

#### 2. Instala el módulo dentro del entorno virtual

Con el entorno activado, instala el conector de MySQL:

```powershell
pip install mysql-connector-python
```

Verifica que se instaló con:

```powershell
pip show mysql-connector-python
```

Debería mostrarte información como:

```
Name: mysql-connector-python
Version: x.x.x
Location: ...venv\Lib\site-packages
```

---

#### 3. Vuelve a ejecutar tu script

Estando dentro del entorno, vuelve a ejecutar el script desde el directorio raíz del proyecto:

```powershell
python clientes\clientes.py
```

---

### ✅ Si sigue fallando

* Asegúrate de **no estar usando Anaconda** para ejecutar el script (eso parece estar ocurriendo por el error anterior que mencionaba `anaconda3\python.exe`)
* Si quieres estar completamente seguro, fuerza a usar el Python del entorno virtual con:

```powershell
where python
```

Deberías ver la ruta del `venv`, no la de `Anaconda`.



