# api-ppm
 ejercicio meli

Precondiciones:
# se instala mysql en el equipo local, yo instale este ejecutable en windows
mysql-installer-community-8.0.34.0.msi
# instalar python en el equipo local, yo instale este ejecutable en windows
python-3.11.5-amd64.exe
# habilitar un entorno virtual de python, si este entorno virtual ya existiera solo corresponde activarlo
python -m venv venv
# Para activar el entorno virtual(en windows), ir a la ruta:
cd venv\Scripts
# y ejecutar:
activate.ps1
# volver a la ruta de la aplicacion
cd..
cd..
# instalar algunos paquetes que serán necesarios
pip install uvicorn fastapi sqlalchemy pymysql httpx
###### no estoy seguro si tambien me hiso falta instalar
pip install mysql mysql-connector-python-rf 
# se ejecuta el servidor web uvicorn que instalamos
uvicorn main:app --reload