from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:12345678@localhost:3306/challenge")

conn = engine.connect()

meta_data = MetaData()
