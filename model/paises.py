from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data



paises = Table("paises", meta_data, 
                Column("nombre_pais", String(255), primary_key=True),
                Column("capital", String(255), nullable=False),
                Column("poblacion", Integer, nullable=False))


meta_data.create_all(engine)