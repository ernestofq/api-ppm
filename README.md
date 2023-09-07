## api-ppm
Desarrollo solicitado por MeLi.

Precondiciones para diponibilizar el entorno de desarrollo de esta aplicación:
#### Se instala mysql en el equipo local, yo instale el siguiente ejecutable en windows:
mysql-installer-community-8.0.34.0.msi
#### El usuario "root" debe tener la contraseña "12345678" o de lo contrario modificar el punto de conexión el fichero db.py con las credenciales correctas.
#### Crear una base de datos llamada "challenge"
#### Instalar python en el equipo local, podemos instalar Python en powershell escribiendo "python" esto nos llevará a la Microsoft Store y desde ahí lo instalaremos.
#### Ubicamos la carpeta del proyecto, en este caso (api-ppm), si dentro de esta carpeta encontramos con una carpeta llamada "venv" la borramos para evitar algún conflicto luego con el entorno virtual que crearemos.
#### Abrimos la carpeta del proyecto en Visual Studio Code.
#### Abilitar un entorno virtual de python, para esto abriríamos una nueva terminal en la raíz del proyecto y ejecutamos:
python -m venv venv
#### Para activar el entorno virtual (en windows), ir a la ruta:
cd venv\Scripts
#### Tengamos en cuenta ejecutar el siguiente script de powershell (si no está habilitado, habilitamos la ejecución de scripts) con el comando: 
Set-ExecutionPolicy -ExecutionPolicy Unrestricted
#### Luego activamos el entorno virtual ejecutando el siguiente script de powershell:
activate.ps1
#### Volver a la ruta de la aplicación.
cd..
cd..
#### Instalar algunos paquetes que serán necesarios
pip install uvicorn fastapi sqlalchemy pymysql cryptography httpx
#### Ejecutar el servidor web uvicorn que instalamos.
uvicorn main:app --host 0.0.0.0 --reload
### Por si se llegara a necesitar en la parpeta del proyecto se encuentra el fichero "requerimientos.txt" que muestra los paquetes y dependencias que son necesarios estén instalados.
#### En este punto estaríamos listos para editar nuestro codigo y ademas probar las funcionalidades.


#### Como la aplicación, desarrollada con FastAPI nos brinda una interfaz que nos permite interactuar con las funciones implementadas a través de la URL:
http://localhost:8000/docs
#### La base de datos se debe llenar con datos, para esto podemos ejecutar directamente en el navegador la siguiente URL:
http://localhost:8000/agregar/pais/automatico
#### La funcionalidad requerida para la aplicación se puede consultar a través de la siguiente URL, modificando el nombre del país que se desea consultar:
http://localhost:8000/?nombre_pais=cuba

## ¡¡La aplicacion ya se encuantra disponible de manera ONLINE en la siguiente URL!!
http://5c1504635f74.sn.mynetname.net:34203
