import configparser
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entities import entities

dir_path = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
config.read(dir_path + '/../conf/config.ini')

db_url = f"postgresql://{config['postgresqlDB']['user']}:{config['postgresqlDB']['pass']}" \
         f"@{config['postgresqlDB']['host']}:5432/{config['postgresqlDB']['db']}"
engine = create_engine(db_url)


def connect():
    try:
        Base = entities.Base
        Base.metadata.create_all(engine)
        session_conf = sessionmaker(bind=engine)
        session = session_conf()
        print("DB Session Established!")
        return session
    except Exception as error:
        print("Error while connecting to PostgreSQL", error)
