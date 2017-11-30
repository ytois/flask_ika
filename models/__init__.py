from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def session(user, password, host, db, port=5432):
    config = 'postgresql://{user}{password}@{host}:{port}/{db}'.format(
        user=user,
        password=':%s' % password if password else '',
        host=host,
        db=db,
        port=port,
    )
    engine = create_engine(config, pool_size=5)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    return db_session


def init_base(session):
    Base = declarative_base()
    Base.query = session.query_property()
    return Base

Base = init_base(
    session(
        current_app.config['DATABASE']['user'],
        current_app.config['DATABASE']['pass'],
        current_app.config['DATABASE']['host'],
        current_app.config['DATABASE']['db'],
    )
)
