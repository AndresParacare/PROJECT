import sqlalchemy as db
import persistence.model as mod

#Motor de la base de datos
engine = db.create_engine('sqlite:///db/login.sqlite', echo=True, future=True)
mod.Base.metadata.create_all(engine)