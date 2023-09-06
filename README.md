# api-ppm
 ejercicio meli

Precondiciones:
# Se instala mysql en el equipo local, yo instale el siguente ejecutable en windows:
mysql-installer-community-8.0.34.0.msi
# El usuario "root" debe tener la contraseña "12345678" o de lo contrario modificar el punto de conexion el fichero db.py con las credenciales correctas.
# Crear una base de datos llamada "challenge"
# instalar python en el equipo local, podemos instalar Python en powershell escribiendo "python" esto nos llevará a la Microsoft Store y desde ahi lo instalaremos.
# Abrimos la carpeta del proyecto en Visual Studio Code
# Abilitar un entorno virtual de python, para esto habririamos una nuava terminal en la raiz del proyecto y ejecutamos:
python -m venv venv
# Para activar el entorno virtual(en windows), ir a la ruta:
cd venv\Scripts
# Tengamos en cuenta ejecutar el siguiente scrpts de powershell (si no esta habilitado, habilitamos la ejecusion de scrpts) con el comando: 
Set-ExecutionPolicy -ExecutionPolicy Unrestricted
# Luego acivamos el entorno virtual ejecutando el siguente script de powershell:
activate.ps1
# Volver a la ruta de la aplicacion
cd..
cd..
# Instalar algunos paquetes que serán necesarios
pip install uvicorn fastapi sqlalchemy pymysql cryptography httpx
# Ejecutar el servidor web uvicorn que instalamos
uvicorn main:app --reload


# Como la aplicacion, desarrollada con FastAPI nos brinda una interfaz que nos permite interactuar con las funciones implementadas a traves de la URL:
http://localhost:8000/docs
# La base de datos se debe llenar con datos, para esto podemos ejecutar directamente en el navegador la siguiente URL:
http://localhost:8000/agregar/pais/automatico
# La funcionalidad requerida para la aplicacion se puede consultar a traves de la siguente URL, modificando el nombre del pais que se desea consultar:
http://localhost:8000/?nombre_pais=cuba
