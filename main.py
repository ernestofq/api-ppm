from fastapi import FastAPI
from router.router import pais

app = FastAPI(
    title="Challenge Paises del Mundo",
    description="API Rest desarrollada utilizando FastAPI.\n\n La aplicación es tiene como objetivo, luego de haberle introducido el nombre de un país, devolver una estructura json, con la capital, el porcentaje de población que ocupa ese país con respecto a la población mundial y el nombre del país con mayor población que le sigue.\n\n\n + La funcionalidad requerida para la aplicación se puede consultar a través de la siguiente URL, modificando el nombre del país que se desea consultar:\n\n       Ejemplo: http://5c1504635f74.sn.mynetname.net:34203/query/?nombre_pais={cuba}\n\n + Para garantizar la disponibilidad de los datos a consultar, podría ser necesario acceder a la siguiente URL:\n\n                http://5c1504635f74.sn.mynetname.net:34203/agregado/automatico" ,
    version="FastAPi v0.1.0",
    )
app.include_router(pais)