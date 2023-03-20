import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""_summary_
Creacion de la variable para tener la base de datos

    """
sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

"""motor base de datos"""
engine = create_engine(database_url, echo=True)

"""Crear secion para conexion a la base de datos"""

session = sessionmaker(bind=engine)

"""manejo de las tablas"""

base = declarative_base()